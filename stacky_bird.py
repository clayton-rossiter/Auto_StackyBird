from ppadb.client import Client
import time

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
        self.stack = 125    # time in ms to add one stack
        self.connect()

    def connect(self):
        self.adb = Client(host=self.host, port=self.port)
        try:
            self.device = self.adb.devices()[0]
        except:
            print("Cannot connect to phone!")

    def start(self):
        command = 'input tap {} {}'.format(self.startx, self.starty)
        print(command)
        self.device.shell(command)


    def revive(self):
        command = 'input tap {} {}'.format(self.revivex, self.revivey)
        print(command)
        self.device.shell(command)
        time.sleep(3)
        self.start()

    def tap(self, x, y):
        command = 'input tap {} {}'.format(x,y)
        print(command)
        self.device.shell(command)
        print("tapped")

    def hold(self, duration):
        command = 'input swipe {} {} {} {} {}'.format(self.holdx,self.holdy,self.holdx,self.holdy,duration)
        self.device.shell(command)
        print('Screen held for {} ms'.format(duration))

if __name__ == '__main__':
    samsung = StackyBird()
    print (samsung.device)
    samsung.revive()
    samsung.hold(125)
    samsung.hold(250)
    samsung.hold(375)
        