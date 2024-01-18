def lasit_failu(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            saturs = f.read()
            

            print("saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f" '{file}' Neatradu .")
    except Exception as e:
        print(f"Kļūdījies {e}")


faila_ceļš = 'fails.txt'
lasit_failu(faila_ceļš)