import pyscreenshot as sc
import pyautogui as gui

def take_screenshot(xs, ys, xe, ye):
    screen = sc.grab((xs, ys, xe, ye))
    return screen

def mouse_pos_scrap_horizontal(margin_left, margin_rigth, top, bottom):
        _, y = gui.position()
        return 0 + margin_left, y - top, gui.size()[0] - margin_rigth, y + bottom

def mouse_pos_scrap_vertical(left, rigth, margin_top, margin_bottom):
        x, _ = gui.position()
        return x - left, 0 + margin_top, x + rigth, gui.size()[1] - margin_bottom

def main():
    take_screenshot(*mouse_pos_scrap_horizontal(50, 400, 200, 50)).show()

if __name__ == '__main__':
    main()