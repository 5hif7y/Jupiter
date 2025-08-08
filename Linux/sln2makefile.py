#!/usr/bin/python

##############################################################
#
# sln2makefile.py
#
# Script to generate a top-level makefile from a Visual Studio
# .NET 2002 solution file.  Walks project dependencies to 
# generate target dependencies.
#
# Usage: sln2makefile -s <solution file> -p <project name> 
#
# (c) 2004 Monolith Productions, Inc. All Rights Reserved.
# (c) 2004 TouchdownEntertainment Inc. All Rights Reserved.
#
# dlj - 11/04 modified for .Net 2002 and Jupiter
#
##############################################################

import string, re, getopt, sys

##############################################################
# Function: findProjectByGUID
##############################################################
def findProjectByGUID(projectGUID):
    for projectName, projectInfo in projectDictionary.iteritems():
        if projectInfo.group('project_guid') == projectGUID:
            return projectName

##############################################################
# Function: emitMakefileEntry
##############################################################
def emitMakefileEntry(projectInfo):
    # find the project name and paths
    projectGUID = projectInfo.group('project_guid')
    projectName = projectInfo.group('project_name')
    vcprojPath = projectInfo.group('project_path')
    vcprojPath = string.replace(vcprojPath, "\\", "/")
    projectDir = vcprojPath[:vcprojPath.rfind("/")]
    makefilePath = projectDir + "/Makefile"

    # only process this project if we haven't emitted it yet
    if (not emittedDictionary.has_key(projectGUID)):
        # build list of dependency names
        dependencyString = ""
        if dependenciesDictionary.has_key(projectGUID):
            dependencies = dependenciesDictionary[projectGUID]
            for dependencyGUID in dependencies:
                if vsver == 7:
                    dependencyName = findProjectByGUID("{" + dependencyGUID + "}")
                else:
                    dependencyName = findProjectByGUID(dependencyGUID)

                dependencyString += " " + dependencyName
    
        # emit makefile entries for the project
        print projectName + ": " + makefilePath + dependencyString
        print "	@(echo 'Compiling " + projectName + "...')"
        print "	@(cd " + projectDir + ";make)"
        print
        print makefilePath + ": " + vcprojPath
        print "	@($(SHELL) -ec 'xsltproc $(VCPROJSCRIPTPATH)/vcproj2makefile.xsl " + vcprojPath + " > " + makefilePath + "')"
        print
    
        # recurse for dependencies
        if dependenciesDictionary.has_key(projectGUID):
            dependencies = dependenciesDictionary[projectGUID]
            for dependencyGUID in dependencies:
                if vsver == 7:
                    dependencyName = findProjectByGUID("{" + dependencyGUID + "}")
                else:
                    dependencyName = findProjectByGUID(dependencyGUID)

                dependencyInfo = projectDictionary[dependencyName]
                emitMakefileEntry(dependencyInfo)
    
        emittedDictionary[projectGUID] = projectName;
            
##############################################################
# Main
##############################################################                                                                                    
try:
    opts, args = getopt.getopt(sys.argv[1:], "s:p:")
except getopt.GetoptError:
        print "usage: sln2make -s <solution file> -p <project name>" 
        sys.exit(2)

solutionFileName = None
projectName = None

for o, a in opts:
    if o == "-s":
        solutionFileName = a    
    if o == "-p":
        projectName = a

if (solutionFileName == None or projectName == None):
    print "ERROR: Invalid arguments"
    sys.exit(2)

# read the solution file
solutionFile = open(solutionFileName)

# make sure this is a valid solution
header = solutionFile.readline();

if string.find(header, "Microsoft Visual Studio Solution File, Format Version 7.00") == 0:
    vsver = 7
elif string.find(header, "Microsoft Visual Studio Solution File, Format Version 8.00") == 0:
    vsver = 8
else:
    print "ERROR: not a Visual Studio .NET 2002 or 2003 solution file"
    sys.exit(2)

# split into projects and the global section
fileData = solutionFile.read();
projects  = fileData.split("Project(");

# clean up the list
del projects[0]
projects[len(projects)-1] = projects[len(projects)-1].split("Global")[0]

#visual 7 does dependencies differently ( parse separate dependency area )
if vsver == 7:
    depends = fileData.split("GlobalSection(ProjectDependencies) = postSolution");
    del depends[0]
    depends[len(depends)-1] = depends[len(depends)-1].split("EndGlobalSection")[0]

# index all the projects and dependencies
projectDictionary = {}
dependenciesDictionary = {}

for project in projects:
    projectPattern = re.compile(r'"(?P<solution_guid>\S+)"\) = "(?P<project_name>\S+)", "(?P<project_path>\S+)", "(?P<project_guid>\S+)"')
    projectInfo = projectPattern.search(project)
    
    currentProjectName = projectInfo.group('project_name')
    currentProjectGUID = projectInfo.group('project_guid')
    projectDictionary[currentProjectName] = projectInfo

    if vsver == 7:
        dependencyPattern = re.compile(r'' + currentProjectGUID +'\S+ = {(?P<dependency_guid>\S+)}+')
        dependencyInfo = dependencyPattern.findall(depends[0])
    else:
        dependencyPattern = re.compile(r'(?P<dependency_guid>\S+) = {\S+}+')
        dependencyInfo = dependencyPattern.findall(project)

    
    if dependencyInfo:
        dependenciesDictionary[currentProjectGUID] = dependencyInfo 


# find the requested project
if not projectDictionary.has_key(projectName):
    print "ERROR: Project'" + projectName + "' does not exist in solution"
    sys.exit(2)

projectInfo = projectDictionary[projectName]

# keep track of projects we've emitted
emittedDictionary = {}

# now that we have all of the GUIDs and dependency mappings, emit the makefile
print """
###############################################################
#
# Auto-generated makefile for %s.
#
# (c) 2004 Monolith Productions, Inc. All Rights Reserved.
# (c) 2004 TouchdownEntertainment Inc. All Rights Reserved.
#
###############################################################
""" % solutionFileName

# output the build rules
emitMakefileEntry(projectInfo)

# output the clean rule
print "clean:"

for projectInfo in projectDictionary.itervalues():
    projectGUID = projectInfo.group('project_guid')
    # only process projects that we have emitted
    if (emittedDictionary.has_key(projectGUID)):
            vcprojPath = projectInfo.group('project_path')
            vcprojPath = string.replace(vcprojPath, "\\", "/")
            projectDir = vcprojPath[:vcprojPath.rfind("/")]
            makefilePath = projectDir + "/Makefile"
            print "	@(if [ -e " + makefilePath + " ]; then make -C " + projectDir + " clean; fi)"
    
for projectInfo in projectDictionary.itervalues():
    projectGUID = projectInfo.group('project_guid')
    # only process projects that we have emitted
    if (emittedDictionary.has_key(projectGUID)):
            vcprojPath = projectInfo.group('project_path')
            vcprojPath = string.replace(vcprojPath, "\\", "/")
            projectDir = vcprojPath[:vcprojPath.rfind("/")]
            makefilePath = projectDir + "/Makefile"
            print "	rm -f " + makefilePath
    
print
    
# output rebuild rule
print "rebuild: clean " + projectName

        

