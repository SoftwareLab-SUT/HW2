songs = {'Sad': 'モラトリアム by Moratorium',
        'Happy': 'Into the I-LAND by IU',
        'Tired': 'Pour aller ou? by Lea Paci',
        'Stressed': 'NAKKA by IU',
        'Angry': 'La Di Die by Nessa Barrett',
        'In Love': 'Love Story by Taylor Swift',
        'Lazy': 'Ain\'t your mama by Jennifer Lopez'}

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