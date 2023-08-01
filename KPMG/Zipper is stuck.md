# Zipper is Stuck

> As an elite cyber investigator, you receive an anonymous tip about a suspicious network activity . Unravel the encrypted messages, follow the digital trail, and work with your team to retrieve the confidential information. The message has a 3 digit lock.  

We are given wireshark capture file.
On examining the packets, we can see that there are some http requests. One of the request contains a GET request to flag.zip file and the response contains the zip file. We can extract this file using wireshark. 

![wireshark](https://github.com/shashankk90/Writeups/blob/master/KPMG/files/images/Zipper%20is%20stuck1.png)
![wireshark](https://github.com/shashankk90/Writeups/blob/master/KPMG/files/images/Zipper%20is%20stuck2.png)

The zip file is password protected using 3 digit lock. I wrote a simple script to try all the 3 digit passwords.

```sh
#! /bin/bash
# zipperIsStuck.sh
for password in {100..999}; do
  unzip -P "$password" -d "dir$password" "Zipper Is Stuck.zip" > /dev/null 2>&1
  if [ -z "$(ls dir$password)" ]; then
    rmdir "dir$password"
  fi
done

cat dir*/*
rm -rd dir*
```

We can run this script to try all the combinations.
This will allow us to extract the files. There are a few passwords for which the zip file extracts but the contents are corrupt. We can ignore these.

```sh
[ssk@arch temp]$ ./brute.sh 
`1:Կ5MKgռN)ywUiKPMG_CTF{P@$$w0rd_i$_KPMG}`?c$atBPeP?,_|Ips2{L ˄;Lj\
```
