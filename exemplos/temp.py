import hashlib
password = 'pas$w0rd'
h = hashlib.md5(password.encode('utf8')).hexdigest()
print(h)
