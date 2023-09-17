import autopy


class Mouse():
    def __init__(self):
        pass
    
    def move(self, x, y):
        # move mouse
        autopy.mouse.move(x, y)
    
    def click(self):
        autopy.mouse.click()
    
