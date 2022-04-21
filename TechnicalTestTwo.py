import cli_ui
import argparse

import models

parser = argparse.ArgumentParser(description="Basic CRUD for personal data management")
parser.add_argument('-o', '--operation', type=str, choices=['create', 'read', 'update', 'delete'], default='create',
                    required=False, help='CRUD operation to perform')

args = parser.parse_args()

cli_ui.setup(verbose=True, color='always')

if args.operation == 'create':
    names = cli_ui.ask_string("Type the names of the person: ")
    last_name = cli_ui.ask_string("Enter the person's last name: ")
    age = cli_ui.ask_string("Enter the age of the person: ")
    email = cli_ui.ask_string("Enter the person's email: ")
    person = models.Person(
        names=names,
        last_name=last_name,
        age=age,
        email=email
    )
    cli_ui.info(cli_ui.green, person.save())
elif args.operation == 'read':
    option = cli_ui.ask_string("Do you want to list all people?: y or n")
    persons = models.Objects()
    if option == 'y' or option == 'Y':
        cli_ui.info(cli_ui.blue, persons.get_person())
    elif option == 'n' or option == 'N':
        option = cli_ui.ask_string("Enter the person's id: ")
        cli_ui.info(cli_ui.blue, persons.get_person(id=float(option)))
    else:
        cli_ui.error(cli_ui.red, 'Option not valid')
elif args.operation == 'update':
    id = cli_ui.ask_string("Type the id of the person: ")
    names = cli_ui.ask_string("Type the names of the person: ")
    last_name = cli_ui.ask_string("Enter the person's last name: ")
    age = cli_ui.ask_string("Enter the age of the person: ")
    email = cli_ui.ask_string("Enter the person's email: ")
    person = models.Person(
        names=names,
        last_name=last_name,
        age=age,
        email=email
    )
    cli_ui.info(cli_ui.blue, person.update(id=float(id)))
else:
    option = cli_ui.ask_string("Enter the person's id: ")
    persons = models.Objects()
    cli_ui.info(cli_ui.blue, persons.delete_person(id=float(option)))

