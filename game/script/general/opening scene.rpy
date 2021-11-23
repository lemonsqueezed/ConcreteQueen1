##STATS DEFAULT
default house = " "
default fashion = 1
default vogue = 1
default siren = 1
default money = 1
default mcn = None
## default mcn.total = mcn.fashion + vogue + siren
## default money = total * 100

label start:

show screen gameUI
play sound applause volume .8 fadein .5 fadeout .5
stop sound
nar "Sore legs. Nausea. Lightheaded. Tired."
nar "But you couldn't be happier"
scene bg blrm
with dissolve
play music masterblaster
## play people talking ambience
nar "You're pleasantly surprised everyone was so welcoming and nice to you as a beginner."
nar "You're glad you got it over and done with."
nar "It's only uphill from here, right?"
nar "You trust the process that it'll get easier with time, and feel proud of yourself you finally took the leap into the community."
nar "Everyone starts somewhere."
##pause
## people fading ambience
nar "The venue is clearing out. It's small and a bit claustrophobic, but honestly it adds to the vibe."
nar "You look down at your dress"
menu:
    "It's elegant and over the top. Gotta make a strong first impression.":
        $ fashion += 1
        nar "You're not too great on your feet so you hope this will help them overlook that."
        nar "If you wear a dress big and fancy enough, they can't even see you mess up any moves!"
    "It's something practical. You didn't want to overdo it for your first show. You're really honestly better at voguing than fashion.":
        $ vogue += 1
        nar "You question if you pulled a muscle or something with how hard you went on the stage. That's okay."
        nar "Limbs are replacable, legacy is forever. No pain, no gain."
    "You wore something fun. Clothes and voguing isn't everything. You know you're charming and can bet on it":
        $ siren += 1
        nar "You decided to just wing it and hope for the best. Kinda a first date look."
        nar "Be flexible, be formal, but also show enough of yourself. That's your philosophy on life."
        nar "You didn't take it too seriously."
        nar "You came to have fun and meet people, break out of your shell, and learn."

nar "You really overestimated yourself as a pang of lightheadedness hits you."
nar "Whatever. Post workout days feel the best anyway."
nar "Just gotta go to the locker, clean up and pick up your bag, and take the subway home--"

## MAKE ??? CHARACTER

"HEY YOU!"
mcn "Huh?!"
nar "You're a little startled and annoyed, wanting to go home more than anything"
nar "Did you do something wrong? Why didn't they bring it up earlier? This was a bad idea right- You should've stayed at home-"

show ven idle at left
with moveinleft

ven "Hey!"
mcn "Hi?"

show cup idle at center
with moveinright

show swa idle at right
with moveinright

cup "I hope it's okay if we sit and chat for a bit!"
menu:
    "Yes":
        mcn "Yeah what's up?"
    "Also yes but slightly less confidently":
        mcn "Uhhh yeah, am I in trouble or something?"
        ven "Oh sweatheart no!"
ven "I'm so sorry, let me introduce everyone..."
ven "I'm Venus Fly,"
ven "This is Swanna Song"
ven "and is Cupidia"

swa "We all absolutely LOVED your performance"
cup "What did you say your name was again, darling?"
cup "Sorry, It's all in one ear out the other with me, haha!"
ven "Yeah. It really is."
python:
    mcn = renpy.input("", length=20)
    mcn = mcn.strip()

    if not mcn:
        mcn = "Dolly"
mcn "My name is [mcn]!"

ven "And your full stage name is...?"

python:
    dqn = renpy.input("", length=20)
    dqn = dqn.strip()

    if not dqn:
        dqn = "Fresha Vacado"
cup "What a lovely name... [mcn] (also known as THE [dqn]) I can already see the Wikiapedia article!"

swa "Just a Wikipedia arcticle? Cupid, stop selling them short."
swa "*I* can already picture them on Times Square billboards and in newspaper headlines across the country, maybe even across the *world*!"
nar "Swanna gestures to you. You don't know whether to feel like a kind of lab animal, or to be honored by the way they're talking about you"

ven "Anyways, now to the reason we're here--"
ven "I don't think they mentioned you being a part of any house when they introduced you,"
ven "Is that right?"

## "STILL NEW TO ALL OF THIS"
menu:
    "That's right, I'm still new to all of this...":
        mcn "Yeah, embarassing I know. I'm still pretty new to all of this."
        ven "Hey, everyone starts somewhere!"
        ven "And I can see that it's one strong start, hun."
        nar "While you're certainly loving the attention, you start feeling a little anxious that you'll disappoint them."

    "I'm unsure about what I'm looking for in a house":
        mcn "I don't really know what I want in a house, there's a *lot* to choose from..."
        ven "Ah, well, we can give you a quick rundown of our houses if that's cool?"
        cup "We all thought you were STUNNING, and want to scout you"
        nar "Well...beggars can't be choosers..."
        nar "That sounds really mean-- you just meant, like, how could you possibly turn any of these queens down?!"
        nar "But you're a no name, even if you hated them how much of a choice is it, really? This is New York City."

    "Why? Are you that desperate for members?":
        mcn "Are you really so desperate for members you'd recruit some no-name?"
        cup "Not just *some* no-name, we only go for very *cute* no-names! You certainly fit that bill."
        swa "Oh please, just because we recognize talent--?!"
        nar "Venus shoves both of them out of the way."
        ven "Knock it off you two. you're scaring them"
        nar "You turn to look up at Venus and find her looking directly at you."
        nar "You didn't realize until now..."
        nar "...how much harder it is to be confident one-on-one."
        nar "You're kind of regretting the quip you made"
        ven "Jeez you're jaded. I can almost hear the rat that powers your brain running itself into a heart attack."
        nar "Venus turns to the other two queens, hands firmly on her hips."
        ven "See this is why *I* claim them; you snakes wouldn't know how to love them, unlike me!"
        nar "You feel yourself leaning back at on the stage at an uncomfortable angle. You adjust your collar a little..."
        nar "You're not used to the attention, especially not from people who are actually cool..."
        mcn "T-thanks?! I mean. Um. I'm not a child yaknow. I'm probably not much younger than you all, actually!"
        nar "Cupid giggles a bit."
        cup "Oh so NOW you drop the cocky attitude."
        nar "She does have a point."

swa "Can we please cut to the chase?"
swa "It's summer, you know! I'm burning up in my immaculate and elegant drip!"
nar "Swanna gestures dramatically to her thick velvet dress."
nar "She then gestures towards her shoes and lifts one foot back for emphasis. The heels look stacked high enough to go to heaven! Jeez!"
ven "Well it's certainly not *my* fault that SOMEBODY sacrifices erogenomics for shoes that are one step away from being a torture device..."
nar "Swanna gives Venus a glare before continuing"
swa "So, we want you to join one of our houses."
swa "Full transparency, we're all 'rival' houses..."
swa "...so we thought it would only be fair for you to get to hear us all out at once, rather than making it a race of who could get to you first."
mcn "Uhm, thank you?"
ven "So, anyway, which of our houses do you wanna join?"
"Choose wisely. And say it with your chest!"

## CHOOSING HOUSE
label choice:
menu:
    "House of Mirrors. Elegant, refined, and specializing in fashion. You KNOW everyone in this house got a walk-in closet and color-coordinated room. It's those kids who color-code and write in neat cursive...but grown up...and gay. Good house if you want to stress over your outfits more than usual and give up flexability, and therefore some of your voguing ability. At least you'll make a good trophy spouse!":
        $ fashion += 1
        $ house = "mirrors"
        $ momn = "Swanna Song"
        jump mirrorsroute
    "House of Frenzy. Venus Fly. Vogue-focused. Flashy and mobile. Good house if you're unafraid of twisting your ankles, and every other body part that it's possible to twist. Great house if you're the person who hogs the center of the dance floor at parties. Not the house for you if you're a avante garde fashion nut. Unless you're okay with all your outfits being teared at compromising seams when you do dips...":
        $ vogue += 1
        $ house = "frenzy"
        $ momn = "Venus"
        jump frenzyroute
    "House of Hearts. Cupidia's house. Siren-centered. You have a feeling everyone in this house has dated eachother at least once. Maybe this would be good for getting you out of your shell? Maybe you're not the best at fashion or vogue, but your charisma renders you a confidence imposter good enough to get away with shoplifting from the White House giftstore by claiming you're actually the president's second cousin.":
        $ siren += 1
        $ house = "hearts"
        $ momn = "Cupidia"
        jump heartsroute
return
