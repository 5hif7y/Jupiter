
@echo off
setlocal


rem Parameters:
rem    "/r or /R" - Rebuild
rem    "/c or /C" - Clean

echo - Building Release

call _build_solution release %1


endlocal
