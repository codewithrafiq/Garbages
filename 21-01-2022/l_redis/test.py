# import redis


# r = redis.Redis(host='localhost', port=6379)


# r.set('name', 'Rafiq')
# r.set('age', '22')
# r.set('address', 'Dhaka')

# print(r.get('name'))
# print(r.get('age'))
# print(r.get('address'))




# r.mset({'name': 'Rafiq', 'age': '22', 'address': 'Dhaka'})
# print(r.mget('name', 'age', 'address'))



# if (r.exists("name")):
#     print("name exists", r.get("name"))
# else:
#     print("name does not exist")





# r.psetex('name', 1000, 'Rafiq')
# r.psetex('age', 1000, '22')
# r.psetex('address', 1000, 'Dhaka')

# print(r.pttl('name'))
# print(r.pttl('age'))
# print(r.pttl('address'))






