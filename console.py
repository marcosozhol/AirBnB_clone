#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Console Module
This module controls all databases.
Can create, modify and delete instances.
"""

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes


class_personalize = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                     "Place": Place, "Review": Review, "State": State,
                     "User": User}


class HBNBCommand(cmd.Cmd):
    """Command processor class."""
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

    def do_create(self, line):
        """Creates a new instance of a class"""
        args = shlex.split(line)
        """Split the passed arguments to interpret
        them as console commands and store them in an array
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_personalize:
            instance = class_personalize[args[0]]()
            print(instance.id)
            instance.save()
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_personalize:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                """
                En este caso si se pasan dos argumentos, concatena con punto
                para poder ejecutar la accion, ej: show User, va a ejecutar
                User.show para mostrar los datos de user.
                """
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in class_personalize:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
            """Utilizamos estos caracteres para dividir la impresion
            de cada instansia al mostrarlas todas"""
        elif args[0] in class_personalize:
            for key in models.storage.all():
                if args[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        """Creamos estas dos variables para cuando el usuario indique alguno
        de estos atributos dentro de Place, y poder actualizar sus datos a
        enteros o flotantes segun a donde corresponda"""
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in class_personalize:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                """En este caso, dado que Place tiene argumentos
                                de tipo entero y flotante, que las demas
                                clases no, entonces corroboramos que el
                                argumento se encuentre dentro de las
                                correspondientes variables que creamos
                                anteriormente y convertimos el valor pasado
                                en entero o flotante para luego guardarlo"""
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0

                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0

                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                            """Actualizamos la clase creada (ej Place) agregando solo
                            ARGS 2 y 3. De este modo, si el usuario pasa mas
                            Args al mismo tiempo, solo se actulizaran los
                            primeros."""
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
