


def name():
    pass

def tag():
    pass

def tags():
    pass



COMMAND_HANDLER = {
    "name": name,
    "tag": tag,
    "tags": tags,
    "exit": exit
}

def main():
    while True:
        user_input = input("Input command >>> ")
        if user_input == "exit":
            break


if __name__ == "__main__":
    main()
