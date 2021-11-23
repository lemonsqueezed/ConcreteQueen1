init offset = -2
init python:
    gui.init(1280, 720)

## 【 UI TEXT 】 ░▒▓████████████████████████████████████■
define gui.text_font = "/images/misc assets/ARIAL.TTF"
define gui.text_color = u'#ffffff'
define gui.text_size = 22
## Character Name
define gui.name_xpos = 200
define gui.name_ypos = -30
define gui.name_xalign = 0.0
## Character NameBox
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False
# Dialogue Box
define gui.textbox_height = 170
define gui.textbox_yalign = 1.0
# Dialogue
define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 30
define gui.dialogue_width = 744
define gui.dialogue_text_xalign = 0.0

# Menu Choice
define gui.interface_text_font = "/images/misc assets/ARIAL.TTF"
define gui.interface_text_color = u'#ffffff'
define gui.interface_text_size = 40
# Accent Color
define gui.accent_color = u'#9933ff'
# Small Text
define gui.idle_small_color = u'#aaaaaa'

# Button Color
define gui.idle_color = u'#fa009f'
define gui.hover_color = u'#97dbf7'
# Current Screen Button (selected, not focused)
define gui.selected_color = u'#ffffff'
# Unselectable (not unlocked yet)
define gui.insensitive_color = u'#8888887f'

# Colors used for the portions of bars that are not filled in
define gui.muted_color = u'#3d1466'
define gui.hover_muted_color = u'#5b1e99'

# Misc.
define gui.label_text_size = 15
define gui.name_text_font = "/images/misc assets/ARIAL.TTF"
define gui.name_text_size = 30
define gui.notify_text_size = 16
## Game Title
define gui.title_text_size = 100
define gui.title_text_font ="/images/misc assets/cheri.regular copy.ttf"
define gui.title_text_xalign = .5
define gui.title_text_yalign = .2
define gui.title_text_outlines = [ (absolute(5), "#000000", absolute(0), absolute (0)) ]


## 【 MENUS 】 ░▒▓████████████████████████████████████■
## Main
define gui.main_menu_background = "gui/guimg/main_menu.png"
define gui.main_menu_text_xalign = 0
define gui.main_menu_text_yalign = 0


## Game
define gui.game_menu_background = "gui/guimg/game_menu.png"
## Button Spacing
define gui.navigation_spacing = 4
define gui.navigation_xpos = 40

## 【 BUTTONS 】 ░▒▓████████████████████████████████████■
## Sizing
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(4, 4, 4, 4)
## Text
define gui.button_text_xalign = 0.0
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
## True, = tiled. False = linearly scaled.
define gui.button_tile = False
## Color
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Choice Buttons #######################################
define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"
define gui.choice_spacing = 20
# Quick Buttons
define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color
## Misc Variations
define gui.radio_button_borders = Borders(18, 4, 4, 4)
define gui.check_button_borders = Borders(18, 4, 4, 4)

## 【 FILE PAGE 】 ░▒▓████████████████████████████████████■
## Save Slot
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color
## Save Thumbnails
define config.thumbnail_width = 266
define config.thumbnail_height = 154
## Number Columns / Rows
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2
## Page Buttons
define gui.page_button_borders = Borders(10, 4, 10, 4)
define gui.page_spacing = 0
## Space B/W file slots
define gui.slot_spacing = 20

## 【 POSITIONING/SPACING 】 ░▒▓████████████████████████████████████■
## B/W preferences
define gui.pref_spacing = 10
## B/W preference buttons
define gui.pref_button_spacing = 0

## 【 FRAMES 】 ░▒▓████████████████████████████████████■
## Generic
define gui.frame_borders = Borders(4, 4, 4, 4)
## Confirm Screen
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)
define gui.confirm_button_text_xalign = 0.5
## Skip Screen
define gui.skip_ypos = 10
define gui.skip_frame_borders = Borders(16, 5, 50, 5)
## Notify Screen
define gui.notify_ypos = 45
define gui.notify_frame_borders = Borders(16, 5, 40, 5)
## Tile Frame Backgrounds?
define gui.frame_tile = False

## 【 BARS / SCROLLBARS / SLIDERS 】 ░▒▓████████████████████████████████████■
## Display Unscrollable Bars?
define gui.unscrollable = "hide"
## Size of horizontal bars, scrollbars, and sliders
define gui.bar_size = 25
define gui.scrollbar_size = 12
define gui.slider_size = 25
## True = Tiled Bar Images // False = linearly scaled
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False
# Horizontal Borders
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)
# Vertical Borders
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## 【 HISTORY 】 ░▒▓████████████████████████████████████■
## Stored Number Blocks of Dialogue History
define config.history_length = 250
## Height of a history screen entry, None = Variable (slower performance)
define gui.history_height = 140
## Speaking Character Label
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0
## Dialogue Text
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0
