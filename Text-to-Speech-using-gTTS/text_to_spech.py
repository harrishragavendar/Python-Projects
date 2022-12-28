from gtts import gTTS
import os
file = open('python.txt','r')
file_txt = file.read().replace('\n',' ')
language = 'en'
output = gTTS(text = file_txt, lang = language, slow = False)
output.save('python.mp3')
file.close()
os.system('start python.mp3')