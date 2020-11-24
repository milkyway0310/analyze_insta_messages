import json
import demoji
from datetime import datetime
from dateutil import tz
from collections import Counter



f = open("messages.json", encoding="utf8" )
data = json.loads(f.read())
huong = data[0]                                                      
chat = huong["conversation"]
len_chat = len(chat)                                                                                    #so luong tin nhan


all_key = []


total_msg_amount = 0
dat_msg_amount = 0
huong_msg_amount = 0   


time_distribution = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
time_oder =         [17,18,19,20,21,22,23,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


day_distribution = [0,0,0,0,0,0,0] 
dat_day_distribution = [0,0,0,0,0,0,0]
huong_day_distribution = [0,0,0,0,0,0,0]


time_maxday_distribution = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


text_amount = 1
max_text_amount =0
day_max_text = datetime.now()


text_overtime = []
text_amount_overtime = 1
day_overtime = []


text_string = ''


emoji_count ={}


  


local_zone = tz.tzlocal()
 



chat_max_day = []
 



for i in range(len_chat):
    key_list = list(chat[i].keys())                                                                    #list các key trong file
    for x in key_list:
        if x not in all_key:
                all_key.append(x)


for i in range(len_chat):
    if ('sender' in chat[i]):
        total_msg_amount +=1
        if (('story_share' in chat[i]) or ('video_call_action' in chat[i])):                           #tổng số tin nhắn
            total_msg_amount -=1


for i in range(len_chat):
    if ((chat[i]['sender']) == '_datvt'):                                                              #so tin nhan cua Dat                
        dat_msg_amount +=1
        if (('story_share' in chat[i]) or ('video_call_action' in chat[i])):
            dat_msg_amount -=1


for i in range(len_chat):
    if (chat[i]['sender']) == 'chrysane':                                                               #so tin nhan cua Huong
        huong_msg_amount +=1
        if (('story_share' in chat[i]) or ('video_call_action' in chat[i])):
            huong_msg_amount -=1


for i in range(len_chat):
    if ('sender' in chat[i]):
        time = chat[i]['created_at']                                                                    #phan bo tin nhan theo thoi gian trong ngay
        time_distribution[int(time[11:13])] +=1
        if (('story_share' in chat[i]) or ('video_call_action' in chat[i])):
            time_distribution[int(time[11:13])] -=1

time_distribution_local = [time_distribution[i] for i in time_oder]
   

for i in range(len_chat):
    date_time = datetime.fromisoformat(chat[i]['created_at'])
    local_datetime =date_time.astimezone(local_zone)
    date = local_datetime.date()                                                                         #phan bo tin nhan theo thoi gian trong tuan
    day = date.weekday()
    day_distribution[day] +=1
    if (('story_share' in chat[i]) or ('video_call_action' in chat[i])):
        day_distribution[day] -=1

for i in range(len_chat):
    date_time = datetime.fromisoformat(chat[i]['created_at'])
    local_datetime =date_time.astimezone(local_zone)
    date = local_datetime.date()                                                                    #phan bo tin nhan cua Huong theo thoi gian trong tuan
    day = date.weekday()
    if (chat[i]['sender']) == 'chrysane':
        huong_day_distribution[day] +=1
        if (('story_share' in chat[i]) or ('video_call_action' in chat[i])):
            huong_day_distribution[day] -=1

for i in range(len_chat):
    date_time = datetime.fromisoformat(chat[i]['created_at'])
    local_datetime =date_time.astimezone(local_zone)
    date = local_datetime.date()                                                                    #phan bo tin nhan cua Dat theo thoi gian trong tuan
    day = date.weekday()
    if (chat[i]['sender']) == '_datvt':
        dat_day_distribution[day] +=1
        if (('story_share' in chat[i]) or ('video_call_action' in chat[i])):
            dat_day_distribution[day] -=1


for i in range((len_chat-1)):
    date_time1 = datetime.fromisoformat(chat[i]['created_at'])
    date1 = date_time1.date()
    date_time2 = datetime.fromisoformat(chat[i+1]['created_at'])                                    #ngay va so tin nhan nhieu nhat
    date2 = date_time2.date()
    if (date1 == date2 ):
        text_amount +=1
    else:
        text_amount = 1
    if(text_amount > max_text_amount):
        max_text_amount = text_amount
        day_max_text = date1


for i in range(len_chat):
    date_time = datetime.fromisoformat(chat[i]['created_at'])                             
    date = date_time.date()
    if (date == day_max_text):
        chat_max_day.append(chat[i]['created_at'])                                              
                                                                                                     
for i in range(len(chat_max_day)):                                                                #phan bo ngay nt nhieu nhat
    time_max_day = int(chat_max_day[i][11:13])
    time_maxday_distribution[time_max_day] +=1
    time_maxday_distribution_local = [time_maxday_distribution[i] for i in time_oder]


for i in range((len_chat-1)):
    date_time3 = datetime.fromisoformat(chat[i]['created_at'])
    date3 = date_time3.date()
    date_time4 = datetime.fromisoformat(chat[i+1]['created_at'])                                #ngay va so tin nhan theo thoi gian
    date4 = date_time4.date()
    
    if (date3 == date4 ):
        text_amount_overtime +=1
        if (('story_share' in chat[i]) or ('video_call_action' in chat[i])):
            text_amount_overtime -=1
    else:
        text_overtime.append(text_amount_overtime)
        day_overtime.append(date3.strftime("%d-%m-%Y"))
        text_amount_overtime = 1


for i in range(len_chat):
    if ('text' in chat[i]):                                                                    #chuyen text ve string
        text_string += ' ' + str(chat[i]['text'])

text_split = Counter(text_string.split())

all_emoji = list(demoji.findall(text_string).keys())


for i in range(len(all_emoji)):
    emoji_count[all_emoji[i]] = text_string.count(all_emoji[i])

common_word = text_split.most_common(20)

# print(text_string.count('yêu em'))
# print(text_string.count('yêu anh'))

# print(all_key)
# print(time_distribution_local)
# print(day_distribution)
# print(dat_day_distribution)
# print(huong_day_distribution)
print(max_text_amount)
print(day_max_text)
# print(time_maxday_distribution_local)
# print(text_overtime)
# print(day_overtime)
# print(all_emoji)
# print(emoji_count)
# print(common_word)







