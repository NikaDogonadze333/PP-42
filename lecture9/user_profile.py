def create_user_profile(first_name, last_name, role="Student", is_active=True):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        "is_active": is_active
    }


print(create_user_profile("Nino", "Beridze"))
print(create_user_profile("Giorgi", "Kapanadze", role="Admin", is_active=False))