import elaradb as elara

db = elara.exe_secure("new.db", True)
db.set("Jonah", 35)
print(db.get("Jonah"))

db.set("Saurabh", "someshitt")
print(db.get("Saurabh"))


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