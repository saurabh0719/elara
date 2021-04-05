import elaradb

db = elaradb.RUN('test.mg')

x = [1, 2, 3]

db.SET('key', x)
print(db.EXISTS('key2'))
y = db.GET('key')
print(y)
db.SAVE()