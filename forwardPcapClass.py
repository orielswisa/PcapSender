import argparse
from scapy.all import *
from time import sleep
import socket
from PyQt5 import QtCore, QtGui, QtWidgets,QtTest


def buildPacket(pkt):
    nPkt = IP(src = opt.srcip,dst = opt.dstip)/UDP(dport = int(opt.dstport))/Raw(pkt[Raw])
    return nPkt

def calculateTime(timesToSend):
    tempTimes = []
    for i in range(len(timesToSend)):
        timeToWait = 0
        if i != 0:
            timeToWait = timesToSend[i] - timesToSend[i-1]
        tempTimes.append(timeToWait)
    return tempTimes

def conditionOfConversation(pkt):
    if pkt.haslayer(UDP) and pkt.haslayer(IP):
        if opt.conv_srcport == '0':
            if pkt[IP].src == opt.srcconvip and pkt[IP].dst == opt.dstconvip and pkt[UDP].dport == int(opt.conv_dstport):
                return True
        else:
            if pkt[IP].src == opt.srcconvip and pkt[IP].dst == opt.dstconvip and pkt[UDP].dport == int(opt.conv_dstport) and pkt[UDP].sport == int(opt.conv_srcport):
                return True
    return False

def main():
    packets = []
    times= []
    all_sniffed = sniff(offline= opt.filename)
    for sniffed_pkt in all_sniffed:
        if conditionOfConversation(sniffed_pkt):
            packets.append(sniffed_pkt)
            times.append(sniffed_pkt.time)

    times = calculateTime(times) 
    i = 0
    for pkt in packets:
        if opt.srcport == '':
            srcport = RandShort()
        else:
            srcport = opt.srcport
        newPkt = buildPacket(pkt)    
        sleep(times[i])
        i += 1
        send(newPkt)
        # print (newPkt.summary())
        print (newPkt.show())





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str,default='TstarUpdated.pcap', help = 'pcap file name or location')
    parser.add_argument('--srcip', type=str,default='192.168.98.125', help = 'Source ip')
    parser.add_argument('--dstip', type=str,default='192.168.0.26', help = 'Destination ip')
    parser.add_argument('--srcconvip', type=str,default='1.1.32.250', help = 'Conversation source ip')
    parser.add_argument('--dstconvip', type=str,default='225.6.7.8', help = 'Conversation destination ip')
    parser.add_argument('--dstport', type=str,default='4444', help = 'Destination por')
    parser.add_argument('--srcport', type=str,default='3333', help = 'Source port')
    parser.add_argument('--conv_srcport', type=str,default='0', help = 'Conversation source port')
    parser.add_argument('--conv_dstport', type=str,default='5555', help = 'Conversation destination port')
    parser.add_argument('--protocol', type=str,default='udp', help = 'Send Protocol')



    opt = parser.parse_args()
    if opt.protocol.lower() == 'udp':
        opt.protocol = 'UDP'
    elif opt.protocol.lower() == 'tcp':
        opt.protocol = 'TCP'


    main()    
        
    
class Sender(object):

    def __init__(self,config_dict, object):
        parser = argparse.ArgumentParser()
        parser.add_argument('--filename', type=str,default=config_dict["filename"], help = 'pcap file name or location')
        parser.add_argument('--srcip', type=str,default=config_dict["srcip"], help = 'Source ip')
        parser.add_argument('--dstip', type=str,default=config_dict["dstip"], help = 'Destination ip')
        parser.add_argument('--srcconvip', type=str,default=config_dict["conv_srcip"], help = 'Conversation source ip')
        parser.add_argument('--dstconvip', type=str,default=config_dict["conv_dstip"], help = 'Conversation destination ip')
        parser.add_argument('--dstport', type=str,default=config_dict["dstport"], help = 'Destination por')
        parser.add_argument('--srcport', type=str,default=config_dict["srcport"], help = 'Source port')
        parser.add_argument('--conv_srcport', type=str,default=config_dict["conv_srcport"], help = 'Conversation source port')
        parser.add_argument('--conv_dstport', type=str,default=config_dict["conv_dstport"], help = 'Conversation destination port')
        parser.add_argument('--protocol', type=str,default=config_dict["protocol"], help = 'Send Protocol')
        
        self.opt = parser.parse_args()
        if self.opt.protocol.lower() == 'udp':
            self.opt.protocol = 'UDP'
        elif self.opt.protocol.lower() == 'tcp':
            self.opt.protocol = 'TCP'
        self.uiObject = object    
        self.uiObject.stopButton.clicked.connect(self.stopSending)
        self.stopFlag = False
        
        
    def stopSending(self):
        self.stopFlag = True
        self.uiObject.stopButton.setEnabled(False)
        self.time_left_int = 0
        try:
            self.uiObject.startButton.setEnabled(True)
            self.my_qtimer.stop()
            self.update_gui()
        except:
            pass
        self.uiObject.packetNumber_lable.setText(str(0))
        self.uiObject.packet_label.setText("Wait for sending..")
        
        
        
        
        
        
    def sendInLoop(self):
        i = 1
        while not self.stopFlag:
            self.sendPcap()
            print("Finish iterations:",i)
            i += 1

            
    def sendPcap(self):
        self.uiObject.startButton.setEnabled(False)
        self.packets = []
        self.times= []
        self.all_sniffed = sniff(offline= self.opt.filename)
        for sniffed_pkt in self.all_sniffed:
            if self.conditionOfConversation(sniffed_pkt):
                self.packets.append(sniffed_pkt)
                self.times.append(sniffed_pkt.time)

        self.times = self.calculateTime(self.times) 
        self.timer_start()
        self.update_gui()
        i = 0
        for pkt in self.packets:
            if self.stopFlag:
               break 
            if self.opt.srcport == '':
                srcport = RandShort()
            else:
                srcport = self.opt.srcport
            self.newPkt = self.buildPacket(pkt)    
            # sleep(self.times[i])
            t = self.times[i]*1000
            QtTest.QTest.qWait(t)
            i += 1
            self.uiObject.packetNumber_lable.setText(str(len(self.packets) - i))
            send(self.newPkt)
            toP = str(self.newPkt.summary())
            self.uiObject.packet_label.setText(toP)
        self.uiObject.startButton.setEnabled(True)
        

    def buildPacket(self,pkt):
        nPkt = IP(dst = self.opt.dstip)/UDP(sport= int(self.opt.srcport),dport = int(self.opt.dstport))/Raw(pkt[Raw])
        return nPkt

    def calculateTime(self,timesToSend):
        tempTimes = []
        for i in range(len(timesToSend)):
            timeToWait = 0
            if i != 0:
                timeToWait = timesToSend[i] - timesToSend[i-1]
            tempTimes.append(timeToWait)
        return tempTimes

    def conditionOfConversation(self,pkt):
        if pkt.haslayer(UDP) and pkt.haslayer(IP):
            if self.opt.conv_srcport == '0':
                if pkt[IP].src == self.opt.srcconvip and pkt[IP].dst == self.opt.dstconvip and pkt[UDP].dport == int(self.opt.conv_dstport):
                    return True
            else:
                if pkt[IP].src == self.opt.srcconvip and pkt[IP].dst == self.opt.dstconvip and pkt[UDP].dport == int(self.opt.conv_dstport) and pkt[UDP].sport == int(self.opt.conv_srcport):
                    return True
        return False


    def timer_start(self):
        self.time_left_int = int(sum(self.times))
        self.my_qtimer = QtCore.QTimer(self.uiObject)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)

        self.update_gui()

    def timer_timeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:
            self.my_qtimer.stop()

        self.update_gui()

    def update_gui(self):
        self.uiObject.time_lable.setText(str(self.time_left_int))    