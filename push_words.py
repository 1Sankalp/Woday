import schedule 
import time
from notify_run import Notify

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

schedule.every().day.at('16:10').do(wotd)

while 1:
    schedule.run_pending()
    time.sleep(1)
  
