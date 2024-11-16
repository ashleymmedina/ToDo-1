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
 

def create():
    userinput == input("Enter your todo: ")
    db.insert({'todo' : userinput})
    print("Todo made successfully!!!")

def read():
    allData = db.all()
    for data in allData:
        print(f'Todo {data.doc_id} : {data["todo"]}')


while True:
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    userinput = input("Enter your command: ")

    if userinput == 'Create' or '1':
        userinput == input("Enter the task you want to add: ")
        create()

    if userinput == 'Read' or '2':
        read()

    if userinput == 'Update' or '3':
        userinput == input("Insert what you would you like to replace: ")
        update = db.update(("todos"), userinput == '')
        update()

    if userinput == 'Delete' or '4':
        userinput == input("Insert what you would like to remove: ")
        delete = db.remove(todos.todo == userinput)
        delete()


    
           
    



