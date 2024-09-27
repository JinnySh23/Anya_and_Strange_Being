@echo off
rem
git add -A
git commit -m %date%
git push origin main
pause