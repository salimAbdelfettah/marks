import base64
from Crypto.Cipher import AES
from Crypto import Random

class Encryption():
	BS = 16

	def __init__(self, password, passphrase):
		self.password = password
		self.passphrase = passphrase

	def encrypt(self):
		BS = 16
		pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
		raw = pad(self.password)
		key = pad(self.passphrase)
		iv = Random.new().read( AES.block_size )
		cipher = AES.new(key, AES.MODE_CBC, iv )
		return base64.b64encode( iv + cipher.encrypt( raw ) )

	def decrypt(self):
		BS = 16
		pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
		unpad = lambda s : s[:-ord(s[len(s)-1:])]
		enc = base64.b64decode(self.password)
		iv = enc[:16]
		key = pad(self.passphrase)
		cipher = AES.new(key, AES.MODE_CBC, iv )
		return unpad(cipher.decrypt( enc[16:] ))
