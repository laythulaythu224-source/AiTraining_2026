#def greet():
#   print("Hello! Welcome to the program.")
#   print("Ucspyay")
#greet()

#def greet_student(name):
#    print(f"Hello, {name}!")
#greet_student("Aung Aung")
#greet_student("Su Su") 

#def calculate_average(scores):
#    if len(scores) == 0:
#        return 0
#    return sum(scores)/len(scores)
#marks = [70,80,90]
#result = calculate_average(marks)
#print(result)

def classify_score(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"
print(classify_score(90))
print(classify_score(55))
print(classify_score(25))

def count_pass_fail(scores):
    numberPass = 0
    numberFail = 0
    for score in scores:
        if score >= 40:
            numberPass += 1
        else:
            numberFail += 1
    return numberPass, numberFail
print(count_pass_fail([90, 55, 25,60,34,20,73,45,80,100,30]))