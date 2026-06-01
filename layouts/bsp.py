from libqtile.lazy import lazy


@lazy.function
def resize_left(qtile):
    layout = qtile.current_layout
    if hasattr(layout, "grow_left"):
        layout.grow_left()


@lazy.function
def resize_right(qtile):
    layout = qtile.current_layout
    if hasattr(layout, "grow_right"):
        layout.grow_right()


@lazy.function
def resize_up(qtile):
    layout = qtile.current_layout
    if hasattr(layout, "grow_up"):
        layout.grow_up()


@lazy.function
def resize_down(qtile):
    layout = qtile.current_layout
    if hasattr(layout, "grow_down"):
        layout.grow_down()
