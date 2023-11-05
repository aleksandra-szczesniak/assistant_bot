contacts = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: No such contact."
        except ValueError:
            return "Error: Invalid input."
        except IndexError:
            return "Error: No contacts in memory."
    return wrapper


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"New contact added: {name} - {phone}"


@input_error
def change_phone(name, new_phone):
    contacts[name] = new_phone
    return f"Phone number updated for {name}"


@input_error
def get_phone(name):
    phone = contacts[name]
    return f"Phone number for {name}: {phone}"


@input_error
def show_all_contacts():
    if not contacts:
        return "No saved contacts."
    contact_list = "\n".join(
        [f"{name}: {phone}" for name, phone in contacts.items()])
    return contact_list


def main():
    print("Hello! How can I help you?")

    while True:
        command = input("Enter the command: ").strip().lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            _, name, phone = command.split(maxsplit=2)
            result = add_contact(name, phone)
            print(result)
        elif command.startswith("change"):
            _, name, new_phone = command.split(maxsplit=2)
            result = change_phone(name, new_phone)
            print(result)
        elif command.startswith("phone"):
            _, name = command.split(maxsplit=1)
            result = get_phone(name)
            print(result)
        elif command == "show all":
            result = show_all_contacts()
            print(result)
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Unknown command. Available commands: hello, add ..., change ..., phone ..., show all, good bye, close, exit")


if __name__ == "__main__":
    main()
