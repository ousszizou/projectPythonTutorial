from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from  hashlib  import md5

class PrpCrypt(object):

    def __init__(self, key):
        self.key = md5(key.encode('utf-8')).hexdigest().encode('utf-8')
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')

        length = 16
        count = len(text)
        if count < length:
            add = (length - count)

            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))

            text = text + ('\0' * add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
    
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')
