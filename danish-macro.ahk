#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

![::
Send, å
return

!;::
Send, æ
return

!'::
Send, ø
return

!+[::
Send, Å
return

!+;::
Send, Æ
return

!+'::
Send, Ø
return
