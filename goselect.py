

#coding=utf-8
import requests
import stations1
import json

allstations = stations1.a

allstations_1 = {v: k for k, v in allstations.items()}

def if_exit(a):
        if (a=='')|(a=='无')|(a==0):
            return 0
        elif a=='有':
            return 1
        else:
            return 1



def trains_info(a,b,c):


        start = a
        from_station = allstations.get(start)

        end = b
        to_station = allstations.get(end)

        search_date = c
        date = search_date


        url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(date,from_station,to_station)


        r = requests.get(url, verify=False)


        trains = r.json()['data']['result']

        return trains

def all_seat(trains):

        first = 0

        for raw_train in trains:
            # 循环遍历每辆列车的信息
            data_list = raw_train.split('|')

            # 车次号码
            train_no = data_list[3]
            # 出发站
            from_station_code = data_list[6]
            from_station_name = allstations_1.get(from_station_code)

            # 终点站
            to_station_code = data_list[7]
            to_station_name = allstations_1.get(to_station_code)

            # 一等座
            first_class_seat = data_list[31] or 0
            # 二等座
            second_class_seat = data_list[30] or 0
            # 软卧
            soft_sleep = data_list[23] or 0
            # 硬卧
            hard_sleep = data_list[28] or 0
            # 硬座
            hard_seat = data_list[29] or 0
            # 无座
            no_seat = data_list[26] or 0

            x = if_exit(first_class_seat) + if_exit(second_class_seat) + if_exit(soft_sleep) + if_exit(hard_seat) + if_exit(hard_sleep) + if_exit(no_seat)

            first += x
            if x != 0:
                print('{}车次有票  {}--{}   一等座[{}]张    二等座[{}]张    软卧[{}]张    硬卧[{}]张    硬座[{}]张     无座[{}]张'.format(train_no,from_station_name,to_station_name,first_class_seat,second_class_seat,soft_sleep,hard_sleep,hard_seat,no_seat))
        return first

def first_seat(trains):

    first = 0
    for raw_train in trains:
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')

        # 车次号码
        train_no = data_list[3]
        # 出发站
        from_station_code = data_list[6]
        from_station_name = allstations_1.get(from_station_code)

        # 终点站
        to_station_code = data_list[7]
        to_station_name = allstations_1.get(to_station_code)

        # 一等座
        first_class_seat = data_list[31] or 0

        x = if_exit(first_class_seat)
        if x != 0:
            print("{}车次有座位  {}-{}  一等座{}张".format(train_no,from_station_name,to_station_name,first_class_seat))
        first += x
    return first

def second_seat(trains):

    first = 0
    for raw_train in trains:
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')

        # 车次号码
        train_no = data_list[3]
        # 出发站
        from_station_code = data_list[6]
        from_station_name = allstations_1.get(from_station_code)

        # 终点站
        to_station_code = data_list[7]
        to_station_name = allstations_1.get(to_station_code)



        # 二等座
        second_class_seat = data_list[30] or 0

        x = if_exit(second_class_seat)
        if x != 0:
            print("{}车次有座位  {}-{}  二等座{}张".format(train_no,from_station_name,to_station_name,second_class_seat))
        first += x
    return first
    



def soft(trains):
    first = 0
    for raw_train in trains:
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')

        # 车次号码
        train_no = data_list[3]
        # 出发站
        from_station_code = data_list[6]
        from_station_name = allstations_1.get(from_station_code)

        # 终点站
        to_station_code = data_list[7]
        to_station_name = allstations_1.get(to_station_code)
        # 软卧
        soft_sleep = data_list[23] or 0

        x = if_exit(soft_sleep)
        if x != 0:
            print("{}车次有座位  {}-{}  软卧{}张".format(train_no, from_station_name, to_station_name, soft_sleep))
        first += x
    return first


def hardseat(trains):
    first = 0
    for raw_train in trains:
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')

        # 车次号码
        train_no = data_list[3]
        # 出发站
        from_station_code = data_list[6]
        from_station_name = allstations_1.get(from_station_code)

        # 终点站
        to_station_code = data_list[7]
        to_station_name = allstations_1.get(to_station_code)
        # 硬卧
        hard_sleep = data_list[28] or 0

        x = if_exit(hard_sleep)
        if x != 0:
            print("{}车次有座位  {}-{}  硬卧{}张".format(train_no, from_station_name, to_station_name, hard_sleep))
        first += x
    return first



def seat(trains):
    first = 0
    for raw_train in trains:
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')

        # 车次号码
        train_no = data_list[3]
        # 出发站
        from_station_code = data_list[6]
        from_station_name = allstations_1.get(from_station_code)

        # 终点站
        to_station_code = data_list[7]
        to_station_name = allstations_1.get(to_station_code)
        # 硬座
        hard_seat = data_list[29] or 0

        x = if_exit(hard_seat)
        if x != 0:
            print("{}车次有座位  {}-{}  硬座{}张".format(train_no, from_station_name, to_station_name, hard_seat))
        first += x
    return first



def noseat(trains):
    first = 0
    for raw_train in trains:
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')

        # 车次号码
        train_no = data_list[3]
        # 出发站
        from_station_code = data_list[6]
        from_station_name = allstations_1.get(from_station_code)

        # 终点站
        to_station_code = data_list[7]
        to_station_name = allstations_1.get(to_station_code)
        # 无座
        no_seat = data_list[26] or 0

        x = if_exit(no_seat)
        if x != 0:
            print("{}车次有座位  {}-{}  无座{}张".format(train_no, from_station_name, to_station_name, no_seat))
        first += x
    return first



    