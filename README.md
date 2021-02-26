# aruba-fabric-composer-companion
stackstorm companion platform for aruba fabric composer

NOTE:
MUST BE INSTALLED ON A HOST WITH STACKSTORM INSTALLED PRIOR!!!!!!

Install stackstorm with something like this:
```
 curl -sSL https://stackstorm.com/packages/install.sh | bash -s -- --user=st2admin
--password='Ch@ngeMe'
```


This application uses the mongo db installed by StackStorm. Since the DB is secured
you will need to log into the StackStorm mongo DB as a StackStorm admin and create a separate DB

# Companion mongengine to work with StackStorm mongo DB

log in with admin first
-------------------------------------------------------------------------------------
mongo -u admin -p UkIbDILcNbMhkh3KtN6xfr9h admin  (passwd in /etc/st2/st2.config)

# Then create a new user
db.createUser({user: "appUser",pwd: "passwordForAppUser",roles: [ { role: "readWrite", db: "app_db" } ]})

# Add creds to the Flask application.py file
```
app.config['MONGODB_SETTINGS'] = {
        'db': 'app_db',
        'host': 'localhost',
        'port': 27017,
        'username': 'appUser',
        'password': 'passwordForAppUser',
        'authentication_source': 'admin'
        }
```

Now Flask app can access the st2 mongo database installation

# Companion uses multiple mongo collections.
You may need to create the page number database manually. The app will
crash when you go to create a new entry in the user log.

If this happens do the following

# Create number collection and add a record to it.
```
mongo -u appUser -p passwordForAppUser admin
> use app_db
> db.createCollection('number')
> db.number.insertOne({num:1})
> db.number.find()
{ "_id" : ObjectId("5cc84e276e9abf31a65a5f1f"), "num" : 1 }
