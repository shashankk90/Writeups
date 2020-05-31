# Intro to Stegano 3
**Category:** Stegano  
**Difficulty:** Baby  
**Author:** explo1t  
>This is an introductory challenge for the almighty steganography challenges. The three stages contain very different variants of hidden information. Find them!

![](https://github.com/aPanther/Writeups/blob/master/CSCG/attachments/chall.png)

## Solution
We are given the above image. But this image is more than an image. It contains a zip file embedded at the end. We can extract the zip from the image using _binwalk_ .
```bash
$ binwalk -e chall.png

DECIMAL   	HEX       	DESCRIPTION
-------------------------------------------------------------------------------------------------------
0         	0x0       	PNG image, 676 x 437, 8-bit/color RGBA, non-interlaced
WARNING: Extractor.execute failed to run 'jar xf 'flag.txt.zip'': [Errno 2] No such file or directory
299068    	0x4903C   	Zip archive data, compressed size: 48, uncompressed size: 28, name: "flag.txt"  
299288    	0x49118   	End of Zip archive 
```
 This zip contains the flag, but we can't extract it because its password protected. We still have to find the password. The image contains big chunks of same color. If we open the image with Windows paint and use the color fill to fill the blue sky, we can see some text in between.
 
 
 ![](https://github.com/aPanther/Writeups/blob/master/CSCG/attachments/steg3sol.png)
 
 
 s33\_m3\_1f\_y0u\_c4n is the password for the zip file. We can now get the flag.
```bash
$ 7z x flag.txt.zip 

7-Zip 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=en_GB.UTF-8,Utf16=on,HugeFiles=on,1 CPU)

Processing archive: flag.txt.zip

Extracting  flag.txt
Enter password (will not be echoed) :


Everything is Ok

Size:       28
Compressed: 220
$ cat flag.txt
CSCG{H1dden_1n_pla1n_s1ght}
```
