@echo off
for %%v in (*.ui) do pyuic5 -x %%v -o ../Ui/%%~nv.py