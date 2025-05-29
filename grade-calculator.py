def grade_call(percentage):
    if percentage >= 95:
        return "YOU PASSED YOUR CLASS WITH A+ GRADE"
    elif percentage >= 90:
        return "YOU PASSED YOUR CLASS WITH A GRADE"
    elif percentage >= 85:
        return "YOU PASSED YOUR CLASS WITH B+ GRADE"
    elif percentage >= 70:
        return "YOU PASSED YOUR CLASS WITH B GRADE"
    elif percentage >= 60:
        return "YOU PASSED YOUR CLASS WITH C GRADE"
    elif percentage >= 50:
        return "YOU PASSED YOUR CLASS WITH D GRADE"
    elif percentage >= 33:
        return "YOU PASSED YOUR CLASS WITH E GRADE"
    else:
        return "SORRY TO SAY!! YOU FAILED!!!!"

def get_marks(subjects):
    return sum(int(input(f"Enter marks for {s} (out of 100): ")) for s in subjects)

def class_10():
    subjects = ["English", "SST", "Math", "Hindi", "Science", "Computer"]
    percent = get_marks(subjects) / 600 * 100
    print(f"Your percentage: {percent:.2f}%")
    print(grade_call(percent))

def class_12():
    print("1. PCM\n2. PCM+Bio\n3. PCB\n4. Commerce\n5. Arts")
    stream = int(input("Choose stream: "))
    if stream == 1:
        subjects = ["Physics", "Chemistry", "Maths", "English", "Optional"]
        div = 500
    elif stream == 2:
        subjects = ["Physics", "Chemistry", "Maths", "Biology", "English", "Optional"]
        div = 600
    elif stream == 3:
        subjects = ["Physics", "Chemistry", "Biology", "English", "Optional"]
        div = 500
    elif stream == 4:
        subjects = ["Accountancy", "Business", "Economics", "English", "Optional"]
        div = 500
    elif stream == 5:
        subjects = ["History", "Political Science", "Geography", "English", "Optional"]
        div = 500
    else:
        print("Invalid stream")
        return
    percent = get_marks(subjects) / div * 100
    print(f"Your percentage: {percent:.2f}%")
    print(grade_call(percent))

def main():
    print("1. Class 10\n2. Class 12\n3. Other Class")
    choice = int(input("Enter your choice: "))
    if choice == 1 or choice == 3:
        class_10()
    elif choice == 2:
        class_12()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
