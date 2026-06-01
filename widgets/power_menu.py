from libqtile.widget import TextBox
from libqtile.lazy import lazy
from bindings.vars import power_menu

class PowerMenu(TextBox):
    def __init__(self, **config):
        super().__init__("⏻", **config)
        self.add_callbacks({"Button1": lazy.spawn(power_menu)})
