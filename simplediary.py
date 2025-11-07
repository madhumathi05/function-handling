def write_entry():
    entry = input("Write your diary entry: ")
    with open("diary.txt", "a") as file:
        file.write(f"{entry}\n")

write_entry()
