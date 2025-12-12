import hashlib
import sys

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

if __name__ == "__main__":
    pin = sys.argv[1]  
    print(hash_pin(pin))  



