import hashlib

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

def combine_hashes(hash1, hash2):
    combined_hash = (hash1 + hash2)
    return sha256(combined_hash)


print("combine_hashes function:", combine_hashes)


file_path = "./fileopen.txt"
with open(file_path, 'w') as file:
    file.write("hello world json data in file ")


with open(file_path, 'r') as file:
    data = file.read()


block_size = max(1, len(data) // 1024)  
print("Block size:", block_size)


blocks = [data[i:i + block_size] for i in range(0, len(data), block_size)][:1024]
print("Blocks:", blocks)


blocks_list = []


while len(blocks) > 1:
    for i in range(0, len(blocks), 2):
        if i + 1 < len(blocks):
            combined_hash = combine_hashes(blocks[i], blocks[i + 1])
            blocks_list.append(combined_hash)
        else:
           
            blocks_list.append(blocks[i])
    
   
    blocks = blocks_list
    blocks_list = []
    print("Intermediate blocks:", blocks)


final_hash = blocks[0] if blocks else None
print("Final hash:", final_hash)