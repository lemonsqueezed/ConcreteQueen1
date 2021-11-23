## 【 BASICS 】 ░▒▓████████████████████████████████████■
define config.name = _("CONCRETE QUEEN!")
define gui.show_name = True
define build.name = "CONCRETEQUEEN"


## 【 SOUNDS + MUSIC 】 ░▒▓████████████████████████████████████■
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
# define config.main_menu_music = "main-menu-theme.ogg"


## 【 TRANSITIONS 】 ░▒▓████████████████████████████████████■
## entering/exiting the game menu
define config.enter_transition = Dissolve(.3)
define config.exit_transition = Dissolve(.3)
## b/w screens of the game menu
define config.intra_transition = Dissolve(.5)
## after a game has been loaded
define config.after_load_transition = Dissolve(.5)
## entering the main menu after the game has ended
define config.end_game_transition = Dissolve(1)

## 【 WINDOW MANAGEMENT 】 ░▒▓████████████████████████████████████■
## This controls when the dialogue window is displayed. If "show", it is always displayed. If "hide", it is only displayed when dialogue is present. If "auto", the window is hidden before scene statements and shown again once dialogue is displayed.
## After the game has started, this can be changed with the "window show", "window hide", and "window auto" statements.

define config.window = "hide"

## Transitions used to show and hide the dialogue window
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## 【 PREFERENCE DEFAULTS 】 ░▒▓████████████████████████████████████■
## text speed (0=instant, 30=fast)
default preferences.text_cps = 30
## default auto-forward delay (0-30, 30 = slower)
default preferences.afm_time = 5

define config.save_directory = "CONKQUEEN-1636547255"


## 【 TASKBAR ICON 】 ░▒▓████████████████████████████████████■
define config.window_icon = "gui/guimg/window_icon.png"

## 【 BUILD/DISTRIBUTION CONFIG 】 ░▒▓████████████████████████████████████■

init python:
    ## The following functions take file patterns. File patterns are case-insensitive, and matched against the path relative to the base directory, with and without a leading /. If multiple patterns match, the first is used.
    ## In a pattern: / is the directory separator. * matches all characters, except the directory separator. ** matches all characters, including the directory separator.
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.
    # build.classify('game/**.png', 'archive') , build.classify('game/**.jpg', 'archive')
    ## Files matching documentation patterns are duplicated in a mac app build, so they appear in both the app and the zip file.
    build.documentation('*.html')
    build.documentation('*.txt')
