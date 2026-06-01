#!/bin/bash

# Qtile Help Menu (using yad)

HELP_TEXT="=== Qtile Help ===

Window Management:
- [Super] + Enter    : Terminal
- [Super] + d        : App launcher (rofi)
- [Super] + Shift + w : Close window
- [Super] + Space    : Next layout
- [Super] + Tab      : Focus next screen
- [Super] + h/j/k/l  : Focus left/down/up/right
- [Super] + Shift + h/j/k/l : Move window

System Control:
- XF86AudioRaiseVolume : Volume up
- XF86AudioLowerVolume : Volume down
- XF86AudioMute        : Mute
- [Super] + Shift + c  : Toggle compositor (X11 only)
- [Super] + s          : Scaling menu

Power Management:
- Click ⏻ widget     : Power menu (Lock, Sleep, Reboot, Shutdown)

Screenshots:
- Print              : Select area → copy to clipboard
- Shift + Print       : Full screen → copy to clipboard

Help:
- F1                 : This help window"

if command -v yad >/dev/null 2>&1; then
    yad --text-info --title="Qtile Help" --width=700 --height=500 \
        --fontname="Sans 12" --show-uri --button="Close:0" \
        --text="$HELP_TEXT"
else
    # Fallback to rofi if yad is not installed
    echo -e "$HELP_TEXT" | rofi -dmenu -i -p "Help (yad missing)" -theme-str 'window {width: 40%;}'
fi
