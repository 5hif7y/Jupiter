
echo off
setlocal


rem Parameters:
rem    "/r or /R" - Rebuild
rem    "/c or /C" - Clean

echo - Building All

del build.log

call build_release %1
call build_debug %1


endlocal
