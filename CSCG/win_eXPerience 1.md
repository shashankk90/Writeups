# win_eXPerience 1
**Category:** Misc  
**Difficulty:** Easy  
**Author:** TheVamp  

>R3m3mb3r th3 g00d 0ld 1337 d4y5, wh3r3 3ncrypt10n t00l5 4r3 u53d, wh1ch 4r3 d34d t0d4y 4nd r3c0mm3nd b1tl0ck3r. H4v3 fun t0 f1nd th15 5m4ll g3m 1n th3 m3m0ry dump.
Annoucement 1: If you find a flag within a picuture, thats not a flag! Its an artifact from an older revision of this challenge, please ignore!

## Solution
We are given a memory dump to find the flag. We will use the tool _volatility_ to find the flag. First we check the processes running with _pstree_
```bash
$./volatility64 -f memory.dmp  pstree
Volatility Foundation Volatility Framework 2.5
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0x81bcca00:System                                      4      0     53    262 1970-01-01 00:00:00 UTC+0000
. 0x81a04da0:smss.exe                                 340      4      3     21 2020-03-22 18:27:38 UTC+0000
.. 0x81a41950:winlogon.exe                            524    340     19    428 2020-03-22 18:27:39 UTC+0000
... 0x81a2d810:lsass.exe                              644    524     23    356 2020-03-22 18:27:39 UTC+0000
... 0x816d8cd8:wpabaln.exe                            988    524      1     66 2020-03-22 18:29:38 UTC+0000
... 0x8197eda0:services.exe                           632    524     16    262 2020-03-22 18:27:39 UTC+0000
.... 0x81abd0f0:svchost.exe                          1024    632     67   1298 2020-03-22 18:27:39 UTC+0000
..... 0x81768310:wuauclt.exe                         1300   1024      7    174 2020-03-22 18:28:35 UTC+0000
..... 0x817a9b28:wscntfy.exe                         1776   1024      1     36 2020-03-22 18:28:51 UTC+0000
.... 0x81a0cda0:VBoxService.exe                       792    632      9    118 2020-03-22 18:27:39 UTC+0000
.... 0x816e41f0:svchost.exe                          1688    632      9     93 2020-03-22 18:28:00 UTC+0000
.... 0x81abf9a8:svchost.exe                           928    632      9    259 2020-03-22 18:27:39 UTC+0000
.... 0x8172abc0:svchost.exe                           548    632      8    129 2020-03-22 18:27:51 UTC+0000
.... 0x8194dc70:svchost.exe                          1076    632      6     74 2020-03-22 18:27:39 UTC+0000
.... 0x817b2318:spoolsv.exe                          1536    632     14    113 2020-03-22 18:27:40 UTC+0000
.... 0x81a16500:svchost.exe                           840    632     20    204 2020-03-22 18:27:39 UTC+0000
.... 0x817da020:svchost.exe                          1120    632     18    219 2020-03-22 18:27:39 UTC+0000
.... 0x81759820:alg.exe                              1176    632      6    100 2020-03-22 18:27:51 UTC+0000
.. 0x81a46928:csrss.exe                               496    340      9    387 2020-03-22 18:27:39 UTC+0000
 0x817b33c0:explorer.exe                             1524   1484     14    353 2020-03-22 18:27:40 UTC+0000
. 0x8173ec08:CSCG_Delphi.exe                         1920   1524      1     29 2020-03-22 18:27:45 UTC+0000
. 0x8176c378:mspaint.exe                              264   1524      4    102 2020-03-22 18:27:48 UTC+0000
. 0x816d8438:TrueCrypt.exe                            200   1524      1     44 2020-03-22 18:28:02 UTC+0000
. 0x817cd690:ctfmon.exe                              1652   1524      1     66 2020-03-22 18:27:40 UTC+0000
. 0x81794608:VBoxTray.exe                            1644   1524     12    122 2020-03-22 18:27:40 UTC+0000
. 0x81791020:msmsgs.exe                              1660   1524      4    169 2020-03-22 18:27:40 UTC+0000
```
We can see that TrueCrypt.exe is running (which replaced Bitlocker). Now we will use _filescan_ to check for files.
```bash
$./volatility64 -f memory.dmp filescan > log
```
On examining the log file we find some interesting files.
- \Device\HarddiskVolume1\Documents and Settings\CSCG\Desktop\CSCG\cscg.flag.PNG
- \Device\TrueCryptVolumeE\password.txt
- \Device\TrueCryptVolumeE\flag.zip

The cscg.flag.PNG is the arfifact mentioned in description. The real files are _password.txt_ and _flag.zip_. We can use _dumpfiles_ to extract these files. The log files also contains the physical offset of these files which are required for extraction.
```bash
$./volatility64 -f memory.dmp dumpfiles -Q 0x0000000001a3c7e8 --dump-dir=./
Volatility Foundation Volatility Framework 2.5
DataSectionObject 0x01a3c7e8   None   \Device\TrueCryptVolumeE\flag.zip
$./volatility64 -f memory.dmp dumpfiles -Q 0x0000000001717be8 --dump-dir=./
Volatility Foundation Volatility Framework 2.5
DataSectionObject 0x01717be8   None   \Device\TrueCryptVolumeE\password.txt
```
This will extract two files _file.None.0x81732ef8.dat_ and _file.None.0x81a8ffa0.dat_. We use _file_ command now to check these files
```bash
$file file*
file.None.0x81732ef8.dat: Zip archive data, at least v5.1 to extract
file.None.0x81a8ffa0.dat: data
$cat file.None.0x81a8ffa0.dat
BorlandDelphiIsReallyCool
```
One file is a zip file containing the flag and the other contains the password of the zip file. Unzipping it we can get the flag.
### CSCG{c4ch3d\_p455w0rd\_fr0m\_0p3n\_tru3\_cryp1\_c0nt41n3r5}
