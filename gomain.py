import goselect
import time
if __name__ == '__main__':
    print('欢迎使用火车票监控程序')
    x = input('请输入始发站：')
    y = input('请输入终点站：')
    u = input('请输入要监控的座位-（全部，一等座，二等座，软卧，硬卧，硬座，无座）：')
    z = input('请输入出发时间，格式为yyyy-mm-dd：')

    tri = goselect.trains_info(x, y, z)
    if u == '全部':

        num = 0
        while (num == 0):
            num = goselect.all_seat(tri)
            if num == 0:
                print('此时无票，请等待，正为您监控')
            time.sleep(1)

    elif u == '一等座':
        num = 0
        while (num == 0):
            num = goselect.first_seat(tri)
            if num == 0:
                print('此时无票，请等待，正为您监控')
            time.sleep(5)
    elif u == '二等座':
        num = 0
        while (num == 0):
            num = goselect.second_seat(tri)
            if num == 0:
                print('此时无票，请等待，正为您监控')
            time.sleep(5)
    elif u == '软卧':
        num = 0
        while (num == 0):
            num = goselect.soft(tri)
            if num == 0:
                print('此时无票，请等待，正为您监控')
            time.sleep(5)
    elif u == '硬卧':
        num = 0
        while (num == 0):
            num = goselect.hardseat(tri)
            if num == 0:
                print('此时无票，请等待，正为您监控')
            time.sleep(5)
    elif u == '硬座':
        num = 0
        while (num == 0):
            num = goselect.seat(tri)
            if num == 0:
                print('此时无票，请等待，正为您监控')
            time.sleep(5)
    elif u == '无座':
        num = 0
        while (num == 0):
            num = goselect.noseat(tri)
            if num == 0:
                print('此时无票，请等待，正为您监控')
            time.sleep(5)