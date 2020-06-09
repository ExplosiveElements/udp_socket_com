"""
一。功能
 1，发送功能
 2，接收功能
 3，退出程序

 二，框架的设计
 1，发送信息 send_msg()
 2,接收的信息 recv_msg()
 3,程序的主入口 main
 4，程序对立运行的时候，才启动聊天器
 三，实行步骤
 1，发送信息send_msg()
 1)，定义变量接收用户与输入的接收方的IP地址
 2），定义变量接收用户与输入的接收方的端口
 3），定义变量接收用户与输入的接收方的内容
 4），使用socket的sendto（） 发送信息

 2，接收信息 recv_msg()
 1)使用socket接收数据
 2）解码数据
 3）输出显示

 3主入口
 1）创建套接字
 2）绑定端口
 3）打印菜单（循环）
 4）接收用户的输入选项
 5）判断用户的选择，并调用对应的函数
 6）关闭套接字
"""

import socket


def send_msg(udp_socket):
    """发送信息的函数"""
    # 1)，定义变量接收用户与输入的接收方的IP地址
    ipaddr = input("请输入接收方的ip地址：\n")
    # 判断是否需要默认
    if len(ipaddr)==0:
        ipaddr = "192.168.88.1"
        print("当前默认接受方的ip地址【%s】" % ipaddr)
    # 2），定义变量接收用户与输入的接收方的端口
    port = input("请输入要发送的端口号：\n")
    if len(port)==0:
        port = "8081"
        print("当前默认接受方的端口号【%s】" % port)
    # 3），定义变量接收用户与输入的接收方的内容
    temp = ""
    for i in range(1, 100):
        temp = temp + "%d," % i
    temp = temp + "100"
    cotent = temp
    print(cotent)
    # 4），使用socket的sendto（） 发送信息
    udp_socket.sendto(cotent.encode(), (ipaddr, int(port)))


def recv_msg(udp_socket):
    """接收信息的函数"""
    # 1)使用socket接收数据
    recv_data, ip_port = udp_socket.recvfrom(1024)
    # 2）解码数据
    recv_text = recv_data.decode()
    recv_list = recv_text.split(',')
    # 3）输出显示
    print("接受到【%s】的消息："%str(ip_port))
    for i in recv_list:
        print(i,end=' ')


def main():
    """程序的主入口"""
    # 1）创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2）绑定端口
    # address --> (“IP地址”，8080)
    # udp_sockeet.bind(adress)
    udp_socket.bind(("", 8080))
    while True:
        # 3）打印菜单（循环）
        print("this is A")
        print("1,发送信息")
        print("2,接收信息")
        print("3,关闭程序")
        # 4）接收用户的输入选项
        sel_num = int(input("请输入选项：\n"))
        # 5）判断用户的选择，并调用对应的函数
        if sel_num == 1:
            # 调用发送信息的函数
            send_msg(udp_socket)
        elif sel_num == 2:
            recv_msg(udp_socket)
        elif sel_num == 3:
            print("系统正在退出。。。")
            print("系统退出完成！")
            break
    # 6）关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    # 程序独立运行的时候才被调用
    main()