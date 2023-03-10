#  qtile built-in libraries
import subprocess

from libqtile import bar, hook
from libqtile.config import Screen

# Config files and other libraries
from cfg.bindings import init_app_run, init_keys
from cfg.groups import init_group_mappings, init_groups
from cfg.layouts import init_layouts
from cfg.widgets import init_widgets
from colors.dracula import Dracula


# Set up the hooks
@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(["picom -b"])
    subprocess.Popen(["feh --bg-max --randomize ~/.config/qtile/wallpapers/*"])


# Define the bar
def init_bar():
    return bar.Bar(
        widgets,
        24,
        opacity=0.66,
    )


# Set the Vars objects
keys = init_keys()
apps = init_app_run()
keys.extend(apps)
widgets = init_widgets()
layouts = init_layouts()
groups = init_groups()
group_mappings = init_group_mappings()

# Set your default widget styles
colors = Dracula()
widget_defaults = dict(
    font="Fira Code Nerd Font",
    fontsize=12,
    fontshadow=None,
)

# Merge the theme dictionary with the widget_defaults dictionary
widget_defaults.update(colors)

# Set up the screens
screens = [Screen(top=init_bar())]
