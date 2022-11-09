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
