scores = []

scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)

scores.remove(45)

avg_score = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)

print(f"Average: {avg_score}, Highest: {highest}, Lowest: {lowest}")

scores.sort()
print(f"Sorted scores: {scores}")

passed_scores = [score for score in scores if score >= 60]
print(f"Passed scores: {passed_scores}")