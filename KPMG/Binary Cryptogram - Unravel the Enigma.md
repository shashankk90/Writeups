# Binary Cryptogram - Unravel the Enigma

> A notorious organization, "The Enigma Syndicate,” has sent encrypted messages detailing a dark conspiracy. Participants must tackle their binary cryptogram using powerful reverse engineering tool to reveal the sinister plot. Unravel the enigma, stop the conspiracy, and become the ultimate codebreaker in this thrilling CTF challenge!

We can use [Binary Ninja](https://cloud.binary.ninja/) to decompile the binary. On inspecting the main function, we can see that it is expecting a command line argument "error".

![binary ninja](https://github.com/shashankk90/Writeups/blob/master/KPMG/files/images/binaryCryptogram.png)

```sh
[ssk@arch kic]$./binaryCryptogram "error"
Decrypted Flag: KPMG_CTF{be441ba8020e7ea99cd879b156db1e79}
```