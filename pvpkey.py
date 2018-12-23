import win32gui, win32api, win32con,time
from win32api import GetSystemMetrics
from PIL import ImageGrab

def PilImage(x,y):
    a, b = GetSystemMetrics(0), GetSystemMetrics(1)  # Python获取屏幕分辨率
    im = ImageGrab.grab((0,0,a,b))#与坐标不同，这里0，0，1，1是一个像素，而坐标是从0~1919的
    pix = im.load()
    return pix[x,y]

def DisplaySize():
    return GetSystemMetrics(0), GetSystemMetrics(1)  # Python获取屏幕分辨率

def LeftClick(x, y):    # 鼠标左键点击屏幕上的坐标(x, y)
    win32api.SetCursorPos((x, y))    # 鼠标定位到坐标(x, y)
    # 注意：不同的屏幕分辨率会影响到鼠标的定位，有需求的请用百分比换算
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)    # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 鼠标左键弹起

    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN + win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 测试

def PressOnce(x):    # 模拟键盘输入一个按键的值，键码: x
    win32api.keybd_event(x, 0, 0, 0)

'''
# 测试
a, b = DisplaySize()
print(a,b)
LeftClick(30, 30)  # 点击
PressOnce(13)  # Enter
PressOnce(9)   # TAB
print(PilImage(80,546))
'''
# SetCursorPos', 'No error message is available' 用管理员身份运行pycharm
if __name__=="__main__":
    jisu=0
    ltime=0
    ntime=0
    time.sleep(5)
    print(PilImage(875, 573))
    print(PilImage(908,323))
    print(PilImage(1050, 635))
    print(PilImage(914,486))
    while 1:

        if PilImage(875, 573)==(220, 154, 39):
            LeftClick(875, 573)
            jisu += 1
            ntime = time.time()-ltime
            ltime = time.time()
            print("刷了第%d次,获得%d经验,用时%d秒" % (jisu,jisu*82,ntime))
        elif PilImage(908,323)==(26, 35, 101):
            LeftClick(908,323)
        elif PilImage(1050,635)==(216, 125, 26):
            LeftClick(1050,635)
        elif PilImage(1061,138)==(48, 131, 205):
            LeftClick(1061,145)
        elif PilImage(1061,138)==(46, 125, 197):
            LeftClick(1061,145)
        elif PilImage(914,486)==(196,39,80):
            LeftClick(914,486)
        else:
            pass

        time.sleep(5)