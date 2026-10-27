GRADE_CATEGORIES = ("Distinction", "Merit", "Pass", "Fail")

def validate_score():
  while True:
    try:
      score = float(input("Enter Python score (0-100): "))
      if 0 <= score <= 100:
        return score
      print("Error: Score must be between 0 and 100. Please try again.")
    except ValueError:
      print("Error: Invalid input. Please enter a numerical value.")


def classify_grade(score):
  if score >= 85:
    return GRADE_CATEGORIES[0]
  elif score >= 70:
    return GRADE_CATEGORIES[1]
  elif score >= 50:
    return GRADE_CATEGORIES[2]
  else:
    return GRADE_CATEGORIES[3]


def calculate_average(students):
  if not students:
    return 0.0
  total_score = sum(student["score"] for student in students)
  return total_score / len(students)


def count_passing(students, passing_threshold=50):
  passing_count = 0
  for student in students:
    if student["score"] >= passing_threshold:
      passing_count += 1
  return passing_count


def display_report(students):
  print("\n" + "=" * 70)
  print(f"{'STUDENT PERFORMANCE REPORT':^70}")
  print("=" * 70)
  print(
      f"{'Name':<15} | {'Age':<5} | {'Study Hours/Wk':<14} | {'Score':<6} |"
      f" {'Grade Category':<15}"
  )
  print("-" * 70)

  for student in students:
    grade = classify_grade(student["score"])
    print(
        f"{student['name']:<15} | {student['age']:<5} |"
        f" {student['study_hours']:<14.1f} | {student['score']:<6.1f} |"
        f" {grade:<15}"
    )

  print("-" * 70)
  avg_score = calculate_average(students)
  total_passing = count_passing(students)
  total_students = len(students)

  print(f"Total Students Evaluated: {total_students}")
  print(f"Class Average Python Score: {avg_score:.2f}")
  print(
      f"Passing Students (Score >= 50): {total_passing} out of"
      f" {total_students}"
  )
  print("=" * 70)


def main():
  students = []
  print("--- Python Student Performance Management System ---")
  print("Please provide records for at least 5 students.\n")
  for i in range(1, 6):
    print(f"--- Student {i} of 5 ---")
    name = input("Enter student name: ").strip()
    if not name:
      name = f"Student {i}"

    while True:
      try:
        age = int(input("Enter age: "))
        if age > 0:
          break
        print("Age must be greater than 0.")
      except ValueError:
        print("Please enter a valid integer for age.")

    while True:
      try:
        study_hours = float(input("Enter weekly study hours: "))
        if study_hours >= 0:
          break
        print("Study hours cannot be negative.")
      except ValueError:
        print("Please enter a valid number for study hours.")

    score = validate_score()

    student_record = {
        "name": name,
        "age": age,
        "study_hours": study_hours,
        "score": score,
    }
    students.append(student_record)
    print("-" * 40)
  display_report(students)


if __name__ == "__main__":
  main()