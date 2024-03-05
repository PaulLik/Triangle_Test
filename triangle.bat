@echo off
@for /l %%a in (1 1 10) do (
	for /l %%b in (1 1 10) do (
		for /l %%c in (1 1 10) do py triangle.py %%a %%b %%c))
@pause