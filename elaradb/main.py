import elaradb

db = elaradb.RUNSECURE('test1.mg')

x = [1, 2, 3]

db.SET('key', x)
print(db.EXISTS('key2'))
y = db.GET('key')
print(y)
# db.PRINTKEY()
db.SAVE()
db.SET('key2', 'saurabh')
z = db.GET('key2')
print('Y : ', y)
print('Z : ', z)

print(db.ALL())
db.CLEAR()
print(db.ALL())