import csv

def filter_companies():
    companies = []
    with open("ssl_companies.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["Number of employees"]) > 1000:
                companies.append({
                    "Name": row["Name"],
                    "Industry": row["Industry"],
                    "Number of employees": row["Number of employees"]
                })
    return companies

def save_companies():
    companies = filter_companies()
    if not companies:
        return
    fieldnames = ["Name", "Industry", "Number of employees"]
    with open("sorted_companies.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(companies)