from text_from_image import get_text_from_image
from scrap_screenshot import take_screenshot, mouse_pos_scrap_horizontal

def main():
    screen = take_screenshot(*mouse_pos_scrap_horizontal(100, 400, 250, 50))
    screen.show()
    screen.save('screen.png')

    text = get_text_from_image('screen.png', 'pol')
    print(text)

if __name__ == '__main__':
    main()