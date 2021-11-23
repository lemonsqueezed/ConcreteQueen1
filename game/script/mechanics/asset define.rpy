# ░▒▓████████████████████████████████████■
## 【 CALLBACKS 】 ░▒▓████████████████████■
# ░▒▓████████████████████████████████████■
init python:
    renpy.music.register_channel("ctc", "voice", False)
    def voice_beeps (on=False, char=1):
        if on:
            if char==0: ##MC##
                renpy.music.play("audio/voice/mc_voice.ogg",
                channel="ctc", loop="True")
            elif char==1: ##SWANNA##
                renpy.music.play("audio/voice/swa_voice.ogg",
                channel="ctc", loop="True")
            elif char==2: ##VENUS##
                renpy.music.play("audio/voice/ven_voice.ogg",
                channel="ctc", loop="True")
            elif char==3: ##CUPIDIA##
                renpy.music.play("audio/voice/cup_voice.ogg",
                channel="ctc", loop="True")
            else:
                renpy.music.stop(channel="ctc")
    def beepy(event, char=1, **kwargs):
        if event == "show_done" or event == "begin":
            voice_beeps(True, char)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="ctc")


# ░▒▓████████████████████████████████████■
## 【 BACKGROUNDS 】 ░▒▓██████████████████■
# ░▒▓████████████████████████████████████■
image bg blrm = "/images/bgs/ballroomy.jpg"
image bg sk8rnk = "/images/bgs/rollerrink.jpg"
image bg asway = "/images/bgs/astorplace.jpg"

image bg cd1 = "/images/bgs/cityday.jpg"
image bg cd2 = "/images/bgs/cityday2.jpg"
image bg cd3 = "/images/bgs/cityday3.jpg"
image bg cd4 = "/images/bgs/cityday4.jpg"

image bg cn1= "/images/bgs/citynight.jpg"
image bg cn2 = "/images/bgs/citynight2.jpg"
image bg cn3 = "/images/bgs/citynight3.jpg"

# ░▒▓████████████████████████████████████■
## 【 CHARACTERS 】 ░▒▓███████████████████■
# ░▒▓████████████████████████████████████■
# NARRATOR
define nar = Character(None,
cb_char=0,
callback=beepy,
what_italic=True,
who_color="ffffff")

# MAIN CHARACTER / NAME-ABLE CHARACTER
define mc = Character("[mcn]",
image="mc",
who_color="ffffff",
dynamic=True,
cb_char=0,
callback=beepy)

# ALI(YAH) / SWANNA SONG / HOUSE OF ELEGANCE [1]
define swa = Character("Swanna Song",
image="swan",
who_color="FFFF00",
cb_char=1,
callback=beepy)
image swa idle = "images/characters/swa/swa1.png"
# image swa talk = "images/characters/swa/swa2.png"

# NIA / VENUS FLYE / HOUSE OF VOGUE [2]
define ven = Character("Venus Fly",
image="venus",
who_color="04d9ff",
cb_char=2,
callback=beepy)
image ven idle = "images/characters/ven/ven1.png"
# image ven talk = "images/characters/ven/ven2.png"

# IMANI DAVIS / CUPIDIA / HOUSE OF SIREN [3]
define cup = Character("Cupidia",
image="cupid",
who_color="c6171a",
cb_char=3,
callback=beepy)
image cup idle = "images/characters/cup/cup1.png"
# image cup talk = "images/characters/cup/cup2.png"

# ░▒▓████████████████████████████████████■
## 【 AUDIO 】 ░▒▓████████████████████████■
# ░▒▓████████████████████████████████████■
# MUSIC
define audio.masterblaster = "audio/bgm/masterblaster.mp3"
# SOUND EFFECTS
define audio.applause = "audio/soundfx/applause.wav"
define audio.breathing = "audio/soundfx/breathing.ogg"
define audio.breathing2 = "audio/soundfx/breathing2.wav"
define audio.crowdcheering = "audio/soundfx/crowdcheering.wav"
define audio.heelwalk = "audio/soundfx/heelwalk.wav"
define audio.heelwalk2 = "audio/soundfx/heelwalk2.m4a"
define audio.star = "audio/soundfx/star.wav"
define audio.star2 = "audio/soundfx/star2.mp3"
