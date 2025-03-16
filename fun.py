import pyautogui
import random
import time
from pynput import keyboard
import subprocess
import threading

time.sleep(2)

exit_flag = False
print(pyautogui.size())
size=pyautogui.size()

def on_press(key):
    global exit_flag
    if key == keyboard.Key.backspace:  # 当按下 Backspace
        exit_flag = True  # 退出标志设为 True
        return False  # 结束监听

listener = keyboard.Listener(on_press=on_press)
listener.start()

pyautogui.FAILSAFE=False


def Open_Terminals():
    script = """
        tell application "Terminal"
            do script ""
            activate
        end tell
        """
    subprocess.run(["osascript", "-e", script])  # 执行 AppleScript 打开新窗口
    volume = random.randint(0, 100)  # 生成 0 到 100 之间的随机音量
    script = f"set volume output volume {volume}"
    subprocess.run(["osascript", "-e", script])
    print(f"volume: {volume}%")

while not exit_flag:
    numx = random.randint(1, size.width)
    print(numx)
    numy = random.randint(1, size.height)
    print(numy)
    print(pyautogui.moveTo(numx, numy,duration=0.05))
    t=threading.Thread(target=Open_Terminals)
    t.start()




























