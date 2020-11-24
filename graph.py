from data import *
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates



font = {'family': 'momospace',
        'color':  '#F9C4C9',
        'weight': 'normal',
        'size': 25,
        }


time_period = ["0-1", "1-2", "2-3", "3-4","4-5", "5-6", "6-7", "7-8", "8-9", "9-10", "10-11", "11-12", "12-13",
                "13-14", "14-15", "15-16", "16-17", "17-18", "18-19", "19-20", "20-21", "21-22", "22-23", "23-24"]

day_period = ["Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


# x_overtime = [datetime.strptime(d, '%d-%m-%Y') for d in day_overtime]
# ax = plt.gca()
# formatter = mdates.DateFormatter("%Y-%m-%d")
# ax.xaxis.set_major_formatter(formatter)
# locator = mdates.DayLocator(interval=10)
# ax.xaxis.set_major_locator(locator)
# plt.plot(x_overtime, text_overtime, color= '#F06162')
# plt.title('Phân bố tin nhắn theo thời gian', fontdict= font)

# labels = 'Chrysane:\n ' +str(huong_msg_amount), '_datvt:\n ' + str(dat_msg_amount)
# size = [huong_msg_amount, dat_msg_amount]


# fig1, ax1 = plt.subplots()
# ax1.pie(size,  labels=labels, startangle=90, autopct = '%1.1f%%' , colors= ['#F9C4C9', '#F68F5F'])
# ax1.axis('equal') 



# p1 = plt.bar(day_period, dat_day_distribution,width=0.5, color= '#F68F5F')
# p2 = plt.bar(day_period, huong_day_distribution, width= 0.5, color='#F9C4C9', bottom=dat_day_distribution)




plt.plot(time_period,time_maxday_distribution_local, color='#F68F5F' )
plt.title('Phân bố tin nhắn ngày nhiều nhất', fontdict= font)


plt.show()
 
