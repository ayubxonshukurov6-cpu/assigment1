email = input("Email kiriting: ")

if email.endswith("@gmail.com") or email.endswith("@yahoo.com") or email.endswith("@outlook.com"):
    if "@" in email:
        print("Email to'g'ri!")
    else:
        print("Xato format!")
else:
    print("Noto'g'ri elektron pochta manzili!")