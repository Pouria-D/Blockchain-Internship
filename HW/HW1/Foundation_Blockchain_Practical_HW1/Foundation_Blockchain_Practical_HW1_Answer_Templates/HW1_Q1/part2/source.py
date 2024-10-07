#Use this library for calculating hash functions
import hashlib
import timeit
code_to_test = """
#Do not change the name of the class
class CollisionFinder:
    def __init__(self):
        pass

    def findCollision(self): #Do not change the name of the function

        use1 = str(96106485)
        sha = hashlib.sha256(user1.encode()).hexdigest()
        sha = sha[-5:]
        x = 0
        while 1:
            sha1 = hashlib.sha256(str(x).encode()).hexdigest()
            sha1 = sha1[-5:]
            if sha1 == sha:
                m = x
                break
            x = x + 1
        user2 = m

        pass1 = str(1272974421)
        sha = hashlib.sha256(pass1.encode()).hexdigest()
        sha = sha[-5:]
        x = 0
        while 1:
            sha1 = hashlib.sha256(str(x).encode()).hexdigest()
            sha1 = sha1[-5:]
            if sha1 == sha:
                m = x
                break
            x = x + 1
        pass2 = m
        return [user1, user2, pass1, pass2]
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
