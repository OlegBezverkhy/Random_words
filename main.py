from requests import get
from bs4 import BeautifulSoup
from googletrans import Translator

yes = ('y', 'Y', 'Д', 'д')


def get_english_words():
    url = 'https://randomword.com/'
    translator = Translator()
    try:
        response = get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        return {'english_words': translator.translate(english_words, dest='ru').text,
                'word_definition': translator.translate(word_definition, dest='ru').text
                }
    except:
        print(f'Произошла ошибка')
        return None


def word_game():
    print('Добро пожаловать в игру')
    while True:
        word_dict = get_english_words()
        if word_dict:
            words = word_dict.get('english_words')
            word_definition = word_dict.get('word_definition')
            print(f'Значение слова - {word_definition}')
            user = input('Что это за слово? ')
            if user == words:
                print('Ответ венный')
            else:
                print(f'Ответ: {user} неверный. Было загадано это слово:  {words}')
        play_again = input('Хотите сыграть еще раз ?(y/n):')
        if play_again not in yes :
            print('Спасибо за игру')
            break


def main():
    word_game()


if __name__ == '__main__':
    main()
