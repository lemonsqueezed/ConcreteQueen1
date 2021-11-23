label competition:
    nar "You nervously tap your foot as you wait with the other contestants backstage"

    nar "You adjust your dress"

    nar "You want to make [momn] proud"

    nar "The judges are tallying up your points"
    nar "You were only one of about six contestants, one or two didn't show apparently?"
    nar "and you go through your performances, trying to predict how many points you could win."

    if dress <= 10:
        jump bad
    if dress >= 10 and dress <= 15:
        jump neutral
    if dress >= 15:
        jump good
    if dress == 0:
        jump comedian
