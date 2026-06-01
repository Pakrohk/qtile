#!/bin/bash

# Qtile Help Menu

HELP_TEXT="=== Qtile Help ===

[Super] + Enter    : Terminal
[Super] + d        : App launcher (rofi)
[Super] + Shift + w : Close window
[Super] + Space    : Next layout
[Super] + Tab      : Focus next screen
[Super] + h/j/k/l  : Focus left/down/up/right
[Super] + Shift + h/j/k/l : Move window

XF86AudioRaiseVolume : Volume up
XF86AudioLowerVolume : Volume down
XF86AudioMute        : Mute
[Super] + Shift + c  : Toggle compositor (X11 only)
[Super] + s          : Scaling menu

Click ⏻ widget     : Power menu

F1 – this help"

echo -e "$HELP_TEXT" | rofi -dmenu -i -p "Help" -theme-str 'window {width: 40%;}'
