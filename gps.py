import serial

class GPS:
    def __init__(self, port, baud, timeout):
        
        self.latitiude = 0
        self.latDirec = None
        self.latDegree = 0
        self.latFeet = 0

        self.longitude = 0
        self.longDirec = None
        self.longDegree = 0
        self.longFeet = 0

        self.speed = 0

        self.ser = serial.Serial( port , baud, timeout = timeout )

        while 1:
            self.updateGpsData(False)

    def updateGpsData(self, print_):
        line = self.ser.readline()
        splitline = line.split(',')

        if(splitline[0] == '$GPGGA'):
            self.latitiude = float(splitline[2])
            self.latDirec = splitline[3]
            self.latDegree = int(self.latitiude/100)
            self.latFeet = self.latitiude-(self.latDegree*100)

            self.longitude = float(splitline[4])
            self.longDirec = splitline[5]
            self.longDegree = int(self.longitude/100)
            self.longFeet = self.longitude-(self.longDegree*100)

            self.speed = splitline[8]

            if(print_):
                print("{} {} {} {} {} {}".format(self.latDegree, self.latFeet, self.latDirec, self.longDegree, self.longFeet, self.longDirec))


gps = GPS('/dev/ttyUSB0', 4800, 5)