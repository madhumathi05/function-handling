def save_user_data(name, age):
    with open("user_data.txt", "a") as file:
        file.write(f"{name},{age}\n")

save_user_data("Madhu", 22)
