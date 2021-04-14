import pyautogui as p

try:
    print(p.position())
    x, y = p.size()
    print(f'Size of screen: {x}px x {y}px')
    p.moveTo(x/2, y/2, 1)
    print(f'Current pos: {p.position()}')
    #p.move(50, 50, 1)

except:
    print("aborted")
