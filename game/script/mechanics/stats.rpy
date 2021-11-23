## FASHION
label fashion_increase:
    $ fashion += 1
    "You gained a point in fashion!"
    return
label fashion_decrease:
    $ fashion -= 1
    "You lost a point in fashion!"
    return

## VOGUE
label vogue_increase:
    $ vogue += 1
    "You gained a point in vogue!"
    return
label vogue_decrease:
    $ vogue -= 1
    "You lost a point in vogue!"
    return

## SIREN
label siren_increase:
    $ siren += 1
    "You gained a point in siren!"
    return
label siren_decrease:
    $ siren -= 1
    "You lost a point in siren!"
    return

## MONEY
label money_increase:
    $ money += 1
    "You earned some money! Get that bag!"
    return
label money_decrease:
    $ money -= 1
    "You lost some money!"
    return

## TAKE ME TO STATS
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "images/stats/stats_idle.png"
        hover "images/stats/stats_hover.png"
        action ShowMenu("StatsUI")

## STATS SCREEN
screen StatsUI:
    add "images/stats/statsbg.jpg"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        hbox:
            spacing 40
            # STAT NAMES
            vbox:
                spacing 10
                text "Fashion" size 30
                text "Vogue" size 30
                text "Siren" size 30
                text "Money" size 30

            # VALUES
            vbox:
                spacing 10
                text "[fashion]" size 30
                text "[vogue]" size 30
                text "[siren]" size 30
                text "[money]" size 30

    ## RETURN BUTTON
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "images/stats/return_%s.png"
        action Return()
