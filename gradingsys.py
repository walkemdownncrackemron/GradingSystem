from itertools import count
from logging import exception
from math import trunc

def show_history() -> None:
    print("\n*** Average score of students ***")

def get_names_score() -> tuple[list[str], list[float]]:
    while True:
        try:
            student_count = int(input("Num of students: "))
            if student_count <= 0:
                print("Please enter a num greater than 0")
                continue
            break
        except ValueError:
            print("Invalid input")
    
    names_of_students = []
    scores = []
    print("\nEnter student names and scores:")
    
    for i in range(student_count):
        name = input(f"Student {i + 1} name: ").strip()
        if not name:
            name = f"Student {i + 1}"
        names_of_students.append(name)
        
        while True:
            try:
                score = float(input(f"Enter score for {name}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be 0-100")
            except ValueError:
                print("Invalid Input")
    
    return names_of_students, scores

if __name__ == "__main__":
    show_history()
    names, scores = get_names_score()
    if scores:
        average = sum(scores) / len(scores)
        print("\nCollected scores:")
        for name, score in zip(names, scores):
            print(f"{name}: {score}")
        print(f"\nAverage score: {average:.2f}")
    else:
        print("No scores to calculate avg.")

def calculate_average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
