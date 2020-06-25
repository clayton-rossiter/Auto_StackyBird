from ppadb.client import Client
import time
import mss
import os
import numpy as np
from PIL import Image
import cv2

class StackyBird():
    def __init__(self, host='127.0.0.1', port=5037):
        self.host = host
        self.port = port
        # phone co-ordinates
        self.startx = 535
        self.starty = 1688
        self.holdx = 560
        self.holdy = 1000
        self.revivex = 565
        self.revivey = 1900
        self.nextLevelX = 545
        self.nextLevelY = 1945
        # time durations (ms)
        self.stack = 125    # time in ms to add one stack
        self.refresh = 125  # time to move one block
        # set colour boundary conditions
        self.boundaryBirdLower = [220,170,100]
        self.boundaryBirdUpper = [255,255,160]
        self.boundaryBlockLower = []    # updates with start()
        self.boundaryBlockUpper = []    # updates with start()
        self.boundaries = (
            (self.boundaryBirdLower, self.boundaryBirdUpper),
            (self.boundaryBlockLower, self.boundaryBlockUpper)
            )
        # below parameters were tested on a 1280x800 monitor
        # relative sizes are later calculated in get_resolution()
        self.referenceGroundLevel= 350/800
        self.referenceBlockSize = 25/800
        self.referencePaddingLeft = 60/1280     # padding of bird from left screen
        self.referenceScreenWidth = 260/1280    # width of playable device screen
        self.referenceScreenHeight = 500/800    # height of playable device screen
        self.referenceScreenTop = 145/800       # distance in px from 0,0 to playable screen top
        # initialise functions
        self.get_resolution()
        # self.connect()

        def initialise_grid():
            # create zeros grid of values for colours
            self.gridBird = np.zeros([20,1])
            self.gridBlocks = np.zeros([20,7])


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
        # get ground colours before beginning to ensure no change in scenery
        self.screenshot()
        lower=[255,255,255]
        upper=[0,0,0]
        # check from ground level datum to two blocks below datum
        for i in range(int(self.groundLevel), int(self.groundLevel + 2*self.blockSize)):
            r,g,b = self.rgb[i,50]
            # check red
            if r < lower[0]:
                lower[0] = r
            if r > upper[0]:
                upper[0] = r
            # check green
            if g < lower[1]:
                lower[1] = g
            if g > upper[1]:
                upper[1] = g
            # check blue
            if b < lower[2]:
                lower[2] = b
            if b > upper[2]:
                upper[2] = b
        self.boundaryBlockLower = lower
        self.boundaryBlockUpper = upper
        # press begin
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
        # take screenshot of just the phone screen
        # assuming Apowermirror screen is far left of screen
        with mss.mss() as sct:
            monitor = {"top": self.screenTop, "left": 0, "width": self.screenWidth, "height": self.screenHeight}
            self.rgb = np.array(pil_frombytes(sct.grab(monitor)))

    def update(self):
        complete = False
        while not complete == True:
            current_time = time.time()
            self.check_grid()
        #     time.sleep(time.time()-current_time)

        def check_grid(self):
            # 1 block per screen width for bird block
            # 7 blocks per screen width
            # 20 blocks per screen height
            # only need to consider blocks right of bird (60px/1280px left padding)
            # monitor centre point of grid x-axis, bottom 10% on y-xaxis
            self.screenshot()

        def check_bird_column(self):
            # bird's R and G values are both above 250, use that as verification for column
            # using 40% of width as dead centre is bird's nose
            self.coordX = self.paddingLeft + self.blockSize*0.4
            coordY = self.blockSize/2
            # for i in range(len(self.gridBird[0:])):
            

# function to convert mss screenshot in BGRA to standard RGB
def pil_frombytes(im):
    return Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX')

# function to convert RGB value into single float
def rgb2single(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])


if __name__ == '__main__':
    game = StackyBird()