import hashlib
import math as m
#Do not change the name of this class
class MerkleTreeCalculator:
    def __init__(self):
        pass

    #use this function for hashing a file
    def sha256sum(self, filename):
        h = hashlib.sha256()
        with open(filename, 'rb', buffering=0) as f:
            for b in iter(lambda: f.read(128 * 1024), b''):
                h.update(b)
        return h.digest()

	#Do not change the name of this function
    def calculate_merkle_root(self,number_of_files):
        #number_of_files = 18
        tree_layers = m.ceil(m.log(number_of_files, 2))
        # free_leafs = 2 ** tree_layers - number_of_files
        initialpath = 'resource'
        file = ['/file'] * number_of_files
        a = list(range(1, number_of_files + 1))
        filenames = [''] * number_of_files
        for i in range(0, number_of_files):
            filenames[i] = initialpath + file[i] + str(a[i]) + '.txt'
        hashes = [''] * 2 ** tree_layers
        for i in range(0, 2 ** tree_layers):
            if i < number_of_files:
                hashes[i] = MerkleTreeCalculator.sha256sum(True, filenames[i])
            else:
                hashes[i] = hashes[i - 2]
        for treelevel in range(tree_layers - 1, -1, -1):
            for i in range(0, 2 ** treelevel):
                string = hashes[2 * i] + hashes[2 * i + 1]
                hashes[i] = hashlib.sha256(string).digest()

        # An irrelevant output
        return hashes[0]



