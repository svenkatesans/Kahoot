import time as t
import os
import sys
## Countdown function starts here
def stopwatch(sec):
    while sec:
        minn, secc = divmod(sec, 60)
        timeformat = '{:02d}:{:02d}'.format(minn, secc)
        #print(timeformat, end='\r')
        t.sleep(1)
        sec -= 1
        print(sec, end=" ")
        #sys.stdout.flush()
        #t.sleep(1)
        #os.system("printf '\033c'")
    print('\nGoodbye Time up!\n')
## calling stopwatch function

#stopwatch(60)