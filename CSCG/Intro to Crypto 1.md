# Intro to Crypto 1
**Category:** Crypto  
**Difficulty:** Baby  
**Author:** black-simon  

>This is an introductory challenge for beginners which want to dive into the world of Cryptography. The three stages of this challenge will increase in difficulty. For an introduction to the first challenge visit the authors step by step guide.
For my new RSA key I used my own SecurePrimeService which definitely generates a HUGE prime!

## Solution
We are given a the _cipher message_ and the _public key_ used to encrypt it. RSA is used for encryption. We can use _openssl_ to extract the modulus and exponent from the file.
```bash
$openssl rsa -noout -modulus -pubin -in pubkey.pem -text
RSA Public-Key: (2047 bit)
Modulus:
    51:cf:f4:6d:9e:e3:20:96:d6:c8:06:cb:c7:df:2d:
    1d:3b:ea:7e:7b:2f:c4:e8:26:d9:fc:5e:18:79:99:
    12:dc:a1:50:b2:9c:65:c0:f9:e6:64:53:39:6c:e7:
    de:63:1a:0f:9a:67:45:13:8b:61:25:bb:cd:18:5a:
    a1:2e:b0:9a:4a:1b:d8:06:11:8c:97:a8:de:05:ed:
    0b:e6:b4:5f:c1:c9:e9:93:71:92:f5:8b:c4:a5:cc:
    27:67:80:3c:0b:21:34:2a:f5:cb:8f:34:af:fb:1a:
    6e:c2:52:0c:76:5d:87:52:1c:68:48:db:d8:31:81:
    2e:cc:6d:8b:b3:d6:17:33:b0:eb:c3:52:cf:64:d4:
    44:5c:99:55:72:92:2f:49:3d:71:89:95:9d:b2:32:
    1e:1b:ac:59:25:fa:56:dc:69:f6:85:8e:fe:eb:a0:
    a5:a9:d7:6b:a1:98:18:71:53:92:74:24:e5:f7:b6:
    80:98:ab:8c:10:44:2b:73:d1:49:02:7c:fc:37:d0:
    30:05:63:37:c3:e0:f4:21:6c:f4:32:23:96:74:41:
    b6:08:ee:c2:a6:48:e8:ce:85:78:94:c6:65:03:0c:
    01:24:56:29:27:9b:38:7f:cd:bd:c3:5b:61:67:71:
    5b:54:bd:55:56:18:0d:9a:f2:50:4b:52:7a:90:fa:
    e7
Exponent: 65537 (0x10001)
Modulus=51CFF46D9EE32096D6C806CBC7DF2D1D3BEA7E7B2FC4E826D9FC5E18799912DCA150B29C65C0F9E66453396CE7DE631A0F9A6745138B6125BBCD185AA12EB09A4A1BD806118C97A8DE05ED0BE6B45FC1C9E9937192F58BC4A5CC2767803C0B21342AF5CB8F34AFFB1A6EC2520C765D87521C6848DBD831812ECC6D8BB3D61733B0EBC352CF64D4445C995572922F493D7189959DB2321E1BAC5925FA56DC69F6858EFEEBA0A5A9D76BA198187153927424E5F7B68098AB8C10442B73D149027CFC37D030056337C3E0F4216CF43223967441B608EEC2A648E8CE857894C665030C01245629279B387FCDBDC35B6167715B54BD5556180D9AF2504B527A90FAE7
```
When we try to find the factor of modulus, we are able to find it easily. The issue is that one of the factors is NOT big enough. Since we can find the factors of modulus, we can also find the decryption key.
```python
message = 4522827319495133992180681297469132393090864882907734433792485591515487678316653190385712678072377419115291918844825910187405830252000250630794128768175509500175722681252259065645121664124102118609133000959307902964132117526575091336372330412274759536808500083138400040526445476933659309071594237016007983559466411644234655789758508607982884717875864305554594254277210539612940978371460389860098821834289907662354612012313188685915852705277220725621370680631005616548237038578956187747135229995137050892471079696577563496115023198511735672164367020373784482829942657366126399823845155446354953052034645278225359074399

Modulus= 0x51CFF46D9EE32096D6C806CBC7DF2D1D3BEA7E7B2FC4E826D9FC5E18799912DCA150B29C65C0F9E66453396CE7DE631A0F9A6745138B6125BBCD185AA12EB09A4A1BD806118C97A8DE05ED0BE6B45FC1C9E9937192F58BC4A5CC2767803C0B21342AF5CB8F34AFFB1A6EC2520C765D87521C6848DBD831812ECC6D8BB3D61733B0EBC352CF64D4445C995572922F493D7189959DB2321E1BAC5925FA56DC69F6858EFEEBA0A5A9D76BA198187153927424E5F7B68098AB8C10442B73D149027CFC37D030056337C3E0F4216CF43223967441B608EEC2A648E8CE857894C665030C01245629279B387FCDBDC35B6167715B54BD5556180D9AF2504B527A90FAE7
e = 0x10001

for i in range(3,1000000000,2):
	if(Modulus % i == 0):
		break

p = i
q = Modulus//p
phi = Modulus - q - p + 1

def multiplicative_inverse(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa

    return lx

d = multiplicative_inverse(e,phi)
from Crypto.Util.number import long_to_bytes
plaintext = pow(message, d, Modulus)
print(long_to_bytes(plaintext))
```
This little program allows us to decrypt the cipher and get the flag.
```bash
$python3 solve.py
b'CSCG{factorizing_the_key=pr0f1t}'
```

### CSCG{factorizing\_the\_key=pr0f1t}
