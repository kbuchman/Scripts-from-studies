import sys
sys.path.append(r'D:/Programming/Useful scripts for studies/')

from Scripts.text_from_image import get_text_from_image
from Scripts.scrap_screenshot import take_screenshot, mouse_pos_scrap_horizontal
from os import remove
import keyboard

def get_value_from_text(input_val, type=float):
    # checking input
    for i in input_val:
        if len(i) != 2:
            return None

    # getting screenshot of task area
    screen = take_screenshot(*mouse_pos_scrap_horizontal(100, 100, 300, 50))
    # screen.show()
    screen.save('./screen.png')

    # getting text 
    text = get_text_from_image('./screen.png', 'pol')
    # print(text)
    remove('./screen.png')

    # getting value 
    values = []
    words = text.split()
    for val in input_val:
        for i, word in enumerate(words):
            if val[0] == word:
                if str(val[1]) == str(words[i + 2]):
                    # print(val[0], word, words[i + 1], words[i + 2], val[1], val[1] == True)
                    values.append(type(words[i + 1].replace(',', '.')))
                    break
    return None if len(values) == 0 or len(values) != len(input_val) else values

def main():
    search_val = (('jeszcze', True),)
    keyboard.wait('ctrl')
    print(get_value_from_text(search_val, float))

if __name__ == '__main__':
    main()