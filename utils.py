import base64
import hashlib
import random, string
import os

class utl:
    @staticmethod
    def salt(k=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    def to_base64(data : str, string=True) -> str:
        if string: return base64.b64encode(data.encode("utf-8")).decode('utf-8')
        return base64.b64encode(data.decode("utf-8"))

    def from_base64(data : str, string=True):
        if string : return base64.b64decode(data.encode("utf-8")).decode("utf-8")
        return base64.b64decode(data.decode("utf-8"))

    def sha256(data : str):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def sha256f(filepath: str, buffer_size: int = 65536) -> str:
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            while chunk := f.read(buffer_size):
                sha256.update(chunk)
        return sha256.hexdigest()