def lasit_failu(file_name):
    try:
        with open(file_name, 'r') as f:
            saturs = f.read()
            print("saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f" '{file_name}' nav atrasts.")
    except Exception as e:
        print(f"nevar nolasīt failu '{file_name}'.")


def main():
    file_name = input("ievadi faila nosaukumu: ")
    file_format = input("ievadi faila formātu: ")

    full_file_name = f"{file_name}.{file_format}"

    lasit_failu(full_file_name)

if __name__ == "__main__":
    main()