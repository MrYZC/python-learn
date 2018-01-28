import array
import struct
f = open('./demo.wav', 'rb')
info = f.read(44) #指定字节数
print info
print struct.unpack('h', '\x01\x02') #转化二进制
print struct.unpack('h', info[22:24])
print struct.unpack('i', info[24:28])
print struct.unpack('h', info[34:36])
f.seek(0,2) #将指针移到文件的末尾
print f.tell()
n = (f.tell()- 44 ) / 2
buf = array.array('h', (0 for _ in xrange(n))) #初始化buf
f.seek(44) #指针指向data区
f.readinto(buf) #把数据读取到buf区中
print buf[0]
print buf[5]
for i in xrange(n): buf[i]/=8
f2 = open('./demo2.wav','wb')
f2.write(info)
buf.tofile(f2)


