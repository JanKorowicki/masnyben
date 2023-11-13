#https://www.purposegames.com/game/kartkowka-2-ga-czesc
import easyocr
import pyautogui
import time
a = 0
def rozpoznanie():
    image = pyautogui.screenshot("in_memory_to_disk.png",region=(485, 388, 470, 34))
    reader = easyocr.Reader(['pl'])
    result = reader.readtext('in_memory_to_disk.png', batch_size=100, detail=0)
    konc = ' '.join(result)
    return konc
time.sleep(2)
while a <= 28:
    miejsce = rozpoznanie()
    print(miejsce)
    if miejsce == "Press play!":
        pyautogui.click(x=779, y=710)
    elif miejsce == "Rysy":
        pyautogui.click(x=783, y=964)
    elif miejsce == "Góry świętokrzyskie":
        pyautogui.click(x=847, y=835)
    elif miejsce == "Gorce" or miejsce == "sorce":
        pyautogui.click(x=791, y=931)
    elif miejsce == "Pieniny":
        pyautogui.click(x=806, y=945)
    elif miejsce == "Góry izerskie":
        pyautogui.click(x=541, y=819)
    elif miejsce == "Podgórze karpackie":
        pyautogui.click(x=863, y=922)
    elif miejsce == "Opołonek":
        pyautogui.click(x=926, y=976)
    elif miejsce == "Kotlina kłodzka":
        pyautogui.click(x=603, y=866)
    elif miejsce == "Wzniesienie elbląskie":
        pyautogui.click(x=764, y=554)
    elif miejsce == "Masyw Śnieżnika":
        pyautogui.click(x=611, y=873)
    elif miejsce == "Góry stołowe":
        pyautogui.click(x=590, y=845)
    elif miejsce == "Śnieżka":
        pyautogui.click(x=559, y=831)
    elif miejsce == "Masyw babie góry":
        pyautogui.click(x=745, y=926)
    elif miejsce == "Przedgórze sudeckie":
        pyautogui.click(x=620, y=838)
    elif miejsce == "Łysica" or miejsce == "Lysica":
        pyautogui.click(x=821, y=833)
    elif miejsce == "Szewskie wzgórza":
        pyautogui.click(x=899, y=561)
    elif miejsce == "Podhale":
        pyautogui.click(x=778, y=944)
    elif miejsce == "Tatry":
        pyautogui.click(x=767, y=962)
    elif miejsce == "Kotlina Sandomierska":
        pyautogui.click(x=894, y=878)
    elif miejsce == "Kotlina oświęcimska":
        pyautogui.click(x=724, y=900)
    elif miejsce == "Dylewska góra":
        pyautogui.click(x=779, y=606)
    elif miejsce == "Karkonosze":
        pyautogui.click(x=572, y=828)
    elif miejsce == "Trzy korony":
        pyautogui.click(x=830, y=947)
    elif miejsce == "Kotlina jeleniogórska":
        pyautogui.click(x=560, y=815)
    elif miejsce == "Barania góra":
        pyautogui.click(x=723, y=937)
    elif miejsce == "Bieszczady":
        pyautogui.click(x=902, y=950)
    elif miejsce == "Góry sowie":
        pyautogui.click(x=597, y=823)
    elif miejsce == "Wieżyca" or miejsce == "Wiezyca":
        pyautogui.click(x=685, y=555)
    a +=1


