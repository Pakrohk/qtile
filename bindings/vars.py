import os

# Set the varible keys
super = "mod4"
alt = "mod1"
print_screen = "Print"


# set the varible locations
home = os.path.expanduser("~")
app_menu = f"{home}/.config/qtile/scripts/rofi/dmenu_drun"
shell_menu = f"{home}/.config/qtile/scripts/rofi/dmenu_run"
win_selector = f"{home}/.config/qtile/scripts/rofi/dmenu_window"
screenshot = f"{home}/.config/qtile/scripts/screenshot"
volume_controller = f"{home}/.config/qtile/scripts/volume_controller"
scaling_menu = f"{home}/.config/qtile/scripts/scaling_menu"
toggle_compositor = f"{home}/.config/qtile/scripts/toggle_compositor"
power_menu = f"{home}/.config/qtile/scripts/power_menu"

# set the varible apps
term = "alacritty"
browser = "firefox"
file_manager = "pcmanfm-qt"
qt5_config = "qt5ct"
