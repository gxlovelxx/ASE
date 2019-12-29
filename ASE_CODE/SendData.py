import time
import socket

# 组播组IP和端口

#mcast_group_ip = '238.1.0.6'
mcast_group_ip = "127.0.0.1"
mcast_group_port = 40001

message = "this message send via mcast !"

# def sender(message):
#     # 建立发送socket，和正常UDP数据包没区别
#     send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#
#     # 每十秒发送一遍消息
#     while True:
#         # 发送写法和正常UDP数据包的还是完全没区别
#
#         # 猜测只可能是网卡自己在识别到目的ip是组播地址后，自动将目的mac地址设为多播mac地址
#
#         send_sock.sendto(message.encode(), (mcast_group_ip, mcast_group_port))
#
#         print(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: message send finish')
#
#         time.sleep(2)
def sender(message,mcast_group_ip, mcast_group_port):
    # 建立发送socket，和正常UDP数据包没区别
    #send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 发送写法和正常UDP数据包的还是完全没区别

    # 猜测只可能是网卡自己在识别到目的ip是组播地址后，自动将目的mac地址设为多播mac地址

    send_sock.sendto(message.encode("utf-8"), (mcast_group_ip, mcast_group_port))

    print(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: message send finish')

    #time.sleep(2)
if __name__ == "__main__":
    sender(message)
