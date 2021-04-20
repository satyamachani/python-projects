from hashlib import sha256
MAX_NONCE =100000000

def sha256(text):
    return sha256(text.encode('ascii')).hexdigest()

def mine(block_number,transactions,previous_hash,prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = sha256(text)
        if new_hash.startswitch(prefix_str):
            print(f"yay! Sucessfully mined bitcoins with bitcoins with nonce value :{nonce}")
            return new_hash
    
    raise BaseException("Couldn't find correct has after trying {MAX_NONCE} times")

if __name__ =='__main__':
    transactions = '''
    dhaval->bhavin->20,
    mando->cara->45
    '''
    difficulty = 4
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5 , transactions , '00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048' , difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took : {total_time} seconds")
    print(new_hash)