import csv


def filter_survivors():
  survivors = []
  with open("titanic.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
      if int(row["survived"]) == 1:
        survivors.append(row)
  return survivors


def save_survivors():
  survivors = filter_survivors()
  if not survivors:
    return
  fieldnames = survivors[0].keys()
  with open("survived.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(survivors)