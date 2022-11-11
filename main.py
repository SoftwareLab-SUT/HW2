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

hello_world_translations = {'Arabic': 'مرحبا بالعالم!',
                            'Chinese': '你好世界！',
                            'English': 'Hello World!',
                            'French': 'Bonjour monde!',
                            'German': 'Hallo Welt!',
                            'Persian': 'سلام دنیا!',
                            'Russian': 'Привет мир!'}

while True:
    print("What language do you know?")
    print("Option:\n"
          "- Arabic \n"
          "- Chinese\n"
          "- English\n"
          "- French\n"
          "- German\n"
          "- Persian\n"
          "- Russian")
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