label good:
    "You jump up with joy as your point total flashes on the screen. You have the most points! You’re still in shock that you’ve won. Your friends and supporters squeeze you in a hug, holding you up and cheering."

label neutral:
    "You look up to see yourself in the middle of the ranks. You slightly smile to yourself, and pick up your head. Ready to continue for another day."

label bad:
    "Your heart sinks as you see your name in last place. Others are cheering as they see their name ranked higher and a larger cheer erupts on your left side from the contestant with the most points."

    nar "You try not to feel too down. You know you tried your best and that’s something to be proud of as well."
    nar "You hear the familiar click of heels as you sulk on a couch backstage. You dread what's coming next."
    if house = "frenzy":
        ven "eeee"
    if house = "mirrors":
        swa "eee"
    if house = "hearts":
        cup "eee"

    "[momn]"

label comedian:
    jud "BOLD CHOICE FOR AN OUTFIT [mcn]!!!"
    jud "You're"
