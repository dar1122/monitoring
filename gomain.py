import goselect
import time
if __name__ == '__main__':
    print('欢迎使用火车票监控程序')
    x = input('请输入始发站：')
    y = input('请输入终点站：')
    z = input('请输入出发时间，格式为yyyy-mm-dd：')

    num = 0
    while (num == 0):
        num = goselect.se(x,y,z)
        if num == 0:
            print('此时无票，请等待，正为您监控')
        time.sleep(5)
