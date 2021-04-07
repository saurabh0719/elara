import elaradb

db = elaradb.exe_secure('test2.mg', False)

x = [1, 2, 3]

db.set('key', x)
print(db.exists('key2'))
y = db.get('key')
print(y)
# db.PRINTKEY()
# db.commit()
db.set('key2', 'saurabh')
z = db.get('key2')
print('Y : ', y)
print('Z : ', z)
print(db.retmem())
db.commit()
db.exportdb('export.json')
db.clear()
print(db.retmem())



# print(db.retall())
# y = [45, 65, 7]

# p = {
#     "Hello" : "Saurabh",
#     "age" : 22,
#     "somelist" : y
# }

# db.set('key4', p)
# db.commit()
# print(db.retdb())



# dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
# {'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]
# print(db.get('key1'))
# print(db.get('key2'))
# print(db.retall)
# print(db.retdb)