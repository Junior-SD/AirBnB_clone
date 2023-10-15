#!/usr/bin/python3
"""program called console.py that contains the entry point of the
command interpreter:

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
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from models import storage

className = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'Amenity': Amenity,
        'City': City,
        'Review': Review,
        'State': State
        }


class HBNBCommand(cmd.Cmd):
    """ The python Command line interface"""
    prompt = "(hbnb) "
    className = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'Amenity': Amenity,
            'City': City,
            'Review': Review,
            'State': State
            }

    def do_quit(self, arg):
        """ command to quit the CLI """
        return True

    def do_EOF(self, arg):
        """ QUIT cmd usin ctrl + D """
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        If the class name is missing, print ** class name missing **
        If the class name doesn’t exist, print ** class doesn't exist **\
                (ex: $ create MyModel)
        """
        if not arg:
            print(" ** class name missing **")
            return
        elif arg not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        else:
            new_obj = HBNBCommand.className[arg]()
            HBNBCommand.className[arg].save(new_obj)
            print(new_obj.id)

    def do_show(self, arg):
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
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in className:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on class and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in className:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or\
                not on the class name
        """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in className:
            obj_dict = models.storage.all(className[args[0]])
        else:
            print("** class doesn't exist **")
            return
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print(f"[{', '.join(obj_list)}]")

    def do_update(self, arg):
        """update an instance based on classname, id- attribute && value
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]

        # check if instance id is missing
        if len(args) < 2:
            print("** instance id missing **")
            return

        # chck if class exist
        if class_name not in className:
            print("** class doesn't exist **")

        # CHECK IF INSTANCE EXISTS
        instance_id = args[1]
        instance_key = f"{class_name}.{instance_id}"
        if instance_key not in models.storage.all():
            print("** no instance found **")
            return

        # check if attribute name exists
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = arg[2]

        # check attribute value
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]

        # Handle data type conversions for specific attributes
        integers = ["number_rooms", "number_bathrooms", "max_guest"\
                , "price_by_night"]
        floats = ["latitude", "longitude"]
        if class_name == "Place":
            if attribute_name in integers:
                try:
                    attr_value = int(attr_value)
                except AttributeError:
                    attr_value = 0
            elif attribute_name in floats:
                try:
                    attr_value = float(attr_value)
                excepti AttributeError:
                    attr_value = 0.0

        setattr(models.storage.all()[instance_key], attribute_name, attr_value)
        models.storage.all()[instance_key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
