# Secure Storage Showdown

> Your mission is to navigate the intricacies of AWS (Amazon Web Services) and obtain the confidential information within.
> https://kpng-ctf.s3.ap-south-1.amazonaws.com/index.html

We are given the link to a aws s3 bucket. The `aws-cli` allows us to list all the files available in the bucket. 

```bash
[ssk@arch kic]$ aws s3 ls s3://kpmg-ctf --recursive

2023-04-88 22:13:46         42 flag-me-if-you-can.txt
2023-04-08 22:05:00  110824955 hacker.gif
2023-04-88 22:09:82         81 index.html
```
The bucket has a flag file which contains the flag.
```bash
[ssk@arch kic]$ aws s3 cp s3://kpmg-ctf/flag-me-if-you-can.txt flag.txt
download: s3://kpmg-ctf/flag-me-if-you-can.txt to ./flag.txt

[ssk@arch kic]$ cat flag.txt
KPMG_CTF{5247146a414c3ea2f7bec2c0f9b0664d}
```