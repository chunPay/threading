# encoding:utf-8
import threading
import os
import time

filepath="/home/msmc/data/nginxlog/agif/2018-11-18/2018-11-18"
result="/home/msmc/agif_log/python_result"
files=os.listdir(filepath)
fw=open(result,'a+')
lit=[ 6468549060181012488,6468686757201621025,6468704763579379828,6468771400613539958,6468775247327178849]
def small_one(num):
    global files
    global lock
    while True:
        try:
            lock.acquire()
            if len(files)>0:
                for filen in files:
                    print filen
                    fp=open(filepath+"/"+filen,'r+')
                    for lines in fp.readlines():
#                        print lines
                        for lt in lit:
                            if lines.find(str(lt))>0:
                                fw.write(lines)
                    files.remove(filen)
                    time.sleep(0.5)
            else:
                print "no more files"
                os._exit(0)
            lock.release()
            time.sleep(0.5)
        except Exception,e:
            print e
            os._exit(0)

threadlist=[]
lock=threading.Lock()
if __name__=="__main__":
    for i in range(5):
        t=threading.Thread(target=small_one,args=(i,))
        threadlist.append(t)
    for t in threadlist:
        t.start()
    for t in threadlist:
        t.join()
    print "finish"
