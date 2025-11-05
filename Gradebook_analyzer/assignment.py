#Name = Naman
#Roll=2501350018
#Title=Gradebook analyzer

import csv

gradebook = {}


f = open("gradebook.csv", "a+")
f.seek(0)
reader = csv.reader(f)
for row in reader:
    if row:
        name = row[0]
        marks = list(map(float, row[1:]))
        gradebook[name] = marks
f.close()

while True:
    print("\n1. Add Student Data")
    print("2. Show All Data")
    print("3. Show Passed Students")
    print("4. Show Failed Students")
    print("5. Exit")

    a= input("Enter choice: ")

    if a == "1":
        while True:
            name = input("\nEnter student name (or 'done' to stop): ")
            if name.lower() == "done":
                break

            marks = []
            for i in range(1, 5):
                marks.append(float(input(f"Enter marks for Subject {i}: ")))
            gradebook[name] = marks

        f = open("gradebook.csv", "w", newline="")
        writer = csv.writer(f)
        for name, marks in gradebook.items():
            writer.writerow([name] + marks)
        f.close()

        print("\nStudent data added and saved successfully!")

    elif a == "2":
        if not gradebook:
            print("\nNo data available!")
        else:
            print("\n" + "=" * 70)
            print(f"{'Name':<12}{'Sub1':<8}{'Sub2':<8}{'Sub3':<8}{'Sub4':<8}{'Avg':<8}{'Grade':<8}{'Result':<8}")
            print("=" * 70)

            for name, marks in gradebook.items():
                avg = sum(marks) / len(marks)
                grades = []

                for n in marks:
                    if n >= 90:
                        grades.append("A")
                    elif n >= 80:
                        grades.append("B")
                    elif n >= 70:
                        grades.append("C")
                    elif n >= 60:
                        grades.append("D")
                    elif n >= 50:
                        grades.append("E")
                    else:
                        grades.append("F")

                if avg >= 90:
                    avg_grade = "A"
                elif avg >= 80:
                    avg_grade = "B"
                elif avg >= 70:
                    avg_grade = "C"
                elif avg >= 60:
                    avg_grade = "D"
                elif avg >= 50:
                    avg_grade = "E"
                else:
                    avg_grade = "F"

                result = "PASS" if avg_grade in ["A", "B", "C", "D"] else "FAIL"

                print(f"{name:<12}{marks[0]:<8}{marks[1]:<8}{marks[2]:<8}{marks[3]:<8}"
                      f"{avg:<8.1f}{avg_grade:<8}{result:<8}")

            print("=" * 70)

    elif a== "3":
        print("\nPassed Students:")
        found = False
        for name, marks in gradebook.items():
            avg = sum(marks) / len(marks)
            if avg >= 60:
                print(name)
                found = True
        if not found:
            print("None")

    elif a== "4":
        print("\nFailed Students:")
        found = False
        for name, marks in gradebook.items():
            avg = sum(marks) / len(marks)
            if avg < 60:
                print(name)
                found = True
        if not found:
            print("None")

    elif a == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")