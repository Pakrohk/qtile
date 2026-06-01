# built in libs
from libqtile.config import Key
from libqtile.lazy import lazy

# Modules and Others Config files
from layouts.bsp import resize_down, resize_left, resize_right, resize_up

from .vars import alt, help_menu, super, toggle_compositor, volume_controller


# Define keybindings
def init_keys():
    keys = [
        # Switch between windows in current stack pane
        Key([super], "h", lazy.layout.left()),
        Key([super], "k", lazy.layout.down()),
        Key([super], "j", lazy.layout.up()),
        Key([super], "l", lazy.layout.right()),
        # Move windows posation in current stack
        Key([super, "Shift"], "h", lazy.layout.shuffle_left()),
        Key([super, "Shift"], "k", lazy.layout.shuffle_down()),
        Key([super, "Shift"], "j", lazy.layout.shuffle_up()),
        Key([super, "Shift"], "l", lazy.layout.shuffle_right()),
        # Flib windows tile desing
        Key([super, alt], "j", lazy.layout.flip_down()),
        Key([super, alt], "k", lazy.layout.flip_up()),
        Key([super, alt], "h", lazy.layout.flip_left()),
        Key([super, alt], "l", lazy.layout.flip_right()),
        # Switch window focus to other pane(s) of stack
        Key([alt], "Tab", lazy.layout.next()),
        Key([alt, "Shift"], "Tab", lazy.layout.previous()),
        # Swap panes of split stack
        Key([super, "Shift"], "Space", lazy.layout.rotate()),
        # Switch Window Mode to Normalize
        Key([super, "Shift"], "n", lazy.layout.normalize()),
        # Switch window Mode to FullScreen
        Key([super, "Shift"], "f", lazy.window.toggle_fullscreen()),
        # Switch between tiling mode and floating mode
        Key([super, "Shift"], "t", lazy.window.toggle_floating()),
        # resize fcuse window
        Key([super, "control"], "g", lazy.layout.grow()),
        Key([super, "control"], "s", lazy.layout.shrink()),
        Key([super, "control"], "j", resize_down()),
        Key([super, "control"], "k", resize_up()),
        Key([super, "control"], "h", resize_left()),
        Key([super, "control"], "l", resize_right()),
        # Toggle between different layouts as defined below
        Key([super], "Tab", lazy.next_layout()),
        # Switch KeyBoard language
        Key([super], "Space", lazy.widget["keyboardlayout"].next_keyboard()),
        # Volume Controle
        Key([], "XF86AudioLowerVolume", lazy.spawn(f"{volume_controller} -d 5")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn(f"{volume_controller} -u 5")),
        Key([], "XF86AudioMute", lazy.spawn(f"{volume_controller} -t")),
        # Compositor Toggle (X11)
        Key([super, "Shift"], "c", lazy.spawn(toggle_compositor)),
        # Help Menu
        Key([], "F1", lazy.spawn(help_menu)),
        # Kill focused window
        Key([super, "Shift"], "w", lazy.window.kill()),
        # Restart Qtile
        Key([super, "control"], "r", lazy.reload_config()),
        # Shutdown Qtile
        Key([super, "control"], "q", lazy.shutdown()),
    ]
    return keys
