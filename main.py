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
