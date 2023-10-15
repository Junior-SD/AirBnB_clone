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
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """ The python Command line interface"""
    custom_prompt = "(hbnb) "
    className = {
            'BaseModel': BaseModel
            'User': User
            'Place': Place
            'Amenity': Amenity
            'City': City
            'Review': Review
            'State': State
            }

    def do_quit(self, line):
        """ command to quit the CLI """
        return True

    def do_EOF(self, line):
        """ QUIT cmd usin ctrl + D """
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        If the class name is missing, print ** class name missing **
        If the class name doesn’t exist, print ** class doesn't exist **\
                (ex: $ create MyModel)
        """
        if not line:
            print (" ** class name missing **")
            return
        elif line not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        else:
            new_obj = HBNBCommand.className[line]()
            HBNBCommand.className[arg].save(new_obj)
            print(new_obj.id)

    def do_show(self, line):
        """ Prints the string representation of an instance based on the\
        class name and id. Ex: $ show BaseModel 1234-1234-1234
        If the class name is missing, print ** class name missing **\
                (ex: $ show)
        If the class name doesn’t exist, print ** class doesn't exist **\
                (ex: $ show MyModel)
        If the id is missing, print ** instance id missing **\
                (ex: $ show BaseModel)
        If the instance of the class name doesn’t exist for the id, print 
        ** no instance found ** (ex: $ show BaseModel 121212)
        """
        line = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
            return False
        if line[0] in className:
            if len(line) > 1:
                key = line[0] + "." + line[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on class and id """
        line = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        if line[0] in className:
            if len(line) > 1:
                key = line[0] + "." + line[1]
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
