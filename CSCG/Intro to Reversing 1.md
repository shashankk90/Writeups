# Intro to Reversing 1
**Category:** Reverse Engineering  
**Difficulty:** Baby  
**Author:** 0x4d5a  

>This is a introductory challenge for beginners which are eager to learn reverse engineering on linux. The three stages of this challenge will increase in difficulty. 
Once you solved the challenge locally, grab your real flag at: nc hax1.allesctf.net 9600
Note: Create a dummy flag file in the working directory of the rev1 challenge. The real flag will be provided on the server
## Solution
The given zip file contains a _dummy flag_ and a program _rev1_. We will use the _ltrace_ command to trace the library calls.
```bash
$ltrace ./rev1 
fopen("./flag", "r")                             = 0x560a375442a0
fread(0x560a36b0c040, 256, 1, 0x560a375442a0)    = 0
fclose(0x560a375442a0)                           = 0
puts("Give me your password: "Give me your password: 
)                  = 24
read(0test
, "test\n", 31)                            = 5
strcmp("test", "y0u_5h3ll_p455")                 = -5
puts("Thats not the password!"Thats not the password!
)                  = 24
+++ exited (status 0) +++
```
We can see the general structure of the program. It reads the flag, then asks for a password. If the password is **y0u\_5h3ll\_p455**, it will probably give us the flag.
```bash
 $./rev1
Give me your password: 
y0u_5h3ll_p455
Thats the right password!
Flag: CSCG{real_flag_is_on_the_server}
```
We got the dummy flag, now the same thing but with the server.
```bash
$nc hax1.allesctf.net 9600
Give me your password: 
y0u_5h3ll_p455
Thats the right password!
Flag: CSCG{ez_pz_reversing_squ33zy}
```

### CSCG{ez\_pz\_reversing\_squ33zy}
