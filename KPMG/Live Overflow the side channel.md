# Live Overflow the side channel

> You have intercepted the power consumption from a wizards wand who is communicating to the enemy. Gandalf says that these wands use some kind of square and multiply algorithm based on the bit of the exponent when represented in binary. Find the key and stop the attack.  

We are given a file containing value of voltage at different times. The title and description hints towards a [youtube video](https://youtu.be/bFfyROX7V0s) by LiveOverflow. His video describes what's going on. Basically single low volt is 0 and low volt follwed by high volt is 1 due to the square and multiply algorithm.

I wrote a program to decode the key from the volts.
```python
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
```

On running this program, we get the flag.
```sh
[ssk@arch temp]$ python volt.py 
KPMG_CTF{21f0da0c0d3541fd}
```