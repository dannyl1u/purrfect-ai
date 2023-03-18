from flask import Flask, jsonify, request
import random


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "up and running"


def add_french_accents(word):
    """
    Adds random French accents to a word
    """
    # accents = ['é', 'è', 'ê', 'ë', 'à', 'â', 'î', 'ï', 'ô', 'ù', 'û']
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowel_dict = {
        "a": ['à', 'â'],
        "e": ['é', 'è', 'ê', 'ë'],
        "i": ['î', 'ï'],
        "o": ['ô'],
        "u": ['ù', 'û']
    }

    accented_word = ''
    for letter in word:
        if letter in vowels:
            letter = random.choice(vowel_dict[letter])
            accented_word += letter
        else:
            accented_word += letter
    if (accented_word[len(accented_word) - 1] == 'n'):
        accented_word += 'é'
    return accented_word

def translate_to_french(text):
    """
    Translates an English string to French
    """
    words = text.split()
    translated_words = []
    for word in words:
        accented_word = add_french_accents(word)
        translated_words.append(accented_word)
    translated_text = ' '.join(translated_words)
    return translated_text


@app.route('/translate', methods=['GET'])
def translate():
    name = request.args.get('name')
    return translate_to_french(name)

app.run(host="localhost", port=8000, debug=True)
