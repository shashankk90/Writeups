# Intro to Reversing 3
**Category:** Reverse Engineering  
**Difficulty:** Baby  
**Author:** 0x4d5a  

>This is a introductory challenge for beginners which are eager to learn reverse engineering on linux. The three stages of this challenge will increase in difficulty. 
Once you solved the challenge locally, grab your real flag at: nc hax1.allesctf.net 9602
Note: Create a dummy flag file in the working directory of the rev1 challenge. The real flag will be provided on the server

## Solution
The given zip file contains a _dummy flag_ and a program _rev3_. We will use the _ltrace_ command to trace the library calls.
```bash
 $ltrace ./rev3
fopen("./flag", "r")                             = 0x5576397f82a0
fread(0x55763916e040, 256, 1, 0x5576397f82a0)    = 0
fclose(0x5576397f82a0)                           = 0
puts("Give me your password: "Give me your password: 
)                  = 24
read(0AAA
, "AAA\n", 31)                             = 4
strcmp("IHK", "lp`7a<qLw\036kHopt(f-f*,o}V\017\025J") = -35
puts("Thats not the password!"Thats not the password!
)                  = 24
+++ exited (status 0) +++
```
We can see the general structure of the program. It reads the flag, then asks for a password. If the password matches, it will give us the flag. It uses some form of encryption to hide the password. To get the encryption algorithm we will use _Ghidra_. Using Ghidra we can get the _main()_ function of the program.
```c
undefined8 main(void)
{
  int iVar1;
  ssize_t sVar2;
  long in_FS_OFFSET;
  int local_40;
  byte local_38 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  initialize_flag();
  puts("Give me your password: ");
  sVar2 = read(0,local_38,0x1f);
  local_38[(int)sVar2 + -1] = 0;
  local_40 = 0;
  while (local_40 < (int)sVar2 + -1) {
    local_38[local_40] = local_38[local_40] ^ (char)local_40 + 10U;
    local_38[local_40] = local_38[local_40] - 2;
    local_40 = local_40 + 1;
  }
  iVar1 = strcmp((char *)local_38,"lp`7a<qLw\x1ekHopt(f-f*,o}V\x0f\x15J");
  if (iVar1 == 0) {
    puts("Thats the right password!");
    printf("Flag: %s",flagBuffer);
  }
  else {
    puts("Thats not the password!");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
We can see the algorithm used for encryption.
```c
local_40 = 0;
  while (local_40 < (int)sVar2 + -1) {
    local_38[local_40] = local_38[local_40] ^ (char)local_40 + 10U;
    local_38[local_40] = local_38[local_40] - 2;
    local_40 = local_40 + 1;
  }
 ```
 What it does is takes each character, XORs it with (index+10) and then subtracts 2 from it. Then it is compared with encrypted password. I wrote a python program to decrypt it. We have to take each character of encrypted password, subtract 2 and XOR it with (index+10)
 ```python
 epasswd = "lp`7a<qLw\036kHopt(f-f*,o}V\017\025J"
passwd = ''
for i in range(0,len(epasswd)):
	var = ord(epasswd[i]) + 2
	var = var ^ (i+10)
	passwd += chr(var)
print passwd
```
Running the program we get the password which can be used to get the flag.
```bash
$python solve.py 
dyn4m1c_k3y_gen3r4t10n_y34h
$python solve.py | ./rev3
Give me your password: 
Thats the right password!
Flag: CSCG{real_flag_is_on_the_server}
$python solve.py | nc hax1.allesctf.net 9602
Give me your password: 
Thats the right password!
Flag: CSCG{pass_1_g3ts_a_x0r_p4ss_2_g3ts_a_x0r_EVERYBODY_GETS_A_X0R}
```
### CSCG{pass\_1\_g3ts\_a\_x0r\_p4ss\_2\_g3ts\_a\_x0r\_EVERYBODY\_GETS\_A\_X0R}
 
