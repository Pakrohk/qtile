# python libraries
import os
import subprocess

#  qtile built-in libraries
from libqtile import bar, hook, qtile
from libqtile.config import Screen

# import bindings Modules
from bindings.apps import init_apps_run
from bindings.cores import init_keys
from bindings.groups import init_groups_keys
from bindings.mouse import init_mouse_keys
# import groups configs
from groups.creator import init_name_creator
from groups.rules import init_app_rules
# import layouts config
from layouts.settings import init_layouts
# import themes and colors
from themes.dracula import Dracula
# import widgets configs
from widgets.top import init_widgets


# Set up the hooks
@hook.subscribe.startup_once
def autostart():
    # Notification daemon
    subprocess.Popen("dunst")

    # Compositor (Wayland-native apps don't need picom)
    # picom is X11-only. For Wayland, the compositor is built into Qtile.
    if qtile.core.name == "x11":
        subprocess.Popen(["picom", "-b"])

    # Clipboard manager
    # greenclip is X11-only. cliphist is a good Wayland alternative.
    if qtile.core.name == "wayland":
        subprocess.Popen(["wl-paste", "--type", "text", "--watch", "cliphist", "store"])
        subprocess.Popen(["wl-paste", "--type", "image", "--watch", "cliphist", "store"])
    else:
        subprocess.Popen(["greenclip", "daemon"])

    os.environ["QT_QPA_PLATFORMTHEME"] = "qt5ct"
    subprocess.Popen("lxqt-policykit-agent")
    subprocess.Popen("nm-applet")


# Set your default widget styles
colors = Dracula()
widgets_themes = dict(
    font="FantasqueSansMono Nerd Font Mono",
    fontsize=18,
)

# Merge the theme dictionary with the widgets_themes dictionary
widgets_themes.update(colors)

layoutConfig = dict(
    margin=[5, 2, 2, 5],
    border_width=2,
    border_focus=colors["pink"],
    border_normal=colors["cyan"],
)

# Set the Vars objects
keys = init_keys()
mouse = init_mouse_keys()
apps = init_apps_run()
keys.extend(apps)
layouts = init_layouts(layoutConfig)
groups = init_name_creator()
groups_bind = init_groups_keys()
keys.extend(groups_bind)
group_mappings = init_app_rules()

# Define the bar
def init_bar():
    return bar.Bar(
        init_widgets(widgets_themes),
        24,
        opacity=0.66,
        background=colors["background"],
        border_width=0,  # remove the default border
        margin=[0, 5, 5, 10],  # add some margin
    )


# Set up the screens
screens = [
    Screen(
        top=init_bar(),
        wallpaper="~/.config/qtile/wallpapers/dracula_qtile.png",
        wallpaper_mode="stretch",
    ),
    Screen(
        bottom=init_bar(),
        wallpaper="~/.config/qtile/wallpapers/dracula_qtile.png",
        wallpaper_mode="stretch",
    ),
]

focus_on_window_activation = "smart"
drag = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
wmname = "qtile"
