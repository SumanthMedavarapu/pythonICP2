def string_alternative(str):
    print(str)
    alter_string = str[::2]
    return alter_string
def main():
    str =input("Enter the string : ")
    print(string_alternative(str))


if __name__ == "__main__":
    main()


