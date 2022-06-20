# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os

# from libqtile import qtile
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "kitty"  # guess_terminal()
browser = "firefox"

# Kanagawa Normal
"""
colors = {
    0: "#090618",
    1: "#C34043",
    2: "#76946A",
    3: "#C0A36E",
    4: "#7E9CD8",
    5: "#957FB8",
    6: "#6A9589",
    7: "#C8C093",
    8: "#1F1F28" ,#background
    9: "#DCD7BA" ,#foreground
}
"""

# Pywal Colors

colors = []
cache = "/home/jem/.cache/wal/colors"


def load_colors(cache):
    with open(cache, "r") as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append("#ffffff")
    lazy.reload()


load_colors(cache)

# Key Bindings

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right",),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    # Toggle between different layouts as defined below
    #Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(["mod1"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    #Key(["control"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Key([mod], "r", lazy.spawncmd("dmenu_run -p 'Run: '"), desc="Run Lanucher"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
                background=colors[7],#"#15181a",
                foreground=colors[3],
                selected_background=colors[1],
                selected_foreground=colors[4],
            )
        ), 
    ),
]
# Groups

groups = []

group_names = ["1", "2", "3", "4", "5"]

# Nerd Fonts

# nf-fa-firefox
# nf-oct-code
# NF-MDI-settings
# nf-mdi-file_document
# nf-mdi-visualstudio

# Right Bar

# nf-fa-clock_o
# nf-mdi-keyboard


# group_labes = ["web", "dev", "sys", "doc", code]
group_labels = ["", "", "漣", "", "﬏"]

group_layouts = ["colums", "monadtall", "columns", "monadtall", "monadtall"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            # Change Workspaces
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            #Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
            #Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name), lazy.group[i.name].toscreen(),),
        ]
    )

# Define layout_theme
layout_theme = {
    "margin": 10,
    "border_normal": colors[5],
    "border_focus": colors[1],
    "border_width": 3,
}
# margin : 20, border_width: 5,
layouts = [
    # layout.Columns(margin=5, border_normal=colors[5], border_focus=colors[1], border_focus_stack=[colors[2], colors[4]], border_width=3),
    layout.Columns(**layout_theme),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(**layout_theme, num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Fira Code Regular Nerd Font Complete",  # "Hack Regular Nerd Font Complete",
    fontsize=20,
    padding=10,
)
extension_defaults = widget_defaults.copy()


def init_widget_list():
    widgets_list = [
        widget.Image(
            filename="~/.config/qtile/icons/python-white.png",
            scale="False",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal)},
        ),
        widget.GroupBox(  # active="#00000000",
            inactive="#747474",
            highlight_method="block",
            highlight_color = colors[1],
            this_current_screen_border=colors[1],
            this_screen_border=colors[3],
            other_current_screen_border = colors[1],
            other_screen_border = colors[3],

        ),
        widget.Chord(
            chords_colors={
                "launch": (colors[1], colors[3]),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.WindowName(foreground=colors[5]),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=colors[2],
            background="#00000000",
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[8],
            background=colors[2],
            padding=0,
            scale=0.9,
        ),
        widget.CurrentLayout(foreground=colors[8], background=colors[2]),
        widget.Systray(),
        # widget.StatusNotifier(),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=colors[4],
            background=colors[2],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=colors[2],
            background=colors[4],
        ),
        widget.KeyboardLayout(
            foreground=colors[8], background=colors[4], fmt="Keyboard: {}", padding=5
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=colors[1],
            background=colors[4],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=colors[2],
            background=colors[1],
        ),
        widget.Clock(
            format="%Y-%m-%d %a %I:%M %p",
            foreground=colors[8],
            background=colors[1],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=colors[1],
            background="#00000000",
        ),
        widget.Spacer(length=3, background="#00000000"),
    ]

    return widgets_list


def init_widget_screen():
    widget_screen = init_widget_list()
    return widget_screen


def init_screens():
   return [Screen(top=bar.Bar(init_widget_screen(), size=24, opacity=0.8))]


screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
