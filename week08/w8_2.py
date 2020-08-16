import datetime
import time


def timer(func):
    print('running in timer')
    def timer1():
        starttime = datetime.datetime.now()
        func()
        endtime = datetime.datetime.now()
        print((endtime - starttime).seconds)

    return timer1

@timer
def func():
    time.sleep(4)
    print('run func')




func()
