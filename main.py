songs = {'Sad': 'When the Party Is Over by Billie Eilish',
        'Happy': 'Happy by Pharrel Williams',
        'Tired': 'Slow Up by Jacob Banks',
        'Stressed': 'In My Blood by Shawn Mendes',
        'Angry': 'Roar by Katy Perry',
        'In Love': 'Love Story by Taylor Swift',
        'Lazy': 'The Lazy Song by Bruno Mars'}

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