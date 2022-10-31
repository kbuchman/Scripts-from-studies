from .text_from_image import get_text_from_image
from .scrap_screenshot import take_screenshot, mouse_pos_scrap_horizontal
from os import remove

def get_value_from_text(word_before, word_after, type=float):
    # getting screenshot of task area
    screen = take_screenshot(*mouse_pos_scrap_horizontal(100, 400, 450, 50))
    #screen.show()
    screen.save('./screen.png')

    # getting text 
    text = get_text_from_image('./screen.png', 'pol')

    remove('./screen.png')

    # getting value 
    words = text.split()
    for i, word in enumerate(words):
        if word == word_before:
            if words[i + 2] == word_after:
                return type(words[i + 1].replace(',', '.'))
    return None

def main():
    print(get_value_from_text('wynosi', 's.'))

if __name__ == '__main__':
    main()