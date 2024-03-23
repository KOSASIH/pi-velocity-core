import hashlib
import base58

class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.address = None

    def generate_keys(self):
        import rsa
        (self.private_key, public_key) = rsa.newkeys(bits=2048)
        self.public_key = public_key

    def get_address(self):
        if self.address is None:
            public_key_bytes = self.public_key.save_pkcs1('PEM')
            public_key_contents = public_key_bytes.decode('utf-8')
            public_key_hash = hashlib.sha256(public_key_contents.encode('utf-8')).digest()
            public_key_checksum = hashlib.new('ripemd160').update(public_key_hash).digest()
            public_key_checksum_bytes = base58.b58encode(public_key_checksum)
            address = 'P' + str(public_key_checksum_bytes, 'utf-8')
            self.address = address

    def sign_data(self, data):
        message = int(hashlib.sha256(data.encode('utf-8')).digest(), 16)
        signature = self.private_key.sign(message, rsa.pkcs1.PSS(mgf=rsa.pkcs1.MGF1(hashlib.sha256())))
        return signature.verify(message, self.public_key)

    def verify_signature(self, data, signature):
        message = int(hashlib.sha256(data.encode('utf-8')).digest(), 16)
        try:
            self.public_key.verify(message, signature, rsa.pkcs1.PSS(mgf=rsa.pkcs1.MGF1(hashlib.sha256())))
            return True
        except rsa.PKCS11Error:
            return False
