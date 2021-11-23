init offset = -1

## 【 STYLES 】 ░▒▓████████████████████████████████████■
style default:
    properties gui.text_properties()
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
style gui_text:
    properties gui.text_properties("interface")
style button:
    properties gui.button_properties("button")
style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
style prompt_text is gui_text:
    properties gui.text_properties("prompt")
style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
style frame:
    padding gui.frame_borders.padding
    background Frame("gui/guimg/frame.png", gui.frame_borders, tile=gui.frame_tile)

## 【 SAY SCREEN 】 ░▒▓████████████████████████████████████■
screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    if not renpy.variant("small"): ## If there's a side image, display it above the text.
        add SideImage() xalign 0.0 yalign 1.0

init python: #namebox available for styling through the Character object.
    config.character_id_prefixes.append('namebox')

style window is default
style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/guimg/textbox.png", xalign=0.5, yalign=1.0)
style say_label is default
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
style say_dialogue is default
style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
style say_thought is say_dialogue

style namebox is default
style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/guimg/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
style namebox_label is say_label

## 【 TEXT INPUT SCREEN 】 ░▒▓████████████████████████████████████■
screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"
style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

## 【 CHOICES SCREEN 】 ░▒▓████████████████████████████████████■
screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action

define config.narrator_menu = True ## true = menu captions spoken by the narrator. false = menu captions displayed as empty buttons.

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5
    spacing gui.choice_spacing
style choice_button is default:
    properties gui.button_properties("choice_button")
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## 【 QUICK MENU 】 ░▒▓████████████████████████████████████■
screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            textbutton _("BACK") action Rollback()
            textbutton _("HISTORY") action ShowMenu('history')
            textbutton _("SKIP") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("AUTO") action Preference("auto-forward", "toggle")
            textbutton _("SAVE") action ShowMenu('save')
            textbutton _("Q.SAVE") action QuickSave()
            textbutton _("Q.LOAD") action QuickLoad()
            textbutton _("OPTIONS") action ShowMenu('options')
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True
style quick_button is default
style quick_button_text is button_text
style quick_button:
    properties gui.button_properties("quick_button")
style quick_button_text:
    properties gui.button_text_properties("quick_button")

## 【 MENU SCREENS 】 ░▒▓████████████████████████████████████■
screen navigation():
    vbox:
        style_prefix "navigation"
        if main_menu:
            xalign 0.5
            yalign 0.65
        else:
            xoffset 10
        yalign 0.5
        spacing gui.navigation_spacing
        if main_menu:
            textbutton _("NEW GAME") action Start()
        else:
            textbutton _("MAIN MENU") action MainMenu()
            textbutton _("HISTORY") action ShowMenu("history")
            textbutton _("SAVE GAME") action ShowMenu("save")
        textbutton _("LOAD GAME") action ShowMenu("load")
        textbutton _("SETTINGS") action ShowMenu("options")
        textbutton _("QUIT") action Quit()
        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    outlines [ (absolute(3), "#000000", absolute(0), absolute (0)) ]

## 【 MAIN MENU SCREEN 】 ░▒▓████████████████████████████████████■

screen main_menu():
    tag menu
    add gui.main_menu_background
    frame:
        style "main_menu_frame"
    use navigation
    if gui.show_name:
        vbox:
            style "main_menu_vbox"
            text "[config.name!t]":
                style "main_menu_title"
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_frame:
    xsize 280
    yfill True
style main_menu_title:
    properties gui.text_properties("title")
style main_menu_vbox:
    xalign .5
    xoffset 0
    xmaximum 800
    yalign 0.0
    yoffset 20
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

## 【 GAME MENU SCREEN 】 ░▒▓████████████████████████████████████■
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    frame:
        style "game_menu_outer_frame"
        hbox: ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude
    use navigation
    label title
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    background "gui/overlay/game_menu.png"
style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10
style game_menu_viewport:
    xsize 920
style game_menu_vscrollbar:
    unscrollable gui.unscrollable
style game_menu_side:
    spacing 10
style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

## 【 LOAD / SAVE SCREEN 】 ░▒▓████████████████████████████████████■
screen save():
    tag menu
    use file_slots(_(" "))

screen load():
    tag menu
    use file_slots(_(" "))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_(""), auto=_("AUTOSAVES"), quick=_("QUICK SAVES"))

    use game_menu(title):
        fixed:
            order_reverse True
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")
                for page in range(1, 8):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3
style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")
style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
style slot_button_text:
    properties gui.button_text_properties("slot_button")


## 【 PREFERENCES SCREEN 】 ░▒▓████████████████████████████████████■
screen options():
    tag menu
    use game_menu(_(" "), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                vbox:
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")
                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
style pref_label is text:
    size 1000
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2
style pref_label_text is notify_text
style pref_label_text:
    yalign 1.0

style pref_vbox is vbox
style pref_vbox:
    xsize 225

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
style radio_button_text is gui_button_text
style radio_button_text:
    properties gui.button_text_properties("radio_button")
style radio_vbox is pref_vbox
style radio_vbox:
    spacing gui.pref_button_spacing

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style check_button_text is gui_button_text
style check_button_text:
    properties gui.button_text_properties("check_button")
style check_vbox is pref_vbox
style check_vbox:
    spacing gui.pref_button_spacing

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_slider:
    xsize 350
style slider_button is gui_button
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10
style slider_button_text is gui_button_text
style slider_button_text:
    properties gui.button_text_properties("slider_button")
style slider_pref_vbox is pref_vbox
style slider_vbox:
    xsize 450

style mute_all_button is check_button
style mute_all_button_text is check_button_text

## 【 HISTORY SCREEN 】 ░▒▓████████████████████████████████████■
screen history():
    tag menu
    predict False
    use game_menu(_(""), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"
        for h in _history_list:
            window: ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
        if not _history_list:
            label _("The dialogue history is empty.")

define gui.history_allow_tags = { "alt", "noalt" } ## what tags are allowed to be displayed on the history screen
style history_window is empty
style history_window:
    xfill True
    ysize gui.history_height
style history_name is gui_label
style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
style history_name_text is gui_label_text
style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
style history_text is gui_text
style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
style history_label is gui_label
style history_label:
    xfill True
style history_label_text is gui_label_text
style history_label_text:
    xalign 0.5

## 【 YES/NO QUESTIONS CONFIRM SCREEN 】 ░▒▓████████████████████████████████████■
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
    key "game_menu" action no_action ## right click + escape answer "no"
style confirm_frame is gui_frame
style confirm_frame:
    background Frame([ "gui/guimg/confirm_frame.png", "gui/guimg/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
style confirm_button is gui_medium_button
style confirm_button:
    properties gui.button_properties("confirm_button")
style confirm_button_text is gui_medium_button_text
style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

## 【 SKIP INDICATOR SCREEN 】 ░▒▓████████████████████████████████████■
## Displayed to indicate that skipping is in progress. https://www.renpy.org/doc/html/screen_special.html#skip-indicator
screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 6
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"
transform delayed_blink(delay, cycle): ##is used to blink arrows one after another
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat
style skip_triangle is skip_text
style skip_triangle: ## font has 2 have triangle
    font "DejaVuSans.ttf"
style skip_frame is empty
style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/guimg/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding
style skip_text is gui_text
style skip_text:
    size gui.notify_text_size

## 【 NOTIFY SCREEN 】 ░▒▓████████████████████████████████████■
## The notify screen is used to show the player a message. (For example, when the game is quicksaved or a screenshot has been taken.) https://www.renpy.org/doc/html/screen_special.html#notify-screen
screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"
    timer 3.25 action Hide('notify')
transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
style notify_text is gui_text
style notify_text:
    properties gui.text_properties("notify")
style notify_frame is empty
style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/guimg/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
