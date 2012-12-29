@echo off

( 
    @cd /d "%~dp0" 
) && (
    if exist ".appcfg_cookies" (@del /f /q .appcfg_cookies)
) && (
    set PYTHONSCRIPT="import sys,os;execfile('uploader.py');"
) && (
    "..\local\proxy.exe"
)

@pause>NUL

@echo off

