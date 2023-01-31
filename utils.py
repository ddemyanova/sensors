import pymongo

connection_string = 'mongodb+srv://marykvitka:marykvitka123@cluster0.sgqnr87.mongodb.net/?retryWrites=true&w=majority'
db_name = 'sensorsDB'

# Створити зв'язок з клієнтом
try:
    client = pymongo.MongoClient(connection_string)
except:
    print('Error connecting to client.\n')
    quit()
else:  
    print ('Connected to client.\n')

# Вивести список баз даних та їх кількість
database_list = client.list_database_names()
print ('Database_list:', database_list, '\n')
print ('Number of databases:', len(database_list), '\n')

# Вивести список всіх несистемних колекцій у базі даних
db = client[db_name]
filter = {'name': {'$regex': r'^(?!system\.)'}}
print('Collection names in database', db_name, ':\n', db.list_collection_names(filter=filter), '\n')

# Створити колекцію, якщо з такою назвою ще не існує
collection_name = 'humiditySensors'
if collection_name in db.list_collection_names():
    print('Collection', collection_name, 'have been already created.\n')
else:
    col = db.create_collection(
        name=collection_name,
        codec_options=None,
        read_preference=None,
        write_concern=None,
        read_concern=None,
        session=None,
    )
    print ('Collection', col.name, 'has been created now.\n')
    
# Вставити один документ в колекцію
collection = db[collection_name]
dict_hum = { 'name': 'HIH9120-021-001S', 'company': 'Honeywell', 'resolution': 14 , 'price': 46.20 }
ins = collection.insert_one(dict_hum)

# Переглянути ідентифікатор вставленого документа в колекції
print('Documents in collection', collection.name, ':\n', collection.find_one(), '\n')
print('Id of inserted document:', ins.inserted_id, '\n')

# Вставити декілька документів в колекцію
list_hum = [{ 'name': 'SHT75', 'company': 'Sensirion', 'resolution': 12, 'price': 27.73 },
            { 'name': 'SHT15', 'company': 'Sensirion', 'resolution': 12, 'price': 21.21 }]
print('Documents in collection', collection.name, ':\n', list(collection.find()), '\n')

# Переглянути ідентифікатори вставлених документів в колекції
ins2 = collection.insert_many(list_hum)
print('Documents in collection', collection.name, ':\n', list(collection.find()), '\n')
print('Ids of inserted documents:', ins2.inserted_ids, '\n')

# Переглянути документи, де ціна більше 27
query = {"price": {"$gt": 27}}
print("Price > 27:", list(collection.find(query)))

# Змінити один документ
hum_query = { 'name': 'SHT75', 'company': 'Sensirion', 'resolution': 12, 'price': 27.73 }
hum_new = {'$set': { 'name': 'SHT75', 'company': 'Sensirion', 'resolution': 12, 'price': 29.73 }}
collection.update_one(hum_query, hum_new)
print('Document in collection was updated\n', list(collection.find()), '\n')

# Змінити декілька документів
hum_query = { 'company': 'Sensirion' }
hum_new = { '$set': {'price': 30 }}
upd = collection.update_many(hum_query, hum_new)
print('Documents in collection', collection.name, ':\n', list(collection.find()), '\n')
print(upd.modified_count, 'documents updated.\n')

# Видалити один та всі документи
collection.delete_one({ 'name' : 'HIH9120-021-001S' })
one_doc = collection.find_one({ 'name' : 'HIH9120-021-001S' })
print('Deleted document with the name HIH9120-021-001S is', one_doc,'.\n')
collection.delete_many({})
print('All documents deleted.\n')

# Видалити колекцію, якщо існує
if collection.name in db.list_collection_names():
    print ('Collection', collection.name, 'dropped.\n')
    db[collection.name].drop()

# Закрити зв'язок з клієнтом
client.close()
print ('Connection to client is closed.\n')
