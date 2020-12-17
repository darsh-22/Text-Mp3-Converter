from gtts import gTTS 

with open("input.txt", 'r') as file:
    
    file = file.read()
    
    # Language initialisation 
    language = 'en'

    # slow=False means high speed 
    print("========= Converting... =========") 
    myobj = gTTS(text=file, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named  output.mp3

    print("========= Start Saving... =========") 
    myobj.save("output.mp3") 

    print("============ Done ============")
