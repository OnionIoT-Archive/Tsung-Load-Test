import os,sys

test=sys.argv[1]
time=0
for fil in os.listdir("./log/"+test):
    new=os.path.getmtime("./log/"+test+"/"+fil)
    if new>time:
        new=time
        recent=fil
print fil
