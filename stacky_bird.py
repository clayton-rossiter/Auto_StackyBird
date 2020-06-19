from ppadb.client import Client
import time
import mss
import os

class StackyBird():
    def __init__(self, host='127.0.0.1', port=5037):
        self.host = host
        self.port = port
        self.startx = 535
        self.starty = 1688
        self.holdx = 560
        self.holdy = 1000
        self.revivex = 565
        self.revivey = 1900
        self.nextLevelX = 545
        self.nextLevelY = 1945
        self.colorBird = (253,251,125)
        self.colorGrass = (0,247,160)
        self.colorMudLight = (253,141,95)
        self.colorMudDark = (238,123,78)
        self.referenceGroundLevel= 500/800
        self.referenceBlockHeight = 25/800
        self.referenceBlockX = 75/1280
        self.referenceScreenWidth = 260/1280
        self.referenceScreenHeight = 500/800
        self.referenceScreenBottom = 640/800
        self.stack = 125    # time in ms to add one stack
        self.get_resolution()
        self.connect()

    def connect(self):
        # connect to android device
        self.adb = Client(host=self.host, port=self.port)
        try:
            self.device = self.adb.devices()[0]
        except:
            print("Cannot connect to phone!")
    
    def get_resolution(self):
        # needed to get screen resolution to scale heights
        # take screenshot and get number of pixels
        sct = mss.mss()
        img = sct.grab(sct.monitors[1])
        self.monitorWidth = img.size[0]
        self.monitorHeight = img.size[1]
        self.blockHeight = self.referenceBlockHeight*self.monitorHeight
        self.groundLevel = self.referenceGroundLevel*self.monitorHeight
        self.screenHeight = self.referenceScreenHeight*self.monitorHeight
        self.screenBottom = self.referenceScreenBottom*self.monitorHeight
        self.screenWidth = self.referenceScreenWidth*self.monitorWidth
        self.birdX = self.referenceBlockX*self.monitorWidth

    def tap(self, x, y):
        command = 'input tap {} {}'.format(x,y)
        self.device.shell(command)

    def hold(self, duration):
        command = 'input swipe {} {} {} {} {}'.format(self.holdx,self.holdy,self.holdx,self.holdy,duration)
        self.device.shell(command)
        print('Screen held for {} ms'.format(duration))

    def start(self):
        time.sleep(3)
        self.tap(self.startx, self.starty)
        print('Game started!')

    def revive(self):
        self.tap(self.revivex, self.revivey)
        print('Tapped to restart')
        self.start()
    
    def next_level(self):
        self.tap(self.nextLevelX, self.nextLevelY)
        print('Level complete!')
        self.start()

    def screenshot(self):
        self.screenshot = mss.mss()
        # get pixel matrix


    def update(self):
        current_time = time.time()
        self.screenshot()


if __name__ == '__main__':
    game = StackyBird()
    # game.start()
    # game.update()