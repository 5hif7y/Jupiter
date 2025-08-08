
@echo off
setlocal


rem Parameters:
rem    "/r or /R" - Rebuild
rem    "/c or /C" - Clean


echo - Building Debug

call _build_solution debug %1


endlocal
