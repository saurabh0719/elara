import elaradb

key_path = 'elara.key'
elaradb.KEYGEN(key_path)

db = elaradb.RUNSECURE('test.mg', key_path)

x = [1, 2, 3]

db.SET('key', x)
print(db.EXISTS('key2'))
y = db.GET('key')
print(y)
db.PRINTKEY()
db.SAVE()
db.SET('key2', 'saurabh')
z = db.GET('key2')
print('Y : ', y)
print('Z : ', z)
