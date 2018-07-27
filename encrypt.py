from Crypto.Cipher import AES
import binascii
import os
from random import Random
import sys

def jm_iv(yiv,ivkey): #实际加密工作
    if len(ivkey) > 16:
        ivkey = ivkey[0:16]
    elif len(ivkey) <16 :      
        ivy = len(ivkey) % 16  
        ivkey = ivkey + '0'*(16 - ivy)
    jmfile = raw_input("please enter encrypt file:")
    ivfp = open(jmfile , 'rb')   
    iviv = ivfp.read(16)
    ivfp.close()
    ivcipher = AES.new(ivkey, AES.MODE_CBC, iviv)
    ivmsg = ivcipher.encrypt(yiv)
    return ivmsg

def AES_File(fs,key,iv):   #整合密文及加密信息
    cipher = AES.new(key, AES.MODE_CBC, iv)
    x = len(fs) % 16
    if x != 0:
        fs_pad = fs + '0'*(16 - x)
    iv = jm_iv(iv, key)
    msg = iv + cipher.encrypt(fs_pad)
    return msg


def random_str(randomlength=16):    #随机字符串
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


if __name__ == "__main__":
    iv = random_str()
    ylj = str(sys.argv[1])
    key = str(sys.argv[2])
    #print iv
    if len(key) > 16:
        key = key[0:16]
    elif len(key) <16 :      
        y = len(key) % 16  
        key = key + '0'*(16 - y)
    fs = open(ylj , 'rb')
    fs.seek(0,0)
    fs_msg = fs.read()
    fs.close()
    filename = random_str()
    print filename
    fc = open(filename, 'wb')
    fc_msg = AES_File(fs_msg,key,iv)
    fc.writelines(fc_msg)
    fc.close()
    raw_input('Enter for Exit...')