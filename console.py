#!/usr/bin/python3
""" This module is entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """ The commands processor """
    prompt = "(EAF)"
    lst_classes = ['BaseModel', 'User', 'Amenity',
                   'Place', 'City', 'State', 'Review']
    lst_cmd = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """ Parses command input """
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cmd = cls[1].split('(')
            args = cmd[1].split(')')
            if (
                    cls[0] in HBNBCommand.lst_classes
                    and cmd[0] in HBNBCommand.lst_cmd
            ):
                arg = cmd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def emptyline(self):
        """ Do nothing when empty line present """
        pass

    def do_count(self, clss_name):
        """ Count number of instances of a class """
        counter = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == clss_name:
                counter = counter + 1
        print(counter)

    def do_create(self, type_model):
        """ Creates an instance according to a given class """
        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.lst_classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[type_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ Shows string representation of an instance passed """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        if args[0] not in HBNBCommand.lst_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Delete an instance passed """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        if args[0] not in HBNBCommand.lst_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Print string represention of all instances of a given class """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        if args[0] not in HBNBCommand.lst_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                if obj_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """ Update an instance based on the class name and id """
        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)
        if args[0] not in HBNBCommand.lst_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                obj_name = objc.__class__.__name__
                obj_id = objc.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
