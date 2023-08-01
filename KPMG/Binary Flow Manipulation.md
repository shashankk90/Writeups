# Binary Flow Manipulation

> The objective of this challenge is to reverse engineer a given binary executable file and modify the particular Registry to redirect program execution to a specific target address to display the flag.

We can use [Binary Ninja](https://cloud.binary.ninja/) to decompile the binary. The main function itself does not have anything related to the flag. There is `UnreachableFunction` that is not called anywhere in the program that contains the flag.

![binary ninja](https://github.com/shashankk90/Writeups/blob/master/KPMG/files/images/binaryFlowManipulation.png)

We can use the gdb to directly execute any function in the binary.

```sh
[ssk@arch files]$ gdb ./binaryFlowManipulation
Reading symbols from ./binaryFlowManipulation...
(gdb) break main
Breakpoint 1 at 0x8049842: file payload1.c, line 21.
(gdb) r
Starting program: /home/ssk/writeup/files/binaryFlowManipulation 

Breakpoint 1, main () at payload1.c:21
21	payload1.c: No such file or directory.
(gdb) print (void)UnreachableFunction()
KPMG_CTF{47634f7cdde0d9b804f9d0d603e4cd47}+
[Inferior 1 (process 103414) exited normally]
The program being debugged exited while in a function called from GDB.
Evaluation of the expression containing the function
(UnreachableFunction) will be abandoned.
(gdb) quit
```