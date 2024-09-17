import hashlib   

cars_list = ["moter car", "bus", "train", "plain", "van"]
hashes = [hashlib.sha256(item.encode()).hexdigest() for item in cars_list]

print("The hashes are:", hashes)


if len(hashes) % 2 != 0:
    hashes.append(hashes[-1])
    print("The hashes are:", hashes)

hashes_list = []
while len(hashes) > 1:
    for i in range(0, len(hashes), 2):
        if i + 1 < len(hashes):
            combined_hash = hashlib.sha256((hashes[i] + hashes[i + 1]).encode()).hexdigest()
            hashes_list.append(combined_hash)
        else:
            hashes_list.append(hashes[i])
    hashes = hashes_list
    hashes_list = []
    print("Intermediate hashes:", hashes)

merkle_root = hashes
print("Merkle root:", merkle_root)
    
    
    