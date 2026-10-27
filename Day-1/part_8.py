# student_scores = [70,85,90,65,78]

# print(student_scores)
# print(student_scores[0])
# print(student_scores[1])
# print(student_scores[2])
# print(student_scores[3])
# print(student_scores[4])

scores = [70, 85, 90, 65, 78]
scores.append(95)
print(scores)

scores[0] = 75
print(scores)

scores.remove(85)
print(scores)

print("Count:", len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))

scores = [55, 80, 35, 90, 65]
for score in scores:
    if score >= 80:
        print(score)
        
location = (16.8, 96.15)
print("Latitude:", location[0])
print("Longitude:", location[1])
print("Number of values:", len(location))