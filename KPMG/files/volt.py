# volt.py

file = open('Voltage.txt','r')
volts = file.read()
file.close()
volts = volts.split(', ')
volts = [ 0 if int(volts[i]) < 40 else 1 for i in range(0,len(volts),5)]
i = 0
key = ''
while i < len(volts):
    if volts[i+1] == 1 and volts[i] == 0:
        key+= '1'
        i += 2
    else :
        key+='0'
        i += 1

for i in range(0, len(key), 8):
    print(chr(int(key[i:i+8],2)),end='')
