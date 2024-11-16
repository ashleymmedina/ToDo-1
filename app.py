from tinydb import TinyDB, Query

db = TinyDB('./db.json')

todos = Query()

# mydata = db.search(user.name == 'John')
# add = db.insert({'name'} )
# delete = db.remove(user.name == 'John')
# update = db.update({'name' : 'Jane Jim'}, user.name == 'Jane')

# create
# read
# update
# delete

# def create():
#    userinput == input("Enter your command: ")
 

# def read():
#     get.userdata 

while True:
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")

    userinput = input("Enter your command: ")

    if userinput == 'Create':
        userinput == input("Enter the task you want to add: ")

    if userinput == 'Update':
        userinput == input("Insert what you would you like to update: ")
        update = db.update(("userinput"), userinput == '')

    if userinput == 'Delete':
        userinput == input("Insert what you would like to remove: ")
        delete = db.remove(userinput == '')


    
           
    



