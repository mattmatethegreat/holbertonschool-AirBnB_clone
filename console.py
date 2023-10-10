#!/usr/bin/python3
""" Command Line Interpreter """

import shlex
import cmd
from models import storage
from models.amenity import Amenity

class HBNBCommand(cmd.Cmd):
    """ Initializing Console """
    prompt = "(HBNB) "

    def do_quit(self, arg):
        """ """
        return True

    def help_quit(self):
        """ """
        print("Quit the command interpreter")

    def do_create(self, arg):
        """ """
        if not arg:
            print("** class name missing **")
            return

        classes = {"User": User, "Place": Place} #
        class_name = arg.split()[0]

        if class_name in classes:
            instance = classes[class_name]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """ """
        print("Create a new instance of a class. Usage: create <class_name>")

    def do_all(self, arg):
        """List all instances of a class"""
        classes = {"User": User, "Place": Place} #

        if not arg:
            instances = []
            for cls_name, cls in classes.items():
                instances += cls.all()
            print([str(instance) for instance in instances])
            return

        class_name = arg.split()[0]

        if class_name in classes:
            instances = classes[class_name].all()
            print([str(instance) for instance in instances])
        else:
            print("** class doesn't exist **")

        def help_all(self):
            """Help message for the all command"""
            print("List all instances of a class. Usage: all [class_name]")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
