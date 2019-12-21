# pylint: skip-file

# Source autoconfig.yml
config.load_autoconfig()

#
# Theme
#
c.fonts.monospace = '"Fira Mono", Monospace'
bg = "#31363b"
c.colors.statusbar.normal.bg =\
    c.colors.statusbar.command.bg =\
    c.colors.tabs.selected.odd.bg =\
    c.colors.tabs.selected.even.bg =\
    c.colors.tabs.pinned.selected.odd.bg =\
    c.colors.tabs.pinned.selected.even.bg =\
    bg

c.scrolling.smooth = True
c.new_instance_open_target = 'window'
c.session.lazy_restore = True
c.content.autoplay = False
c.content.host_blocking.enabled = False

# Dark theme toggle
stylesheets = [
    '~/.config/qutebrowser/solarized-dark-all-sites.css',
    "''"
]
config.bind('tt', f"config-cycle content.user_stylesheets {' '.join(stylesheets)}")

# Think "m for media"
config.unbind('m')
config.unbind('M')
config.bind('mm', 'hint links spawn mpv {hint-url}')
config.bind('mcm', 'spawn mpv {url}')
config.bind('md', 'hint -r links spawn youtube-dl {hint-url} -o ~/Downloads/%(title)s')
config.bind('mcd', 'spawn youtube-dl {url} -o ~/Downloads/%(title)s')

config.bind('ab', 'bookmark-add')
config.bind('aB', 'bookmark-del')

# readline shortcuts
config.bind('<Ctrl-d>', 'fake-key <Delete>', 'insert')
config.bind('<Ctrl-a>', 'fake-key <Home>', 'insert')
config.bind('<Ctrl-e>', 'fake-key <End>', 'insert')
config.bind('<Ctrl-f>', 'fake-key <Right>', 'insert')
config.bind('<Ctrl-b>', 'fake-key <Left>', 'insert')
config.bind('<Ctrl-p>', 'fake-key <Up>', 'insert')
config.bind('<Ctrl-n>', 'fake-key <Down>', 'insert')
config.bind('<Ctrl-w>', 'fake-key <Ctrl-backspace>', 'insert')
config.bind('<Ctrl-k>', 'fake-key <Shift-End><Delete>', 'insert')
config.bind('<Ctrl-u>', 'fake-key <Shift-Home><Backspace>', 'insert')

# Think ";i for image"
config.unbind(';I')
config.unbind(';i')
config.bind(';ii', 'hint images')
config.bind(';iI', 'hint images tab')
config.bind(';id', 'hint images download')
config.bind(';iy', 'hint images yank')

