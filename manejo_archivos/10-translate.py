from translate import Translator

with open("message.txt","r") as message:
    message_text = message.read()
    print(f"Mensaje original {message_text}")
    print("Translating....")
    translator = Translator(to_lang="es")
    translation = translator.translate(message_text)
    print(f"Mensaje traducido: {translation}")


    with open("translated_message.txt","w") as message_translation:
         message_translation.write(translation)



