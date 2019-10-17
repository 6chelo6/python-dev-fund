#!/usr/bin/env python

	

from win32gui import GetWindowText, GetForegroundWindow
print GetWindowText(GetForegroundWindow())

