import random

answers = ["Можно", "Нельзя", "Попробуй ещё раз", "Плохо", "Хорошо", "Отлично"]

def generate_answer():
    random_index = random.randint(0, len(answers)-1)
    return answers[random_index]

print("Добро пожаловать в Волшебный шар!")
print("Задайте свой вопрос и получите ответ.")
while True:
    question = input("Ваш вопрос: ")
    if question.lower() == "выход":
        break
    else:
        answer = generate_answer()
        print("Ответ: " + answer)
