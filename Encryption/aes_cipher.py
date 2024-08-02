import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher:
    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(raw.encode())
        return base64.b64encode(iv + encrypted).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(enc[AES.block_size:])
        return self._unpad(decrypted).decode('utf-8')

    def _pad(self, s):
        padding_len = self.bs - len(s) % self.bs
        return s + chr(padding_len) * padding_len

    def _unpad(self, s):
        padding_len = s[-1]
        return s[:-padding_len]

# Example usage:
if __name__ == '__main__':
    key = input("Introduce key: ")
    cipher = AESCipher(key)

    plaintext = "hello"
    encrypted = cipher.encrypt(plaintext)
    print("Encrypted: ", encrypted)

    key_for_decryption = input("Introduce key to decode: ")
    cipher_for_decryption = AESCipher(key_for_decryption)
    decrypted = cipher_for_decryption.decrypt(encrypted)
    print("Decrypted: ", decrypted)
