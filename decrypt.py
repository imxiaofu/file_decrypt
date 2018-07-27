# -*- coding: gbk -*-
#A Test to Return a AES-File of a Common File

from Crypto.Cipher import AES
#from Crypto import Random
import binascii
import os
from random import Random
import sys

def jm_iv(yiv,ivkey):
    if len(ivkey) > 16:
        ivkey = ivkey[0:16]
    elif len(ivkey) <16 :      
        ivy = len(ivkey) % 16  
        ivkey = ivkey + '0'*(16 - ivy)
    jmfile = raw_input('please enter decrypt file:')
    ivfp = open(jmfile , 'rb')   
    iviv = ivfp.read(16)
    #print iviv
    ivfp.close()
    ivcipher = AES.new(ivkey, AES.MODE_CBC, iviv)
    ivmsg = ivcipher.decrypt(yiv)
    return ivmsg


def jm(fp,key,iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    msg=cipher.decrypt(fp)
    return msg

def random_str(randomlength=16):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


if __name__ == "__main__":
    mblj = str(sys.argv[1])
    key = str(sys.argv[2])
    if len(key) > 16:
        key = key[0:16]
    elif len(key) <16 :      
        y = len(key) % 16  
        key = key + '0'*(16 - y)
    fp = open(mblj, 'rb')
    yiv = fp.read(16)
    iv = jm_iv(yiv, key)
    print iv
    #fp.seek(0,16)
    fp_msg = fp.read()
    fp.close()
    
    filename = random_str()
    fp1 = open(filename + '.jpg', 'wb')
    fp1.seek(0,0)
    zuizhong = jm(fp_msg , key, iv)
    fp1.writelines(zuizhong)
    fp1.close()
    
    raw_input('Enter for Exit...')