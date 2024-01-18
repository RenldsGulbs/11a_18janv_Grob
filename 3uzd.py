def lasit_trešo_rindu(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r', encoding='utf-8') as fails:
            rinda = fails.readlines()
            if len(rinda) >= 3:
                print(rinda[2])
            else:
                print("failā mazāk par 3 rindām.")
    except Exception as e:
        print(f"kļūda: {e}")


lasit_trešo_rindu('fails2.txt')