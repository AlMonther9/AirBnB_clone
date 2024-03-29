#!/usr/bin/python3
"""Console module for managing the HBNB project."""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the functionality of the HBNB console."""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false."""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformats the command line for advanced command syntax."""
        if '.' in line and '(' in line and ')' in line:
            try:
                cls, _, args = line.partition('.')
                cmd, _, params = args.partition('(')
                if cmd not in self.dot_cmds:
                    raise ValueError
                params = params.rstrip(')').strip()
                if params:
                    if params[0] == '{' and params[-1] == '}' \
                            and type(eval(params)) is dict:
                        args = params
                    else:
                        args = params.replace(',', '').replace('\"', '')
                line = ' '.join([cmd, cls, args])
            except ValueError:
                pass
        return line

    def postcmd(self, stop, line):
        """Prints if isatty is false."""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, line):
        """Terminate the HBNB console."""
        exit()

    def help_quit(self):
        """Displays the help documentation for quitting the console."""
        print("Exits the program with formatting\n")

    def do_EOF(self, line):
        """Processes EOF to exit the program."""
        print()
        exit()

    def help_EOF(self):
        """Displays the help documentation for handling EOF."""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the emptyline method of the CMD class."""
        pass

    def do_create(self, args):
        """Creates an instance of any class."""
        if not args:
            print("** class name missing **")
            return
        elif args not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """Provides help information for the create method."""
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Display an individual object."""
        cls, _, obj_id = args.partition(" ")

        if not cls:
            print("** class name missing **")
            return

        if cls not in self.classes:
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        key = cls + "." + obj_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Provides help information for the show command."""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Remove a specified object."""
        cls, _, obj_id = args.partition(" ")

        if not cls:
            print("** class name missing **")
            return

        if cls not in self.classes:
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        key = cls + "." + obj_id

        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Assistance details for the remove command"""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Display all objects of a class"""
        if args:
            cls = args.split(' ')[0]
            # exclude any potential additional arguments
            if cls not in self.classes:
                print("** class doesn't exist **")
                return
            x = storage._FileStorage__objects.items()
            print_list = [str(v) for k, v in x
                          if k.split('.')[0] == cls]
        else:
            y = [str(v) for v in storage._FileStorage__objects.values()]
            print_list = y

        print(print_list)

    def help_all(self):
        """Assistance details for the entire command"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Determine the present count of class instances"""
        count = sum(1 for k in storage._FileStorage__objects.keys()
                    if k.split('.')[0] == args)
        print(count)

    def help_count(self):
        """Assistance details for the tally command"""
        print("Counts the current number of class instances")
        print("[Usage]: count <className>\n")

    def do_update(self, args):
        """Revises a specific object with updated information"""
        cls, _, obj_id, *args = args.split()

        if not cls:
            print("** class name missing **")
            return

        if cls not in self.classes:
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        key = cls + "." + obj_id

        if key not in storage.all():
            print("** no instance found **")
            return

        if not args:
            print("** attribute name missing **")
            return

        if len(args) < 2:
            print("** value missing **")
            return

        attr_name = args[0]
        attr_val = args[1]

        if attr_name in self.types:
            attr_val = self.types[attr_name](attr_val)

        obj = storage.all()[key]
        setattr(obj, attr_name, attr_val)
        obj.save()

    def help_update(self):
        """Assistance details for the refresh command"""
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
