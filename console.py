#!/usr/bin/python3
""" This module isan entry point to the command interpreter """
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
    """ The commands processor beguin"""
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

