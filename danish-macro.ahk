#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

!a::
Send, å
return

!e::
Send, æ
return

!o::
Send, ø
return

!+a::
Send, Å
return

!+e::
Send, Æ
return

!+o::
Send, Ø
return