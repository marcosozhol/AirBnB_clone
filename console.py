#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Console Module
This module controls all databases.
Can create, modify and delete instances.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """command processor class."""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program.
        """
        return True
    def emptyline(self):
        """
        When an empty line is entered in response to the prompt,
        it won't repeat the last nonempty command entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
