import hashlib
import json

def strigify(data):
    return json.dumps(data)

def crypto_hash(*args):
    strigified_args = sorted(map(strigify, args))
    joined_data = ''.join(strigified_args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash(1): {crypto_hash(1)}")

if __name__ == '__main__':
    main()