<div align="center">
  <h1>HBNB - The Console <img src="https://cdn-icons-png.flaticon.com/128/6821/6821173.png" width=60 align=center> </h1>
  <h6>
    <a href="https://github.com/AlMonther9/simple_shell#Description-">Description</a>
    ·
    <a href="https://github.com/AlMonther9/simple_shell#Examples-">Examples</a>
    ·
    <a href="https://github.com/AlMonther9/simple_shell#Alternative-Syntax-">Alternative Syntax</a>
    .
    <a href="https://github.com/AlMonther9/simple_shell#usage-">Usage</a>
  </h6>
  <img src="https://img.shields.io/github/repo-size/AlMonther9/simple_shell?color=E1927F&labelColor=1a1e29&style=for-the-badge">
</div>

## Description <img src="https://cdn-icons-png.flaticon.com/128/1903/1903496.png" width=45 align=center>

The HBNB project is a student project aimed at creating a clone of the Airbnb website. The initial stage of this project focuses on developing a backend interface, or console, to manage program data. The console allows users to perform various operations such as creating, updating, and destroying objects, as well as managing file storage. To ensure persistence between sessions, the project uses JSON serialization/deserialization for data storage.

## Examples <img src="https://cdn-icons-png.flaticon.com/128/781/781103.png" width=50 align=center>
Examples
Primary Command Syntax
Example 0: Create an object
Usage: create <class_name>

(hbnb) create BaseModel
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
Example 1: Show an object
Usage: show <class_name> <_id>

(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
Example 2: Destroy an object
Usage: destroy <class_name> <_id>

(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
Example 3: Update an object
Usage: update <class_name> <_id>

(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)

## Alternative Syntax <img src="https://cdn-icons-png.flaticon.com/128/3051/3051633.png" width=45 align=center>
Alternative Syntax
Example 0: Show all User objects
Usage: <class_name>.all()

(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)

(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)

(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, )

(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]


## Usage <img src="https://cdn-icons-png.flaticon.com/512/3123/3123008.png" width=50 align=center>

First, clone this repository.

Once the repository is cloned, locate the `console.py` file and run it as follows:

```bash
/AirBnB_clone$ ./console.py
```

When this command is run, the following prompt should appear:

```
(hbnb)
```

This prompt indicates that you are in the "HBnB" console. There are a variety of commands available within the console program.

Commands:

- `create`: Creates an instance based on a given class.
- `destroy`: Destroys an object based on class and UUID.
- `show`: Shows an object based on class and UUID.
- `all`: Shows all objects the program has access to, or all objects of a given class.
- `update`: Updates existing attributes of an object based on class name and UUID.
- `quit`: Exits the program (EOF will as well).

Alternative Syntax:

Users are able to issue a number of console commands using an alternative syntax:

Usage: `<class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])`

Advanced syntax is implemented for the following commands:

- `all`: Shows all objects the program has access to, or all objects of a given class.
- `count`: Returns the number of object instances by class.
- `show`: Shows an object based on class and UUID.
- `destroy`: Destroys an object based on class and UUID.
- `update`: Updates existing attributes of an object based on class name and UUID.

## Authors <img src="https://cdn-icons-png.flaticon.com/128/2463/2463510.png" width=50 align=center>

* AlMonther Abdulhafeez <a href="https://github.com/AlMonther9" a>
<br>

> Project developed during the [Alx, Holberton School](https://www.holbertonschool.com/) program.