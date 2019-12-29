import struct
import time
import socket
import ParameterConfig as ParamCig
from ReadConfig import *
# 组播组IP和端口
import binascii
from AnalyticalMethods import *
from SendData import *
from ReadNetConfig import *
import socket, select, time

from DataConvert import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#mcast_group_ip = '238.1.0.2'  #105
#mcast_group_ip = '238.1.0.100'  #102
#mcast_group_port = 50001

"""
    数据接收函数
"""
def receiver(config32,congif512,mcast_group_ip,mcast_group_port,dst_ip,dst_port1,dst_port2,dst_port3):
    # 建立接收socket，和正常UDP数据包没区别
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # 获取本地IP地址
    local_ip = socket.gethostbyname(socket.gethostname())
    # 监听端口，已测试过其实可以直接bind 0.0.0.0；但注意不要bind 127.0.0.1不然其他机器发的组播包就收不到了
    sock.bind((local_ip, mcast_group_port))
    # 加入组播组
    mreq = struct.pack("=4sl", socket.inet_aton(mcast_group_ip), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    #SegmentLength = 612  #105
    SegmentLength = 1034  #102

    while True:
        try:
            message, addr = sock.recvfrom(4096)
            # 去包头
            data = message[20:]
            SegmentCount = len(data) / SegmentLength
            paralist512 = []
            paralist32 = []
            paralist32_bit = []
            for i in range(int(SegmentCount)):
                SegmentHeadData = data[i * SegmentLength:SegmentLength * (i + 1)]  #    切分segment
                SegmentData = SegmentHeadData[12:]
                value10 = 0
                for Param512Config in config512:
                    #value = SegmentData[((int(Param512Config.StartWord) - 2) * 2 + 1):((int(Param512Config.EndWord)-1) * 2 + 1)]
                    value = SegmentData[
                            ((int(Param512Config.StartWord) - 1) * 2):((int(Param512Config.EndWord) - 1) * 2 + 2)]
                    #value_s = value.decode('utf8','ignore')

                    value = binascii.b2a_hex(value)
                    data_bin = hex2bin(value,int(Param512Config.EndWord)-int(Param512Config.StartWord)+1)
                    #print(data_bin)
                    #print((int(Param512Config.Lsb)))
                    #print(int(Param512Config.Msb))
                    data = data_bin[int(Param512Config.Lsb)-1:int(Param512Config.Msb)]#.zfill(16)
                    #print(Param512Config.Lsb)
                    #print(Param512Config.Msb)
                    #print(len(data))
                    #data = data_bin[0:]
                   # print(data)
                    value_hex = bin2hex(data)
                    #print(len(value_hex))


                    if Param512Config.DataType == "Unsigned Binary":
                        if len(data) != 1:
                            value_dec = hex_to_ubnr(value_hex)
                        else:
                            print(value_hex)
                            #value_dec = hex2dec(value_hex) #ue_hex)
                        value_dec_end = value_dec * float(Param512Config.LsbRes) + float(Param512Config.Bias)
                    dict512 = {Param512Config.ParameterName:value_dec_end}
                    paralist512.append(dict512)
                #发送数据
                SendData512 = ""
                for dict_data in paralist512:
                    for key,value in dict_data.items():
                        SendData512 = SendData512 + "PCM Data:" + str(key) + "#" + str(value) + ","
                SendData512 = SendData512[0:-1]
                ###########
                print(SendData512)

                #sock.sendto(SendData512,9999)
                #sender(SendData512,"192.168.0.131",9999)
                sender(SendData512, dst_ip, dst_port1)
                paralist512.clear()

                for Param32Config in config32:
                    if hex(SegmentData[1]) == hex(int(Param32Config.InitialFrame)-1):  #SFID验证
                       #获取数据
                        value_raw1 = SegmentData[((int(Param32Config.StartWord) - 1) * 2):((int(Param32Config.EndWord) - 1) * 2 + 2)]
                        print("hhhhhhhhhhhhhhhhhkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

                        paradata = binascii.b2a_hex(value_raw1)
                        print(paradata)
                        data_bin = hex2bin(paradata, int(Param32Config.EndWord) - int(Param32Config.StartWord) + 1)
                        data = data_bin[int(Param32Config.Lsb) - 1:int(Param32Config.Msb)]  # .zfill(16)
                        value_hex32 = bin2hex(data)

                        #print("fffffffffffffffffffff")

                        if Param32Config.DataType == "FLOAT":
                            print(hex(SegmentData[1]))
                            #global paralist32[]
                            #print("uuuuuuuuuuuuuuuuuuuu")
                            #value_dec1 = hex_to_float(paradata)
                            value_dec1 = hex_to_float(value_hex32)
                            # dict32 = {Param32Config.ParameterName: value_dec1}
                            # paralist32.append(dict32)
                            print(paralist32)

                        # if Param32Config.DataType == "Unsigned Binary":
                        #     print(paralist32)
                        #     #global paralist32
                        #     #value_dec = int(value, 16)
                        #     value_dec = int(value_hex32)
                        #     value_dec1 = value_dec * float(Param32Config.LsbRes) + float(Param32Config.Bias)
                        #     print("hello iiiiiiiiiii")
                        #     print(hex(SegmentData[1]))
                        #     dict32 = {Param32Config.ParameterName: value_dec1}
                        #     paralist32.append(dict32)
                        #     #print(paralist32)
                        #     #flag = 1

                        dict32 = {Param32Config.ParameterName:value_dec1}
                        paralist32.append(dict32)
                #发送数据
                SendData32 = ""
                for dict_data in paralist32:
                     for key,value in dict_data.items():
                         SendData32 = SendData32 + "PCM Data:" + str(key) + "#" + str(value) + ","
                SendData32 = SendData32[0:-1]
                #############
                print(SendData32)
                #sender(SendData32,"192.168.0.131", 9998)
                sender(SendData32, dst_ip, dst_port2)
                #sender(SendData32)
                paralist32.clear()

                for Param32Config in config32_bit:
                    if hex(SegmentData[1]) == hex(int(Param32Config.InitialFrame)-1):  #SFID验证
                       #获取数据
                        value_raw1 = SegmentData[((int(Param32Config.StartWord) - 1) * 2):((int(Param32Config.EndWord) - 1) * 2 + 2)]
                        print("hhhhhhhhhhhhhhhhhkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

                        paradata = binascii.b2a_hex(value_raw1)
                        print(paradata)
                        data_bin = hex2bin(paradata, int(Param32Config.EndWord) - int(Param32Config.StartWord) + 1)
                        data = data_bin[int(Param32Config.Lsb) - 1:int(Param32Config.Msb)]  # .zfill(16)

                        value_hex32 = bin2hex(data)

                        if Param32Config.DataType == "Unsigned Binary":
                            print(paralist32)
                            #global paralist32
                            #value_dec = int(value, 16)
                            value_dec = int(value_hex32)
                            value_dec1 = value_dec * float(Param32Config.LsbRes) + float(Param32Config.Bias)
                            print("hello iiiiiiiiiii")
                            print(hex(SegmentData[1]))
                            #dict32 = {Param32Config.ParameterName: value_dec1}
                            #paralist32.append(dict32)
                            #print(paralist32)
                            #flag = 1

                        dict32 = {Param32Config.ParameterName:value_dec1}
                        paralist32.append(dict32)
                #发送数据
                SendData32 = ""
                for dict_data in paralist32:
                     for key,value in dict_data.items():
                         SendData32 = SendData32 + "PCM Data:" + str(key) + "#" + str(value) + ","
                SendData32 = SendData32[0:-1]
                #############
                print(SendData32)
                #sender(SendData32,"192.168.0.131", 9998)
                sender(SendData32, dst_ip, dst_port3)
                #sender(SendData32)
                paralist32.clear()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    config = Getconfig()
    config32 =  config[0:5]
    config32_bit = config[5:6]
    config512 = config[6:]
    config_net = ReadNetConfig(filepathname_net)
    receiver(config32,config512,config_net[0],int(config_net[1]),config_net[2],int(config_net[3]),int(config_net[4]),int(config_net[5]))





