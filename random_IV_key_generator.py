#!/usr/bin/python
import random
import string
IV = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(128))
print('IV: ',IV)
print('key: ', key)