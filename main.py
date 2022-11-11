horoscope = {'January': 'Today, the stars advocate that you concentrate on money matters and how to save some, and in this purpose, you will remain engrossed. However, you are advised not to neglect domestic duties lest you encounter a morose spouse. So carry on and make a dash for that movie as planned. Do not cancel it.',
            'February': 'You will wake up feeling determined and decisive today. Be careful as your rigid views may make you seem stubborn. You may not be willing to come halfway during a conflict and will make a habit of articulating your viewpoint. Tension at the workplace will eat through most of your time today.！',
            'March': 'You will feel lonely and unwanted today. You will feel the need for someone who can calm your troubled mind. Meditation and yoga will help you calm yourself. It is a good day to receive love from that someone special.',
            'April': 'Your ideas today are the source of your energy. A situation may arise, which will force you to take hard decisions later. A new business or venture may prove beneficial. Your magical touch will bestow success in every endeavour.',
            'May': 'You will look to give your house a new appearance by decorating it or undertaking some renovation projects. You will make the best out of waste and produce some truly marvellous pieces of art for improving the ambience of your nest. You will be able to save up on some money.',
            'June': 'Keep an open mind and give vent to your imagination. You will feel very creative today and will pursue your innovative ideas. Luck will favour you, and some things on which you took some risk will bear fruits. You will be very energetic and enthusiastic about all the work you do.',
            'July': 'You will be busy in your work field today and will be able to attain your goals in your work field today. Your level of enthusiasm will be at its peak. Today you may be able to meet with a person of the opposite gender who will be your future partner.',
            'August': 'You are most likely to resent the dominating and overbearing nature of your partner today. Patience will probably go to the dumps in this case then. However, you are advised to sit together and resolve all personality clashes and quarrels because of the larger scheme of things.',
            'September': 'Expect a call to late-night revelry and a chance to binge. However, you don\'t seem to be in the mood to let your hair loose and party. However tempting it may be, your serious side will take over, and you shall deny the offer. No wonder they like that sensible head on your shoulders.',
            'October': 'You want to enhance your knowledge by exploring foreign shores, but luck hasn\'t favoured you yet. Today to be a favourable day for you to try again for higher studies. If associated with the stock market or speculation, you are likely to make profits. You will come across many opportunities, but you need to identify and explore them to the fullest.',
            'November': 'There are no short-cuts to success. You know this very well and work your socks off to get what you want. Colleagues, friends and family all of them will acknowledge and appreciate your efforts and achievements. Though you will be apprehensive about it, you will have to take some risks to bring the desired change in your life.',
            'December': 'Interactions with those of the opposite gender will mark your day. It is also an excellent day to strike up a friendship with them. For those in love, today is a good day to spend time with your partner. For those looking for love, now is the best time to pop the question to that special someone you\'ve secretly admired for long.'
            }

Dragon = """\
         __        _
       _/  \    _(\(o
      /     \  /  _  ^^^o
     /   !   \/  ! '!!!v'
    !  !  \ _' ( \____
    ! . \ _!\   \===^\)
     \ \_!  / __!
      \!   /    \\
(\_      _/   _\ )
 \ ^^--^^ __-^ /(__
  ^^----^^    "^--v'
            
            """
Snake = """\
             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

"""
Horse = """\
            .''
  ._.-.___.' (`\\
 //(        ( `'
'/ )\ ).__. ) 
' <' `\ ._/'\\
   `   \     \\

"""
Sheep = """\
૮꒰˵• ﻌ •˵꒱ა
"""
Monkey = """\
          __
     w  c(..)o   (
      \__(-)    __)
          /\   (
         /(_)___)
         w /|
          | \\
         m  m
"""
Rooster = """\
          www
          (*)<
          )((
     __  /  ))
    ( _\/_  /
   ( (    \|\\
          ,, ,,

"""
Dog = """\
   __
o-''|\_____/)
 \_/|_)     )
    \  __  /
    (_/ (_/  
"""
Pig = """\
             __,---.__
        __,-'         `-.
       /_ /_,'           \\&
       _,''               \\
      (")            .    |
        ``--|__|--..-'`.__|

"""
Rat = """\
              _..----.._    _
            .'  .--.    "-.(0)_
'-.__.-'"'=:|   ,  _)_ \__ . c\\'-..
             '''------'---''---'-"
"""
Ox = ""
Tiger = ""
Hare = ""

zodiac = {"Dragon": Dragon,
          "Snake": Snake,
          "Horse": Horse,
          "Sheep": Sheep,
          "Monkey": Monkey,
          "Rooster": Rooster,
          "Dog": Dog,
          "Pig": Pig,
          "Rat": Rat,
          "Ox": Ox,
          "Tiger": Tiger,
          "Hare": Hare}

print("             _ _ \n"
      "             | (_)           \n"
      " _______   __| |_  __ _  ___ \n"
      "|_  / _ \ / _` | |/ _` |/ __|\n"
      "/ / (_) | (_| | | (_| | (__ \n"
      "/___\___/ \__,_|_|\__,_|\___|\n")


songs = {'Sad': 'モラトリアム by Moratorium',
        'Happy': 'Into the I-LAND by IU',
        'Tired': 'Pour aller ou? by Lea Paci',
        'Stressed': 'NAKKA by IU',
        'Angry': 'La Di Die by Nessa Barrett',
        'In Love': 'Love Story by Taylor Swift',
        'Lazy': 'Ain\'t your mama by Jennifer Lopez'}

hello_world_translations = {'Arabic': 'مرحبا بالعالم!',
                            'Chinese': '你好世界！',
                            'English': 'Hello World!',
                            'French': 'Bonjour monde!',
                            'German': 'Hallo Welt!',
                            'Persian': 'سلام دنیا!',
                            'Russian': 'Привет мир!',
                            'Catalan': 'Hola món!',
                            'Hebrew': 'שלום עולם!',
                            'Spanish': 'Hola!',
                            'Latin': 'Salve!'}

while True:
    print("What language do you know?")
    print("Option:\n"
          "- Arabic \n"
          "- Chinese\n"
          "- English\n"
          "- French\n"
          "- German\n"
          "- Persian\n"
          "- Russian\n"
          "- Catalan\n"
          "- Hebrew\n"
          "- Spanish\n"
          "- Latin\n")
    language = input()
    if language in hello_world_translations.keys():
        print(hello_world_translations[language])
        break
    else:
        print("We don't support this languange yet\n"
              "\n"
              "　　　　　🌸＞＿＿ フ\n"
              "　　　　　| 　_　 _ l\n"
              "　 　　　／` ミ＿xノ\n"
              "　　 　 /　　　 　 |\n"
              "　　　 /　 ヽ　　 ﾉ\n"
              "　 　 │　　|　|　|\n"
              "　／￣|　　 |　|　|\n"
              "　| (￣ヽ＿_ヽ_)__)\n"
              "　＼二つ")

while True:
    print("Enter your birthday's month")
    print("Option:\n"
          "- January \n"
          "- February\n"
          "- March \n"
          "- April \n"
          "- May \n"
          "- June \n"
          "- July \n"
          "- August \n"
          "- September \n"
          "- October \n"
          "- November \n"
          "- December \n")
    month = input()
    if month in horoscope.keys():
        print(horoscope[month])
        break
    else:
        print("This month does not exist!")

while True:
    year = int(input("Input your birth year: "))
    if (year - 2000) % 12 == 0:
        sign = 'Dragon'
    elif (year - 2000) % 12 == 1:
        sign = 'Snake'
    elif (year - 2000) % 12 == 2:
        sign = 'Horse'
    elif (year - 2000) % 12 == 3:
        sign = 'sheep'
    elif (year - 2000) % 12 == 4:
        sign = 'Monkey'
    elif (year - 2000) % 12 == 5:
        sign = 'Rooster'
    elif (year - 2000) % 12 == 6:
        sign = 'Dog'
    elif (year - 2000) % 12 == 7:
        sign = 'Pig'
    elif (year - 2000) % 12 == 8:
        sign = 'Rat'
    elif (year - 2000) % 12 == 9:
        sign = 'Ox'
    elif (year - 2000) % 12 == 10:
        sign = 'Tiger'
    else:
        sign = 'Hare'
    print("Your zodiac sign is: ", sign)
    print()
    print(zodiac[sign])
    break

while True:
    print("What is your mood today?")
    print("Option:\n"
          "- Sad \n"
          "- Happy\n"
          "- Tired\n"
          "- Stressed\n"
          "- Angry\n"
          "- In Love\n"
          "- Lazy")
    mood = input()
    if mood in songs.keys():
        print("This is the song we recommend you listen to:")
        print(songs[mood])
        break
    else:
        print("We don't support this mood yet\n")
