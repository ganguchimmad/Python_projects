import os
from googletrans import Translator, LANGUAGES ,constants
from pprint import pprint

#os.system("start winword")
translator = Translator()

# translate a spanish text to arabic for instance
sentences = [
    "Hello everyone",
    "How are you ?",
    "Do you speak english ?",
    "Good bye!"
]
translations = translator.translate(sentences, dest="kn")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")