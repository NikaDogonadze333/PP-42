scores = [45, 82, 67, 38, 90, 55, 72]

passing_scores = list(filter(lambda x: x >= 50, scores))
updated_scores = list(map(lambda x: min(100, x + 5), passing_scores))

print("Passing scores:", passing_scores)
print("Updated scores:", updated_scores)