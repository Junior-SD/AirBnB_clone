#!/usr/bin/python3
"""program called console.py that contains the entry point of the command interpreter:

> You must use the module cmd
> Your class definition must be: class HBNBCommand(cmd.Cmd):
> Your command interpreter should implement:
> quit and EOF to exit the program
> help (this action is provided by default by cmd but you should keep
it updated and documented as you work through tasks)
> a custom prompt: (hbnb)
an empty line + ENTER shouldn’t execute anything
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ The python Command line interface"""
    custom_prompt = "(hbnb)"

    def do_quit(self, line):
        """ command to quit the CLI """
        return True

    def do_EOF(self, line):
        """ QUIT cmd usin ctrl + D """
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
