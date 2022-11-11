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
