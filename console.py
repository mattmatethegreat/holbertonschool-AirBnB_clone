#!/usr/bin/python3
""" Command Line Interpreter """

import shlex
import cmd
from models import storage
from models.base_model import BaseModel

class HABBCCommand(cmd.Cmd):
    """ Initializing Console """
    prompt = '(HABBC) '
    class_list = {
            "BaseModel",
            #
            #
            #
            #
            #
            #
        }

    def empty(self):
        """ Nothing happens when the line is emtpy """
        pass

    def EOF(self, *line):
        """ Quits if EOF is entered """
        print()
        return True

    def quit(self, *line):
        """ Quits the program """
        return True

    def create(self, *line):
        """ Creates a new instance of BaseModel """
