import os
import sys
import datetime

OS_NAME = "MauroOS"
VERSION = "1.0"

current_dir = os.getcwd()


def cmd_help(args):
    print("Available commands:")
    print(" help - shows this help")
    print(" dir - lists files in the current folder")
    print(" cd <folder> - changes folder")
    print(" cls - clears the screen")
    print(" time - shows the current time")
    print(" echo <txt> - writes text")
    print(" exit - exits the system")
    print(" calc - opens a simple calculator")


def cmd_dir(args):
    global current_dir

    try:
        files = os.listdir(current_dir)
        for f in files:
            print(f)
    except Exception as e:
        print("Error listing directory:", e)


def cmd_cd(args):
    global current_dir
    if not args:
        print("Usage: cd <folder>")
        return

    new_path = os.path.join(current_dir, args[0])

    if os.path.isdir(new_path):
        current_dir = new_path
    else:
        print("Folder not found:", args[0])


def cmd_cls(args):
    os.system("cls" if os.name == "nt" else "clear")


def cmd_time(args):
    now = datetime.datetime.now()
    print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))


def cmd_echo(args):
    print(" ".join(args))


def cmd_exit(args):
    print("Exiting", OS_NAME)
    sys.exit(0)


def cmd_calc(args):
    print("Simple calculator. Write expressions (e.g., 2+3*4) or 'exit' to return.")

    while True:
        expr = input("calc> ")

        if expr.lower() in ["exit", "exit", "quit"]:
            break

        try:
            resultado = eval(expr)
            print("=", resultado)
        except Exception as e:
            print("Invalid expression:", e)


COMMANDS = {
    "help": cmd_help,
    "dir": cmd_dir,
    "cd": cmd_cd,
    "cls": cmd_cls,
    "time": cmd_time,
    "echo": cmd_echo,
    "exit": cmd_exit,
    "calc": cmd_calc,
}


def main():
    cmd_cls([])
    print(f"{OS_NAME} {VERSION}")
    print("Enter 'help' to see commands. \n")

    while True:
        prompt = f"{OS_NAME}:{current_dir}> "
        line = input(prompt)

        if not line.strip():
            continue
        parts = line.strip().split()
        cmd = parts[0].lower()
        args = parts[1:]
        if cmd in COMMANDS:
            try:
                COMMANDS[cmd](args)
            except Exception as e:
                print("Error executing command:", e)
        else:
            print("Unrecognized command:", cmd)


if __name__ == "__main__":
    main()
