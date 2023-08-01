# Unveiling the Hidden Message

> The objective of this challenge is to reverse engineer a given binary executable file and extract flag embedded within the program.

We can use [Binary Ninja](https://cloud.binary.ninja/) to decompile the binary. The data section contains the flag.

![binary ninja](https://github.com/shashankk90/Writeups/blob/master/KPMG/files/images/unveilMessage.png)

KPMG_CTF{e59ff97941044f85df5297e1c302d260}