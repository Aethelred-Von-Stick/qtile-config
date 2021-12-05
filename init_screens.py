from libqtile import bar, widget
from libqtile.config import Screen

def set_font():
    return 'mononoki nerd Font'

#def color(cstring):
#    color_names = ['r','b','g','c','m','y']

def dracula(cstring):
    color_dict = {
        'purple': '#9580ff',
        'green': '#8aff80',
        'pink': '#ff80bf',
        'yellow': '#ffff80',
        'orange': '#ff9580',
        'cyan': '#8be9fd',
        'dkblue': '#6272a4',
        'red': '#ff5555',
        'black': '#282a36',
        'white': '#f8f8f2',
    }
    return color_dict[cstring]

def screen_config():
	return [
	    Screen(
            top=bar.Bar([
                widget.GroupBox(
                    background = dracula('purple'),
                    font = set_font(),
                    active = dracula('green'),
                    inactive = dracula('dkblue'),
                    ),
                widget.TextBox(
                    text = "",
                    foreground = dracula('purple'),
                    padding = 0,
                    background = dracula('green'),
                    fontsize = 29,
                    ),
                widget.CapsNumLockIndicator(
                    background = dracula('green'),
                    foreground = dracula('dkblue'),
                    ),
                widget.TextBox(
                    text = "",
                    background = dracula('dkblue'),
                    padding = 0,
                    foreground = dracula('green'),
                    fontsize = 29,
                    ),               widget.Spacer(),
                widget.TextBox(
                    text = "",
                    fontsize = 29,
                    padding = 0,
                    foreground = dracula('purple'),
                    ),
                widget.WindowName(
                    font = set_font(),
                    foreground = dracula('green'),
                    background = dracula('purple'),    
                    max_chars = 68,
                    padding = 0,
                    ),
                 widget.TextBox(
                    text = "",
                    fontsize=29,
                    padding = 0,
                    foreground = dracula('purple'),
                    ),
                widget.Spacer(),
                widget.CheckUpdates(
                    font = set_font(),
                    color_have_updates = dracula('green'),
                    color_no_updates = dracula('orange'),
                    distro = 'Arch',
                    ),
               widget.Net(
                    font = set_font(),
                    background = dracula('yellow'),
                    foreground = dracula('dkblue'),
                    format = '{down}↓↑ {up}',
                    ),
		        widget.TextBox(
                    text = "Vol:",
                    font = set_font(),
                    background = dracula('orange'),
                    ),
		        widget.Volume(
                    font = set_font(),
                    background = dracula('orange'),
                    ),
		        widget.TextBox(
                    text = "Batt:",
                    font = set_font(),
                    background = dracula('pink'),
                    ),
		        widget.Battery(
                    font = set_font(),
                    format="{percent:2.0%}",
                    background = dracula('pink'),
                    ),
		        widget.Clock(
                    font = set_font(),
                    format='%a %d %b %H:%M',
                    background = dracula('cyan'),
                    foreground = dracula('dkblue'),
                    ),
		        widget.QuickExit(
                    font = 'DejaVu Sans',
                    fontsize = '20',
                    foreground = dracula('green'),
                    background = dracula('red'),
                    countdown_format = ' {} ',
                    default_text = ' ⏻ ',
                    ),
                ], 
                30,
                background = dracula('dkblue'),     #"#1f003a"
            ),         
        ),
        Screen(
            top=bar.Bar([
                widget.GroupBox(
                    font = set_font(),
                    background = dracula('purple'),
                    active = dracula('green'),
                    inactive = dracula('dkblue'),    
                    ),
                  widget.TextBox(
                    text = "",
                    fontsize=29,
                    padding = 0,
                    foreground = dracula('purple'),
                    ),
                widget.Spacer(),
                widget.TextBox(
                    text = "",
                    fontsize = 29,
                    padding = 0,
                    foreground = dracula('purple'),
                    ),
                widget.WindowName(
                    font = set_font(),
                    foreground = dracula('green'),
                    background = dracula('purple'),    
                    max_chars = 68,
                    padding = 0,
                    ),
                 widget.TextBox(
                    text = "",
                    fontsize=29,
                    padding = 0,
                    foreground = dracula('purple'),
                    ),
                widget.Spacer(),
		        widget.Clock(
                    font = set_font(),
                    format='%a %d %b %H:%M',
                    background=dracula('cyan'),
                    foreground=dracula('dkblue'),
                    ),
			    widget.QuickExit(
                    font = 'DejaVu Sans',
                    fontsize = '20',
                    foreground = dracula('green'),
                    background = dracula('red'),
                    countdown_format = ' {} ',
                    default_text = ' ⏻ ',
                    ),
               ], 
                30, 
                background=dracula('dkblue')     #"#1f003a"
                ),
            )   
        ]    

def fake():
	return [
	Screen(
      		bottom=bar.Bar(
         	 [
             		 widget.Prompt(),
             		 widget.Sep(),
                         widget.WindowName(),
                         widget.Sep(),
        	         widget.Systray(),
                         widget.Sep(),
                         widget.Clock(format='%H:%M:%S %d.%m.%Y')
                 ],
                  24,
          background="#555555"
            ),
      x=0,
      y=0,
      width=600,
      height=480
 ),
  	Screen(
     		 top=bar.Bar(
         	 [
             		 widget.GroupBox(),
              		 widget.WindowName(),
             		 widget.Clock()
           ],
          30,
      ),
      x=600,
      y=0,
      width=300,
      height=580
  ),
  Screen(
      top=bar.Bar(
          [
              widget.GroupBox(),
              widget.WindowName(),
              widget.Clock()
          ],
          30,
      ),
      x=0,
      y=480,
      width=500,
      height=400
  ),
  Screen(
      top=bar.Bar(
          [
              widget.GroupBox(),
              widget.WindowName(),
              widget.Clock()
          ],
          30,
      ),
      x=500,
      y=580,
      width=400,
      height=400
  ),
]
