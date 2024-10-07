import hashlib
import random
import time
start_time = time.time()


def collision():
    user1 = str(random.randint(1, 17000))
    pass1 = str(random.randint(1, 17000))
    sha1 = hashlib.sha256(user1.encode()).hexdigest()
    sha2 = hashlib.sha256(pass1.encode()).hexdigest()
    sha1 = sha1[-5:]
    sha2 = sha2[-5:]

    x = 17000
    flag = 1
    while 1:
        sha = hashlib.sha256(str(x).encode()).hexdigest()
        sha = sha[-5:]
        if (x != user1) and (sha1 == sha):
            user2 = x
            flag = flag * 2
        elif sha == sha2 and x != pass1:
            pass2 = x
            flag = flag * 3
        if flag % 6 == 0:
            break
        x = x + 1
    print("username1 =", user1)
    print("username2 =", user2)
    print("password1 =", pass1)
    print("password2 =", pass2)


collision()
print("--- %s seconds ---" % (time.time() - start_time))
