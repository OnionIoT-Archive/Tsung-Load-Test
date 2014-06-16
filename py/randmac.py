import random
def randomMAC():
    mac = [ 0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xef) ]
    return ''.join(map(lambda x: "%02x" % x, mac))
f = open('./csv/maclist.csv','w')
for n in range(100000):
    f.write(randomMAC()+'\n')
f.close()
