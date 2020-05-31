# Intro to Stegano 1
**Category:** Stegano  
**Difficulty:** Baby  
**Author:** explo1t  
>This is an introductory challenge for the almighty steganography challenges. The three stages contain very different variants of hidden information. Find them!  

![](https://github.com/aPanther/Writeups/blob/master/CSCG/attachments/chall.jpg)  
## Solution
We are given the above image. When we use the _file_ commmand on the image, we can see some information in comments.
```bash
$ file chall.jpg 
chall.jpg: JPEG image data, JFIF standard 1.01, comment: "alm1ghty_st3g4n0_pls_g1v_fl4g"
```
It seems like a password for something.
When we use this password with steghide, we obtain a file containing the flag.
```bash
$ steghide extract -sf chall.jpg --passphrase "alm1ghty_st3g4n0_pls_g1v_fl4g"
wrote extracted data to "flag.txt".
$ cat flag.txt 
CSCG{Sup3r_s3cr3t_d4t4}
```

### CSCG{Sup3r\_s3cr3t\_d4t4}
