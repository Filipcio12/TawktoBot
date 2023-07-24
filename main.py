import pyautogui as pag
import keyboard
import time

def main():
    time.sleep(3)
    refresh()

    while not keyboard.is_pressed('q'):
        click_img("elements/powiadomienia.png")
        if not click_img("elements/falka.png"):
            refresh()
            continue
        
        if not click_img("elements/obsluzone.png"):
            continue

        if not click_img("elements/v.png"):
            continue
                
        if not click_img("elements/dolacz_do_rozmowy.png"):
            continue

        if not click_img("elements/dzien_dobry.png"):
            if not click_img("elements/reply.png"):
                continue
            welcome_msg()
        else:
            refresh()
            continue

def refresh():
    pag.hotkey("f5")
    time.sleep(2)

def welcome_msg():
    pag.typewrite("Dzie")
    pag.hotkey("altright", "n")
    pag.typewrite(" dobry,")
    pag.hotkey("shift", "enter")
    pag.typewrite("Czy mog")
    pag.hotkey("altright", "e")
    pag.typewrite(" w czym")
    pag.hotkey("altright", "s")
    pag.typewrite(" pom")
    pag.hotkey("altright", "o")
    pag.typewrite("c?")
    pag.hotkey("enter")

def click_img(img_path: str):
    res = pag.locateCenterOnScreen(img_path, confidence=0.8)
    if res is not None:
        x, y = res
        pag.moveTo(x, y, 1)
        print(img_path[9:-4] + " found")
        pag.click()
        time.sleep(2)
        return True
    else:
        print(img_path[9:-4] + " not found")
        return False

if __name__ == "__main__":
    main()