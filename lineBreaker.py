"""Removes newlines from text coppied to clipboard then places back into clipboard
   set up with win hotkey
   exe in C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Line Breaker\lineBreaker04.exe
   keyboard shortcut ctrl+Alt+2
   """

import win32clipboard

win32clipboard.OpenClipboard()

clip = win32clipboard.GetClipboardData()
win32clipboard.EmptyClipboard()
clip = clip.replace('\n',' ')
clip = clip.replace('\r',' ')
win32clipboard.SetClipboardText(clip)
win32clipboard.CloseClipboard()

