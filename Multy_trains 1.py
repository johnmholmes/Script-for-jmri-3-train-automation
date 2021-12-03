import java
import jmri

class Main(jmri.jmrit.automat.AbstractAutomaton):
    def init(self):
        print "Inside init(self)"
        return

    def setup(self, dccAddr):
        self.dccAddr = dccAddr
        # set up all sensor numbers on complete layout may not be called in this script though

        self.s1 = sensors.provideSensor("CS1001")
        self.s2 = sensors.provideSensor("CS1002")
        self.s3 = sensors.provideSensor("CS1003")
        self.s4 = sensors.provideSensor("CS1004")
        self.s5 = sensors.provideSensor("CS1005")
        self.s6 = sensors.provideSensor("CS1006")
        self.s7 = sensors.provideSensor("CS1007")
        self.s8 = sensors.provideSensor("CS1008")
        self.s9 = sensors.provideSensor("CS1009")
        self.s10 = sensors.provideSensor("CS1010")
        self.s11 = sensors.provideSensor("CS1011")
        self.s12 = sensors.provideSensor("CS1012")
        self.s13 = sensors.provideSensor("CS1013")
        self.s14 = sensors.provideSensor("CS1014")
        self.s15 = sensors.provideSensor("CS1015")
        self.s16 = sensors.provideSensor("CS1016")
        self.s17 = sensors.provideSensor("CS1017")
        self.s18 = sensors.provideSensor("CS1018")
        self.s19 = sensors.provideSensor("CS1019")
        self.s20 = sensors.provideSensor("CS1020")
        self.s21 = sensors.provideSensor("CS1021")
        self.s22 = sensors.provideSensor("CS1022")
        self.s23 = sensors.provideSensor("CS1023")
        self.s24 = sensors.provideSensor("CS1024")
        self.s25 = sensors.provideSensor("CS1025")
        self.s26 = sensors.provideSensor("CS1026")
        self.s27 = sensors.provideSensor("CS1027")
        self.s28 = sensors.provideSensor("CS1028")
        self.s29 = sensors.provideSensor("CS1029")
        self.s30 = sensors.provideSensor("CS1030")
        self.s31 = sensors.provideSensor("CS1031")
        self.s32 = sensors.provideSensor("CS1032")
        self.s33 = sensors.provideSensor("CS1033")
        self.s34 = sensors.provideSensor("CS1034")
        self.s35 = sensors.provideSensor("CS1035")
        self.s36 = sensors.provideSensor("CS1036")
        self.s37 = sensors.provideSensor("CS1037")
        self.s38 = sensors.provideSensor("CS1038")
        self.s39 = sensors.provideSensor("CS1039")
        self.s40 = sensors.provideSensor("CS1040")

        self.throttle4 = self.getThrottle(4, False)  # british rail jinty
        self.throttle6 = self.getThrottle(6, False)  # flying scotsman
        self.throttle7 = self.getThrottle(7, False)  # gwr j50 shunter 
        self.r3 = sensors.provideSensor("IS3")#peel 1 to central 2
        self.r6 = sensors.provideSensor("IS6")#peel 1 to port erin 1
        self.r15 = sensors.provideSensor("IS15")#dockland 1 to dock siding 
        self.r17 = sensors.provideSensor("IS17")#dockland 1 to peel 2

        return

    def handle(self):
        print "handle"
        if self.getName() == 'Train A':
            self.trainA()
        elif self.getName() == 'Train B':
            self.trainB()
        elif self.getName() == 'Train C':
            self.trainC()
        stopSensor = sensors.getSensor('CS1001')# this seems to keep the program active until the sensor goes inactive
        self.waitSensorInactive(stopSensor)
        return False #change to true to run continuosly

    def trainA(self):
        print "trainA", self.dccAddr
        self.r6.setState(ACTIVE)#setting route peel 1 to port erin 1
        self.waitMsec(1000)
        self.throttle6.setF1(True)     # turn on sound for flying scotsman
        self.waitMsec(1000)           # wait for 1 seconds
        self.throttle6.setF3(True)     # turn on whistle
        self.waitMsec(1000)           # wait for 1 seconds
        self.throttle6.setF3(False)    # turn off whistle
        self.waitMsec(200)
        self.throttle6.setIsForward(True)
        self.waitMsec(500)
        self.throttle6.setSpeedSetting(0.22)
        self.waitSensorActive(self.s16)#sensor 16 reading accelerate
        self.throttle6.setSpeedSetting(0.40)
        self.waitSensorActive(self.s33)#sensor 33 reading decelerate
        self.throttle6.setSpeedSetting(0.18)
        self.waitSensorActive(self.s38)#sensor 38 reading stop
        self.throttle6.setSpeedSetting(0)
        self.throttle6.setF7(True)     # turn on whistle
        self.waitMsec(10000)
        self.throttle6.setF7(False)     # turn on whistle
        self.throttle6.setF3(True)     # turn on whistle
        self.waitMsec(1000)           # wait for 1 seconds
        self.throttle6.setF3(False)    # turn off whistle
        self.throttle6.setSpeedSetting(0.35)
        self.waitSensorActive(self.s28)#sensor 28 reading decelerate
        #self.throttle6.setF3(True)    # turn on whistle whistle
        self.throttle6.setSpeedSetting(0.25)
        #self.waitMsec(50)
        #self.throttle6.setF3(False) 
        self.waitSensorActive(self.s26)#sensor 26 reading decelerate
        self.throttle6.setSpeedSetting(0.20)
        self.waitSensorActive(self.s24)#sensor 24 reading decelerate
        self.throttle6.setSpeedSetting(0)
        self.r6.setState(INACTIVE)#setting route peel 1 to port erin 1
        self.waitMsec(1000)
        self.throttle6.setF1(False)     # turn on sound for flying scotsman
 
        print "Loop A Finished"

    def trainB(self):#j50 lner tank engine
        print "trainB", self.dccAddr
        self.waitSensorActive(self.s38)#sensor 38 flying scotsman trigger
        self.waitMsec(1000)
        self.r3.setState(ACTIVE)#setting route 
        self.waitMsec(1000)
        self.throttle7.setIsForward(True)
        self.waitMsec(1000)
        self.throttle7.setSpeedSetting(0.45)
        self.waitSensorActive(self.s17)#sensor 17 reading decelerate
        self.throttle7.setSpeedSetting(0.35)
        self.waitSensorActive(self.s16)#sensor 16 reading decelerate
        self.throttle7.setSpeedSetting(0.20)
        self.waitSensorActive(self.s14)#sensor 16 reading stop
        self.throttle7.setSpeedSetting(0)
        self.r3.setState(INACTIVE)#setting route 
        self.waitMsec(3000)
        print "Loop B finished"

    def trainC(self):# Jinty 0-6-0 british rail
        print "trainC", self.dccAddr
        # first part of journey 
        self.waitMsec(2000)
        self.r15.setState(ACTIVE)#setting route dock siding to dockland 1
        self.waitMsec(2000)
        self.throttle4.setIsForward(True)
        self.waitMsec(1000)
        self.throttle4.setSpeedSetting(0.65)
        self.waitSensorActive(self.s3)#sensor 3 decelerate
        self.throttle4.setSpeedSetting(0.35)
        self.waitSensorActive(self.s1)#sensor 3 decelerate
        self.throttle4.setSpeedSetting(0)
        
        #second part of journey        
        self.r15.setState(INACTIVE)#setting route dock siding to dockland 1
        self.waitSensorActive(self.s14)#sensor set route for peel station platform 2
        self.r17.setState(ACTIVE)
        self.waitMsec(1000)
        self.throttle4.setIsForward(False)
        self.waitMsec(1000)
        self.throttle4.setSpeedSetting(0.60)
        self.waitSensorActive(self.s17)#sensor 17 reading decelerate
        self.throttle4.setSpeedSetting(0.50)
        self.waitSensorActive(self.s15)#sensor 15 reading decelerate
        self.throttle4.setSpeedSetting(0.40)
        self.waitSensorActive(self.s13)#sensor 13 reading decelerate
        self.throttle4.setSpeedSetting(0)
        self.r17.setState(INACTIVE)
        self.waitMsec(60000)

        return 0  

        
        print "Loop C finished"
        print "All Scripts finished"

ta = Main()
ta.setName('Train A')
ta.setup(6)
ta.start()

tb = Main()
tb.setName('Train B')
tb.setup(7)
tb.start()

tc = Main()
tc.setName('Train C')
tc.setup(4)
tc.start()


