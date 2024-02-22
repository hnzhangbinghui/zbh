'''
alive progress库能够让进度条动起来，
alive_progress是一个动态的实时显示进度条库

'''
from alive_progress import alive_bar

import time
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
with alive_bar(len(mylist)) as bar:
    for i in mylist:
        bar()
        time.sleep(1)



