# from pushbullet import PushBullet

# API_KEY = 'o.cxjc9PaMuAClE2YkQt8YFWpTwwppDHv4'

# file = 'words.txt'

# lines =[]
# with open(file, 'r') as f:
#     lines.extend(f.readline() for i in range(3))
# abc = lines
# listToStr = ''.join([str(elem) for elem in abc])
# print(listToStr)
  
# # pb = PushBullet(API_KEY)
# # push = pb.push_note('Word of the Day', listToStr)

# press run print first 3, press run delete them , press run print next 3 

#from pushbullet import PushBullet

import schedule 
import time
from notify_run import Notify

#API_KEY = 'o.cxjc9PaMuAClE2YkQt8YFWpTwwppDHv4'
def wotd():
    file = 'words.txt'

    lines =[]
    with open(file, 'r+') as f:
        lines.extend(f.readline() for i in range(3))
        text = f.readlines()
        while True:
            f.seek(0)
            f.truncate()
            f.writelines(text[3:])
            break

    abc = lines
    listToStr = ''.join([str(elem) for elem in abc])
    print(listToStr)

    notify = Notify()
    notify.send('Word of the Day\n'+listToStr)

schedule.every().day.at('12:45').do(wotd)

while 1:
    schedule.run_pending()
    time.sleep(1)
  
# pb = PushBullet(API_KEY)
# push = pb.push_note('Word of the Day', listToStr)


'''procedural
Meaning - of or relating to processes
Sentence - In other words, the rejection was a bureaucratic/ procedural decision.



prognosticate
Meaning - make a prediction about; tell in advance
Sentence - How strange it is that our dreams often prognosticate coming events!



dwell
Meaning - think moodily or anxiously about something
Sentence - But it is hardly necessary to dwell on so normal an event.



retentive
Meaning - good at remembering
Sentence - The child was very sharp, and her memory was extremely retentive



nexus
Meaning - a connected series or group
Sentence - Numerous innovators are also worrying away at this nexus of problems.'''





