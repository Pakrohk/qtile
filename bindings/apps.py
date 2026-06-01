# built in libs
from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy

# Modules and Others Config files
from .vars import (app_menu, browser, file_manager, home, print_screen,
                   qt5_config, scaling_menu, screenshot, shell_menu, super,
                   term, toggle_compositor, win_selector)


def init_apps_run():
    if qtile.core.name == "wayland":
        clipboard = "cliphist list | rofi -dmenu -p 'Clipboard' | cliphist decode | wl-copy"
    else:
        clipboard = 'rofi -modi "clipboard:greenclip print" -show clipboard'

    keys = [
        Key([super], "Return", lazy.spawn(term)),
        Key([super], "b", lazy.spawn(browser)),
        Key([super], "d", lazy.spawn(app_menu)),
        Key([super], "r", lazy.spawn(shell_menu)),
        Key([super], "w", lazy.spawn(win_selector)),
        Key([super], "v", lazy.spawn(clipboard)),
        Key([super], "e", lazy.spawn(file_manager)),
        Key([super], "q", lazy.spawn(qt5_config)),
        Key([super], "s", lazy.spawn(scaling_menu)),
        Key([super], "c", lazy.spawn(toggle_compositor)),
        Key([], print_screen, lazy.spawn(f"{screenshot} -xc {home}/Pictures/")),
        Key([super], print_screen, lazy.spawn(f"{screenshot} -xsc {home}/Pictures/")),
    ]

    return keys
