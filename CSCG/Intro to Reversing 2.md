# Intro to Reversing 2
**Category:** Reverse Engineering  
**Difficulty:** Baby  
**Author:** 0x4d5a  

>This is a introductory challenge for beginners which are eager to learn reverse engineering on linux. The three stages of this challenge will increase in difficulty. 
Once you solved the challenge locally, grab your real flag at: nc hax1.allesctf.net 9601
Note: Create a dummy flag file in the working directory of the rev1 challenge. The real flag will be provided on the server

## Solution
The given zip file contains a _dummy flag_ and a program _rev2_. We will use the _ltrace_ command to trace the library calls.
```bash
$ltrace ./rev2 
fopen("./flag", "r")                             = 0x55af951ca2a0
fread(0x55af941f3040, 256, 1, 0x55af951ca2a0)    = 0
fclose(0x55af951ca2a0)                           = 0
puts("Give me your password: "Give me your password: 
)                  = 24
read(0AAAAAAA
, "AAAAAAA\n", 31)                         = 8
strcmp("\312\312\312\312\312\312\312", "\374\375\352\300\272\354\350\375\373\275\367\276\357\271\373\366\275\300\272\271\367\350\362\375\350\362\374") = -50
puts("Thats not the password!"Thats not the password!
)                  = 24
+++ exited (status 0) +++
```
We can see the general structure of the program. It reads the flag, then asks for a password. If the password matches, it will give us the flag. It uses some form of encryption to hide the password. Playing around with it, we can see that all numbers are in octal and each letter has a specific number assigned to it. With enough experimenting, we can easily find the encryption algorithm. It takes each letter, converts it to its ascii value, adds 137 and then is converted to octal. I wrote a simple python program to decrypt it and get the password.
```python
leaks = "374 375 352 300 272 354 350 375 373 275 367 276 357 271 373 366 275 300 272 271 367 350 362 375 350 362 374"
numbers = leaks.split(' ')
password = ''
for i in numbers:
	password += chr(int(i,8) - 137)
print password
```
This gives us the password which can be used to get the flag
```bash
$python rev2.py 
sta71c_tr4n5f0rm4710n_it_is
$python rev2.py | ./rev2
Give me your password: 
Thats the right password!
Flag: CSCG{real_flag_is_on_the_server}
```
```bash
$python rev2.py | nc hax1.allesctf.net 9601
Give me your password: 
Thats the right password!
Flag: CSCG{1s_th4t_wh4t_they_c4ll_on3way_transf0rmati0n?}
```
## CSCG{1s\_th4t\_wh4t\_they\_c4ll\_on3way\_transf0rmati0n?}


