def save_score(name, score):
    with open("scores.txt", "a") as file:
        file.write(f"{name}:{score}\n")

def quiz():
    score = 0
    answer = input("What is the capital of India? ")
    if answer.lower() == "delhi":
        score += 1
    save_score("Madhu", score)

quiz()
