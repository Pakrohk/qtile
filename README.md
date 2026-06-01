# Modernized Dracula for [Qtile](https://qtile.org/)
 > A modernized, Wayland-ready dark theme and configuration for [Qtile](https://qtile.org/)
 
 ![Qtile dracula](https://github.com/dracula/qtile/assets/87908673/ac5630c5-554a-41e5-a2aa-03f807995693)

 This configuration has been modernized to support both **Wayland** and **X11** sessions seamlessly.

 ## Key Modernizations
 - **Wayland Native**: Optimized for Wayland while maintaining X11 compatibility.
 - **Dynamic Tool Selection**: Automatically chooses between `grim`/`slurp` (Wayland) and `maim` (X11) for screenshots.
 - **Modern Clipboard**: Uses `cliphist` and `wl-copy` for Wayland clipboard management.
 - **Enhanced Stability**: Updated to use the latest Qtile APIs (e.g., `StatusNotifier` instead of `Systray` on Wayland).
 - **Robust Scripts**: Improved error handling and feature parity across backends.
 - **Visual Polish**: Achieves a spacious, "spectrwm"-like feel with optimized margins and bar dimensions.
 - **Dynamic Scaling**: On-the-fly DPI (X11) and Scaling (Wayland) adjustments via the bar.
 - **Integrated Power Management**: Convenient menu for Lock, Sleep, Reboot, and Shutdown.
 - **Interactive Help**: Quick access to all keybindings via the F1 menu.

 ## Requirements 
 To properly run this qtile configuration, please install the following dependencies:

 ### General
   - `network-manager-applet` (for WiFi management: `nm-applet`)
   - `dunst` (notification daemon)
   - `rofi` or `rofi-wayland` (app launcher)
   - `lxqt-policykit` (for polkit authentication)
   - `python-psutil` (for resource widgets)
   - `fantasque-sans-mono-nerd-font` (recommended font)

 ### Wayland Specific
   - `grim` & `slurp` (for screenshots)
   - `wl-clipboard` (clipboard utilities)
   - `cliphist` (clipboard history)
   - `wlr-randr` (for dynamic scaling)

 ### X11 Specific
   - `picom` (compositor)
   - `maim` & `xclip` (for screenshots and clipboard)
   - `rofi-greenclip` (clipboard history for X11)

 ### Optional but Recommended
   - `yad` (for professional Help menu)
   - `pulseaudio-utils` (provides `pactl` for unified volume control)

## Install
 ```
 git clone https://github.com/Pakrohk/qtile.git ~/.config/qtile
 ```

## Customization

### Config Files
You can customize the autostarted applications in the `config.py` file. It now includes logic to detect the backend and launch appropriate tools.

Additionally, other config files under `bindings/`, `groups/`, `layouts/`, and `widgets/` can be modified to tailor the experience.

## Maintenance Notes
- **Backend Detection**: The configuration uses `qtile.core.name` to detect if it's running under `wayland` or `x11`.
- **Bar Arguments**: Deprecated arguments like `floating` or `draw_shadow` have been removed from the Bar definition for compatibility with latest Qtile.
- **Layouts**: Custom BSP resize functions now use standard `grow_` methods for better stability.

## Team
#### Contributions

Contributions from the community are welcome!
Original contributors: [Pakrohk](https://github.com/Pakrohk), [nooob-developer](https://github.com/nooob-developer).

## License
[MIT License](https://github.com/qtile/qtile/blob/master/LICENSE)
