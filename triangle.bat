@echo off
@for /l %%a in (0 1 10) do (
	for /l %%b in (0 1 10) do (
		for /l %%c in (-2 1 10) do py triangle.py %%a %%b %%c))
@pause