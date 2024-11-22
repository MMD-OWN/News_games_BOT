import simplejson as json

# خواندن فایل JSON
def read_database(name_jason):
    with open(name_jason, 'r') as file:
        return json.load(file)

# نوشتن فایل JSON
def write_database(name_jason, database):
    with open(name_jason, 'w') as file:
        json.dump(database, file, indent=4)

# افزودن آی‌دی جدید
def add_new_id(name_jason, new_id):
    database = read_database(name_jason)
    
    # بررسی وجود آی‌دی
    if any(item['id'] == new_id for item in database):
        return "False"
    else:
        # حذف قدیمی‌ترین آی‌دی و افزودن آی‌دی جدید
        database.pop(0)
        #database.append({"id": new_id})
        write_database(name_jason, database)
        return "True"