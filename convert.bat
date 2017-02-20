@echo off
echo %1
echo %2

set var=%~f3
echo %var%

cd %1

java -jar %2 %var%

cd ..