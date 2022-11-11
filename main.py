horoscope = {'January': 'Today, the stars advocate that you concentrate on money matters and how to save some, and in this purpose, you will remain engrossed. However, you are advised not to neglect domestic duties lest you encounter a morose spouse. So carry on and make a dash for that movie as planned. Do not cancel it.',
            'February': 'You will wake up feeling determined and decisive today. Be careful as your rigid views may make you seem stubborn. You may not be willing to come halfway during a conflict and will make a habit of articulating your viewpoint. Tension at the workplace will eat through most of your time today.！',
            'March': 'You will feel lonely and unwanted today. You will feel the need for someone who can calm your troubled mind. Meditation and yoga will help you calm yourself. It is a good day to receive love from that someone special.',
            'April': 'Your ideas today are the source of your energy. A situation may arise, which will force you to take hard decisions later. A new business or venture may prove beneficial. Your magical touch will bestow success in every endeavour.',
            'May': 'You will look to give your house a new appearance by decorating it or undertaking some renovation projects. You will make the best out of waste and produce some truly marvellous pieces of art for improving the ambience of your nest. You will be able to save up on some money.',
            'June': 'Keep an open mind and give vent to your imagination. You will feel very creative today and will pursue your innovative ideas. Luck will favour you, and some things on which you took some risk will bear fruits. You will be very energetic and enthusiastic about all the work you do.',
            }

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
