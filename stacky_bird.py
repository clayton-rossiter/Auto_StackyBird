from ppadb.client import Client
import time
import mss
import os
import numpy as np

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
        self.stack = 125    # time in ms to add one stack
        self.refresh = 125  # time to move one block
        # below parameters were tested on a 1280x800 monitor
        # relative sizes are later calculated in get_resolution()
        self.referenceGroundLevel= 500/800
        self.referenceBlockSize = 25/800
        self.referencePaddingLeft = 60/1280     # padding of bird from left screen
        self.referenceScreenWidth = 260/1280    # width of playable device screen
        self.referenceScreenHeight = 500/800    # height of playable device screen
        self.referenceScreenTop = 145/800       # distance in px from 0,0 to playable screen top
        self.get_resolution()
        self.connect()

        def initialise_grid():
            # create empty grid of values for colours

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
        # currently only works with 1 monitor, or game working on first monitor
        sct = mss.mss()
        img = sct.grab(sct.monitors[1])
        self.monitorWidth = img.size[0]
        self.monitorHeight = img.size[1]
        self.blockSize = self.referenceBlockSize*self.monitorHeight
        self.groundLevel = self.referenceGroundLevel*self.monitorHeight
        self.screenHeight = self.referenceScreenHeight*self.monitorHeight
        self.screenTop= self.referenceScreenTop*self.monitorHeight
        self.paddingLeft = self.referencePaddingLeft*self.monitorWidth
        self.screenWidth = self.referenceScreenWidth*self.monitorWidth
        # self.birdX = self.referenceBlockX*self.monitorWidth

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

    def update(self):
        while True:
            current_time = time.time()
            self.check_grid()
            time.sleep(time.time()-current_time)

        def check_grid(self):
            # approximately 10 blocks per screen width
            # approximately 20 blocks per screen height
            # only need to consider blocks right of bird (3 blocks right)
            # monitor centre point of grid 
            self.screenshot()

        
        def screenshot(self):
            # take screenshot of just the phone screen
            # assuming Apowermirror screen is far left of screen
            with mss.mss() as sct:
                monitor = {"top": self.screenTop, "left": 0, "width": self.screenWidth, "height": self.screenHeight}
                self.rgba = np.array(sct.grab(monitor))
            # count current height of bird
            


if __name__ == '__main__':
    game = StackyBird()