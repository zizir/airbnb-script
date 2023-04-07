import os
import csv
import codecs
import datetime
import time

if __name__ == "__main__":
    BHI_ = 'BHI-reservation-upcoming.csv'
    DSIS_ = 'DSIS-reservation-upcoming.csv'
    LBO_ = 'LBO-reservation-upcoming.csv'
    csv_files = [BHI_, DSIS_, LBO_]
    filesPath = './04-03-2023'    # 文件所在相对路径
    rooms_sum = []  # 需要打扫的房间

    # 获取csv 字符
    for csv_f in csv_files:
        check_out_ = []  # 汇总 check out
        rooms_ = []      # 汇总 rooms
        with codecs.open(os.path.join(filesPath, csv_f), encoding='utf-8') as f:
            reader = csv.DictReader(f, skipinitialspace=True)   # reader
            for line in reader:
                check_out_.append(line['check out'])    # 获取check out信息
                rooms_.append(line['room'])             # 获取room信息. 通过count将两数组联系起来

        # 对比时间戳，7天内
        today_ = datetime.date.today()  # 当天日期

        # print(time.strftime("%Y-%m-%d %X", time.localtime()))
        # time.gmtime
        # time.localtime()
        # time.asctime()
        # print(datetime.utcnow())
        # print(datetime.utcnow().replace(tzinfo=timezone.utc))

        count = 0   # 标记数组索引
        for i in check_out_:
            # i.split(",")[0].split(" ")[0]    # month
            # i.split(",")[0].split(" ")[1]    # day
            # i.split(",")[1].strip(" ")       # year
        
            if i.split(",")[0].split(" ")[0] == "Jan":  # 1月
                if int(today_.month) == 1 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "Feb":  # 2月
                if int(today_.month) == 2 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "Mar":  # 3月
                if int(today_.month) == 3 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "Apr":  # 4月
                if int(today_.month) == 4 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "May":  # 5月
                if int(today_.month) == 5 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "Jun":  # 6月
                if int(today_.month) == 6 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "Jul":  # 7月
                if int(today_.month) == 7 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "Aug":  # 8月
                if int(today_.month) == 8 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "Sep":  # 9月
                if int(today_.month) == 9 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "Oct":  # 10月
                if int(today_.month) == 10 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "Nov":  # 11月
                if int(today_.month) == 11 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            if i.split(",")[0].split(" ")[0] == "Dec":  # 12月
                if int(today_.month) == 12 and int(i.split(",")[0].split(" ")[1]) == int(today_.day):  # month 与 day相同
                    rooms_sum.append(csv_f.replace("-reservation-upcoming.csv", "-") + rooms_[count])
            count += 1

    # 写入csv文件
    print(rooms_sum)
    header = ['Rooms to be cleaned today']
    file_name = str(today_) + ".csv"
    with open(file_name, 'w', encoding='utf-8') as f:
        # 1:创建writer对象
        writer = csv.writer(f)
        # 2:写表头
        writer.writerow(header)
        # 3:遍历列表，将每一行的数据写入csv
        for room in rooms_sum:
            print(room)
            writer.writerow(room)



