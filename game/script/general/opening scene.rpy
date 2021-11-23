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
ven "I'm so sorry, let me introduce ourselves..."
ven "I'm Venus Fly,"
ven "This is Swanna Song"
ven "and this...creature is Cupidia"

swa "We all LOVED your performance"
cup "What did you say your name was again, darling?~"
cup "Sorry, It's all in one ear out the other with me..."
ven "Yeah. it really is"
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

swa "Cupid stop selling them short."
swa "*I* can already picture them on billboards and headlines"
nar "Swanna gestures to you. You don't know whether to feel like a lab animal or honored by how they're talking about you"

ven "Anyways, the reason we're here-"
ven "I don't think they mentioned you being a part of any house when they introduced you"
ven "Am I mistaken?"

## "STILL NEW TO ALL OF THIS"
menu:
    "That's right, I'm still new to all of this...":
        mcn "Yeah, embarassing I know. I'm still really new to all of this."
        ven "That's cool, everyone starts somewhere."
        ven "And I can see you're already off to a strong start, hun."
        nar "Though you're eating this attention up, you feel a little anxious that you'll disappoint them."

    "I'm unsure about what I'm looking for in a house":
        mcn "I don't really know what I want in a house, there's a lot to choose from..."
        ven "Ah, well, we can give you a quick rundown of our houses if that's cool?"
        cup "We all thought you were STUNNING and want to scout you"
        nar "I mean...beggars can't be choosers..."
        nar "That sounds really mean. I just meant how could I turn these queens down."
        nar "I'm a no name, even if I hated them what choice do I got? This is New York City."

    "Why? Are you that desperate for members?":
        mcn "Oh are you THAT desperate for members you'd recruit a no-name?"
        cup "Nope! Just desperate for cuties like you~"
        swa "Oh please, just because we recognize talent--?!"
        nar "Venus shoves both of them out of the way."
        ven "Knock it off you two. you're scaring them"
        nar "You turn to look up at Venus and find her looking directly at you."
        nar "You didn't realize until now..."
        nar "...how hard it is to be confident one-on-one."
        nar "You regret the quip you made"
        ven "Jeez you're jaded. I can almost hear the little rat on a wheel in your brain working itself into a heart attack"
        nar "Venus turns to the other two queens, hands on hips firmly."
        ven "See this is why I claim them, you snakes don't know how to love them like I do!"
        nar "You feel yourself leaning back at an uncomfortable angle against the stage. You adjust your collar a little..."
        nar "You're not used to the attention, especially not from people who are actually cool..."
        mcn "T-thanks?! I mean. Um. I'm not a child yaknow. I'm probably not much younger than you actually!"
        nar "Cupid giggles a bit."
        cup "Oh NOW you drop the cocky attitude."
        nar "She does have a point."

swa "Can we cut to the chase?"
swa "It's summer yaknow and I'm burning up in this!"
nar "Swanna gestures dramatically to her leather outfit."
nar "She lifts up her legs to show her platform heels. They look like a weird combination between pirouette ballet shoes or whatever, and heels stacked high enough to go to heaven. Jeez."
ven "Not my fault SOMEBODY sacrifices erogenomics for shoes that are practically a torture device..."
nar "Swanna gives a glare at Venus before continuing"
swa "So, we want you to join one of our houses."
swa "Full transparency, we're all 'rival houses'"
swa "...so we thought it was only fair to you if you got to hear us out at once, rather than making it a race of who gets to you first."
mcn "Oh, thank you?"
ven "So anyways, which of our houses do you wanna join?"
"Choose wisely. And say it with your chest."

## CHOOSING HOUSE
label choice:
menu:
    "House of Mirrors. Elegant, prim, and specializes in fashion. You KNOW everyone in this house got a walk-in closet and color-coordinated room. It's those kids who color-code and write in neat cursive...but grown up...and gay. Good house if you want to stress over your outfits more than usual and give up the ability to vogue as well. At least you'll make a good trophy spouse.":
        $ fashion += 1
        $ house = "mirrors"
        $ momn = "Swanna Song"
        jump mirrorsroute
    "House of Frenzy. Venus Fly. Vogue-focused. Flashy and mobile. Good house if you're not scared of twisting your ankles. Great house if you're the person who hogs the center of the dance floor at parties. Not the house for you if you're a avante garde fashion nut. Unless you're okay with all your outfits being teared at compromising seams when you do dips...":
        $ vogue += 1
        $ house = "frenzy"
        $ momn = "Venus"
        jump frenzyroute
    "House of Hearts. Cupidia's house. Siren-centered. You have a feeling everyone's dated each other in this house at least once. Maybe this would be good for getting you out of your shell? Maybe you're not too great at fashion or vogue, but your charisma renders you a confidence imposter good enough to shoplift from the White House giftstore if you wanted to.":
        $ siren += 1
        $ house = "hearts"
        $ momn = "Cupidia"
        jump heartsroute
return
