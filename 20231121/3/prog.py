import struct
import sys
obj = sys.stdin.buffer.read()
length = len(obj)

if length < 44:
    print('NO')
    exit()
if obj[:4] != b'RIFF':
    print('NO')
    exit()
if obj[8:12] != b'WAVE':
    print('NO')
    exit()
if obj[12:16] != b'fmt ':
    print('NO')
    exit()
if struct.unpack('i', obj[16:20])[0] != 16:
    print('NO')
    exit()

if struct.unpack('i', obj[4:8])[0] != length - 8:
    print('NO')
    exit()
Size = struct.unpack('i', obj[4:8])[0]

Type = struct.unpack('h', obj[20:22])[0]
Channels = struct.unpack('h', obj[22:24])[0]
Bits = struct.unpack('h', obj[34:36])[0]

if struct.unpack('h', obj[32:34])[0] != (Bits * Channels)/8 or\
    struct.unpack('h', obj[32:34])[0] not in {1, 2, 4}:
    print('NO')
    exit()

Rate = struct.unpack('i', obj[24:28])[0]
if Rate != 44100 and Rate != 48000:
    print('NO')
    exit()

if struct.unpack('i', obj[28:32])[0] != (Rate * Bits * Channels)/8:
    print('NO')
    exit()

if obj[36:40] != b'data':
    print('NO')
    exit()

if struct.unpack('i', obj[40:44])[0] != Size - 36:
    print('NO')
    exit()
Data_size = struct.unpack('i', obj[40:44])[0]

print(f'Size={Size}, Type={Type}, Channels={Channels}, ', end = "")
print(f'Rate={Rate}, Bits={Bits}, Data size={Data_size}')
