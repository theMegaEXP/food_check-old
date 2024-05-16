

class Print:
    def red(text):
        print(f"\033[91m{text}\033[0m")
    
    def orange(text):
        print(f"\033[33m{text}\033[0m")

    def yellow(text):
        print(f"\033[93m{text}\033[0m")

    def green(text):
        print(f"\033[92m{text}\033[0m")

    def blue(text):
        print(f"\033[94m{text}\033[0m")

    def purple(text):
        print(f"\033[95m{text}\033[0m")

    def bold(text):
        print(f"\033[1m{text}\033[0m")

    def underline(text):
        print(f"\033[4m{text}\033[0m")

    def underline_bold(text):
        print(f"\033[1;4m{text}\033[0m")

    def key_value(key, value):
        print(f"\033[1m{key}\033[0m: {value}")

Print.red("Hello there")
Print.orange("Hello there")
Print.yellow("Hello there")
Print.green("Hello there")
Print.blue("Hello there")
Print.purple("Hello there")
Print.bold("This text is bold")
Print.key_value("This is a key", "This is a value")
Print.underline("This is underlined")
Print.underline_bold("This is underlined and bold!!!")