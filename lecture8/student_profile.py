student = {
    "name": "Ana",
    "contacts": {
        "email": "ana@example.com",
        "phone": "555-1234"
    },
    "courses": {
        "python": {
            "score": 90,
            "passed": True
        },
        "web": {
            "score": 50,
            "passed": False
        }
    }
}

print("Email:", student["contacts"]["email"])
print("Python score:", student["courses"]["python"]["score"])

student["courses"]["web"]["passed"] = True
student["courses"]["web"]["score"] = 65

student["contacts"].pop("phone")

print("Updated student profile:", student)