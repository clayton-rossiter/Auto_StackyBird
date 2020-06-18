from ppadb.client import Client
import time
import mss

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
        self.stack = 125    # time in ms to add one stack
        self.connect()

    def connect(self):
        self.adb = Client(host=self.host, port=self.port)
        try:
            self.device = self.adb.devices()[0]
        except:
            print("Cannot connect to phone!")

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
        self.screenshot = mss()


if __name__ == '__main__':
    game = StackyBird()
    game.revive()
    game.hold(125)
    game.hold(250)
    game.hold(375)
        