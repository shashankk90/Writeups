# Hidden Network Quest
> Your mission is to navigate the vast expanse of the internet and unravel the mystery concealed within the depths of the digital world. For a start, find out who is Aditya Kashinath.  

This OSINT challenge asks to find out about Aditya Kashinath. On googling his name we can find his [Linkedin](https://in.linkedin.com/in/aditya-kashinath-4042a1186). The about section contains the following string:
`S1BNR19DVEZ7YzJlYjkyYjlmNDY2NmViNTU1MTJjYWJmNGFjNDlkNmV9`

We can use put this string into [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=UzFCTlIxOURWRVo3WXpKbFlqa3lZamxtTkRZMk5tVmlOVFUxTVRKallXSm1OR0ZqTkRsa05tVjk) to decode it. It is a base64 encoded string.

KPMG_CTF{c2eb92b9f4666eb55512cabf4ac49d6e}