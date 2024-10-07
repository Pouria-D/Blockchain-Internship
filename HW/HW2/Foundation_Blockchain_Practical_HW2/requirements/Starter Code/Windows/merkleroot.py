import hashlib

# Do not change the name of this class

class MerkleTreeCalculator:

    # use this function for hashing a file
    def sha256sum(self, filename):
        h = hashlib.sha256()
        with open(filename, 'rb', buffering=0) as f:
            for b in iter(lambda: f.read(128 * 1024), b''):
                h.update(b)
        return h.hexdigest()

    # Do not change the name of this function
    def calculate_merkle_root(self, number):
        h1 = {}
        h2 = {}
        h3 = {}
        h4 = {}
        h5 = {}
        for i in range(1, 21):
            h1[i] = MerkleTreeCalculator.sha256sum(True, "file"+str(i)+".txt")
        for i in range(1, 11):
            h2[i] = (hashlib.sha256((str(h1[2 * i - 1]) + str(h1[2 * i])).encode()).hexdigest())
        for i in range(1, 6):
            h3[i] = (hashlib.sha256((str(h2[2 * i - 1]) + str(h2[2 * i])).encode()).hexdigest())
        h3[6] = h3[5]
        for i in range(1, 4):
            h4[i] = (hashlib.sha256((str(h3[2 * i - 1]) + str(h3[2 * i])).encode()).hexdigest())
        h4[4] = h4[3]
        for i in range(1, 3):
            h5[i] = (hashlib.sha256((str(h4[2 * i - 1]) + str(h4[2 * i])).encode()).hexdigest())

        h = hashlib.sha256((str(h5[1]) + str(h5[2])).encode()).hexdigest()

        return h
