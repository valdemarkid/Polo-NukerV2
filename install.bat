@echo off 
Title Download Modules...
python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
python -m pip install -r requirements.txt
cls
Title Downloading Modules
echo starter.py


cd console


start starter.py


cd ..

goto end


echo Python is not installed. Please install Python and try again.
goto end

echo Pip is not installed. Please install pip and try again.
goto end


