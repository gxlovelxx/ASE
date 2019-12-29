import struct
import time
import socket
# 组播组IP和端口

mcast_group_ip = '238.1.0.6'
mcast_group_port = 40001


def receiver():
    # 建立接收socket，和正常UDP数据包没区别
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 获取本地IP地址
    local_ip = socket.gethostbyname(socket.gethostname())
    # 监听端口，已测试过其实可以直接bind 0.0.0.0；但注意不要bind 127.0.0.1不然其他机器发的组播包就收不到了
    sock.bind((local_ip, mcast_group_port))
    # 加入组播组
    mreq = struct.pack("=4sl", socket.inet_aton(mcast_group_ip), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # 允许端口复用，看到很多教程都有没想清楚意义是什么，我这里直接注释掉
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 设置非阻塞，看到很多教程都有也没想清楚有什么用，我这里直接注释掉
    # sock.setblocking(0)
    while True:
        try:
            #print("66666")
            message, addr = sock.recvfrom(4096)
            #print(message)
            print(
                 f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: Receive data from {addr}: {message.decode()}')
        except:
            print("while receive message error occur")

b=b'\xe9\x80\x86\xe7\x81\xab'
string=b.decode() # 第一参数默认utf8，第二参数默认strict
print(string)

ss = "11111ab4"
print(ss)
print(bin(int(ss,16)))
bb = bin(int(ss,16))
b32 = bb[2:].zfill(32)
print(b32)

# if __name__ == "__main__":
#     receiver()

def getbitdata(hex):
    print(444)