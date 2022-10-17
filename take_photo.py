# import pyautogui as pg
# import time
# pg.click(65,1079)
# time.sleep(2)
# pg.click(1536,151)
# time.sleep(2)
# pg.click(680,352)
# time.sleep(2)
# pg.typewrite("cheese")
# pg.typewrite(["enter"])
# pg.click(925,1342)
# time.sleep(3)
# pg.doubleClick()

import pyautogui as pg
import time
time.sleep(10)
for i in range(10):
    pg.write(" https://www.google.com/search?q=regular+division+vs+floor+division+in+python&source=lmns&bih=764&biw=1464&hl=en&sa=X&ved=2ahUKEwjA5bH5md_5AhU_EbcAHWmxBoQQ_AUoAHoECAEQAA#bsht=CgRmYnNtEgYIBBAAGAw")
    pg.press("Enter")
