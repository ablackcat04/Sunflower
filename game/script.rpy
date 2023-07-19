init:
    $ style.default.font = "Taipei.ttf"
    $ style.default.language = "Taipei"


init python:
    style.default.layout = "greedy"
    renpy.music.register_channel("music2","music")
    renpy.music.register_channel("Piano","music")
    renpy.music.register_channel("Flute","music")
    renpy.music.register_channel("Tuba","music")
    config.main_menu_music = "audio/title.ogg"


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.main_menu_music_fadein = 2.0
#define config.main_menu_music_fadeout = 2.0
#define config.main_menu_music_volume = 0.7

define A = Character("ABlackCat")
define Ice = Character("Iceiron")
define Is = Character("Fubuki is cat")

define You = Character("你")
define G = Character("(暫定)")
define Q = Character("?")

define D = Dissolve(0.05)
define P = pixellate

image G black = "black.png"
image G con = "conscientious.png"
image G dontknow = "dontknow.png"
image G dontlike = "dontlike.png"
image G happy = "happy.png"
image G happy2 = "happy2.png"
image G mad = "mad.png"
image G pity = "pity.png"
image G shy = "shy.png"
image G smile = "smile.png"


image bg Splash = "Ice Is Cat.png"
image bg Title = "bg Title.png"
define White = "#FFFFFF"
define Black = "#000"
image bg Black = "#000"
define Camellia = "#1f1e33"
image bg Book = "1.png"
image bg RedBook = "RedBook.png"
image bg AirBook = "AirBook.png"
image bg PixelBook = "PixelBook.png"


define BGM = "audio/Sunflower_Background_Music.mp3"
define Title = "audio/title.ogg"

define BGM10 = "audio/1-0.ogg"
define BGM11 = "audio/1-1.ogg"
define BGM12 = "audio/1-2.ogg"
define BGM13 = "audio/1-3.ogg"
define BGM14 = "audio/1-4.ogg"

define BGM20 = "audio/2-0.ogg"
define BGM21 = "audio/2-1.ogg"
define BGM22 = "audio/2-2.ogg"
define BGM23 = "audio/2-3.ogg"
define BGM24 = "audio/2-4.ogg"

define BGM30 = "audio/3-0.ogg"
define BGM3F = "audio/3-F.ogg"
define BGM3P = "audio/3-P.ogg"
define BGM3T = "audio/3-T.ogg"

define IceIsCat = "audio/ice is cat.ogg"


# The game starts here.


label splashscreen:

    show bg Black

    play music "<silence 0.75>"
    queue music IceIsCat volume 0.5 noloop

    show bg Splash
    with Dissolve(1.5)

    pause 0.5

    hide bg Splash with Dissolve(1.5)

    return


label start:

    stop music fadeout 2.0

    pause 1.0

    play music BGM10 fadein 1.0

    show bg Black
    with Dissolve(1.0)

    show bg Book
    with Dissolve(2.0)

    "一天在早晨一如往常的醒來"
    with None



    "「早安」一位陌生的（女子暫定）向你搭話"

    $ mlength = renpy.music.get_duration(channel='music')

    $ mpos = renpy.music.get_pos(channel='music')

    if (mlength)*4/9 >= (mpos):
        #前面
        $ msilence = (mlength)*4/9 - mpos
        queue music2 ("<silence %s>"% (msilence))
        queue music ("<silence %s>"% (msilence))
        queue music2 BGM13 noloop
        queue music2 BGM14 noloop

    else:
        #後面
        $ msilence = (mlength) - mpos
        queue music2 ("<silence %s>"% (msilence))
        queue music ("<silence %s>"% (msilence))
        queue music2 BGM11 noloop
        queue music2 BGM13 noloop
        queue music2 BGM14 noloop

    "他笑著 "



    show bg AirBook
    with D

    show bg RedBook
    with D

    show bg AirBook
    with D

    show bg Book
    with D

    pause 0.02

    show bg AirBook
    with D

    show bg RedBook
    with D

    show bg AirBook
    with D

    show bg Book
    with D

    "彷彿在記憶深處封印的記憶要被解開"

    "你是 "

    show bg PixelBook
    with P

    "你留著兩行淚說著 "

    "彷彿回到以前，那純粹的年代 "

    "多少次想放棄，多少次想認輸 "

    "是你，是你讓我有繼續走下去的動力 "

    "世界是如此的污濁不清，是如此的混亂不堪。你的溫柔仍在我心中遊蕩。 "
    with D

    #"（Bgm01下） "

    if(renpy.music.is_playing(channel='music2')):
        stop music2 fadeout 2.0

    show bg Black
    with Dissolve(2.0)

    play music BGM20

    pause 2.0

    show G con
    with Dissolve(2.0)

    G "我很擔心你，所以回來看看"

    #"轉身離去"
    show G smile
    "謝謝你，再會了"

    show G shy
    pause 0.5
    show G con
    "隨後不自覺的牽起了他的手"

    $ mlength = renpy.music.get_duration(channel='music')

    $ mpos = renpy.music.get_pos(channel='music')

    if (mlength)*1/2 >= (mpos):
        #前面
        $ msilence = (mlength)*1/2 - mpos
        queue music2 ("<silence %s>"% (msilence))
        queue music ("<silence %s>"% (msilence))
        queue music2 BGM23 noloop
        queue music2 BGM24

    else:
        #後面
        $ msilence = (mlength) - mpos
        queue music2 ("<silence %s>"% (msilence))
        queue music ("<silence %s>"% (msilence))
        queue music2 BGM22 noloop
        queue music2 BGM23 noloop
        queue music2 BGM24

    show G con
    "沉默了一陣子後他甩開手"


    show G happy2
    "並言語道 "

    show G happy
    "放手吧，都過去了，你我應在此相別，人生無不散的宴席，放下吧。我是你無法負擔的沉重的枷鎖，再會了。"



    "手被甩開 "
    hide G
    with P


    "你呆滯在原地，回憶著往事，無情的他，可憐的你，究竟是從何時開始才走到這一步的。"

    #"（太陽花枯萎貌） "


    #

    stop music2 fadeout 2.0


    pause 2.0
    stop music2
    stop music


    play Piano BGM3P volume 0.15 fadeout 2.0
    play Flute BGM3F volume 0.1 fadeout 2.0
    play Tuba BGM3T volume 0.1 fadeout 2.0
    $ renpy.music.set_volume(0, delay=0, channel='Tuba')
    $ renpy.music.set_volume(0, delay=0, channel='Flute')

    "童年時，花田中的約定 "


    show bg Title
    with P

    "我要永遠和你在一起 "

    "童言童語的說著 "

    "我們約定好了噢。 "

    "來打勾勾 "

    "冬天時 "

    "奔跑在乾涸的稻田中 "

    "嬉戲著 "

    "在田中放著鞭炮，烤著地瓜 "
    $ renpy.music.set_volume(0.5, delay=6, channel='Tuba')

    "跌倒了互相攙扶著回家"

    "他臉上的笑靨是珍貴的寶物"

    "眼淚是寶貴的珍珠"

    "夏天時在稻田邊吃著冰過的西瓜"

    "聊著天 "

    "在牛郎織女的見證下，互許的承諾 "

    "直到幾年之後 "

    "這個送你 "

    "別忘呢我 "

    "再見，不要哭，要笑，以後一定會再見的 "

    "互贈的情意，不捨的訣別 "
    $ renpy.music.set_volume(1.0, delay=6, channel='Tuba')
    $ renpy.music.set_volume(0.5, delay=6, channel='Flute')

    "在命運的捉弄下，必須要舉家遷移到遙遠的台北 "

    "簡單的禮物，太陽花的枝條，在手中握緊 "

    "不曾忘記童年時的約定 "

    "無論在何時，何地總是帶著一片花瓣，期盼能遇見她 "

    "為了忘卻煩惱，你專注於讀書當中，你我想要給你更好的生活 "

    "強烈的信念支持著你 "

    "終於考上了一流的高中，淡忘了目的的你，充滿的空洞"

    "在蓊鬱的高中迷失著自我，專心著考上大學 "

    "無法親近的你，在班上角落邊緣蜷縮讀著自己的書，譜著人生的道路。 "

    "放學後無處可去的你獨自回到了家 "

    "渾渾噩噩的專心在自己的學業上，努力達成的成就真的是我所期待的嗎?說不定他根本沒有在等我，只是我一廂情願罷了，哈哈。 "
    $ renpy.music.set_volume(1.0, delay=6, channel='Flute')

    "可是想到那時青澀的約定你不禁淚流滿面，握著那時的花瓣所做成的書籤哭泣，你心中的堅持越來越弱了。 "

    "到了大學努力在研究上無暇顧及其他事情，當年的承諾已然凋零，如花的凋謝出社會之後仍舊努力著，儘管凋零，仍剩枝條頑強的支撐著你的心靈，出了社會後連枝條也不剩了，領著不高的薪水過著得過且過的每天 "

    "渾噩的你失去了目標，直到他再次找你分離的那一天，看到你窩囊的樣子說地重話與你分別，一來是刺激你振作，二來這次是真正的分別了。"

    "下一次見到他時你他已入土，剩張相片紀念著，你默默地送上了的太陽花。 "

    "輕輕地笑著，彷彿他送別你那天，你聽到了自己的話。 "

    "再見別忘了我。 "

    "那天，我沒察覺你的異樣，那天你忍痛和我分離，打著嗎啡強忍劇痛甩門，原來你沒有時間了。謝謝你，現在我能為你做的剩下，譜著你的故事，留下你存在的證據 。"

    stop Piano fadeout 5.0
    stop Flute fadeout 5.0
    stop Tuba fadeout 5.0
    pause 5.0
    #$ renpy.pause(5, hard=True)

    stop Piano
    stop Flute
    stop Tuba
    stop music
    stop music2

    # This ends the game.

    return
