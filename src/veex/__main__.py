from veex.modules.banner import output_banner
import veex.modules.commands as commands

# THE main loop
def main():
    output_banner()

    while True:
        user_input = input("> ").strip()
        is_cmd, command = commands.is_command(user_input)

        if is_cmd and callable(command):
            result = command(user_input)

            if result is not None:
                print(result)
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
