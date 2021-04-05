import elaradb

db = elaradb.load('test.mg')

x = [1, 2, 3]

db.SET('key', x)

y = db.GET('key')
print(y)
db.SAVE()