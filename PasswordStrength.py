import re

def check_password_strength(password):
    # Initialize score
    score = 0
    feedback = []

    # Check the length of the password
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    elif 8 <= len(password) <= 12:
        score += 1
        feedback.append("Password length is acceptable but can be longer for more security.")
    else:
        score += 2
        feedback.append("Good password length.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Password contains uppercase letters.")
    else:
        feedback.append("Consider adding uppercase letters.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("Password contains lowercase letters.")
    else:
        feedback.append("Consider adding lowercase letters.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
        feedback.append("Password contains numbers.")
    else:
        feedback.append("Consider adding numbers.")

    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        score += 1
        feedback.append("Password contains special characters.")
    else:
        feedback.append("Consider adding special characters.")

    # Determine overall password strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Print feedback and overall strength
    print(f"Password Strength: {strength}")
    for comment in feedback:
        print(f"- {comment}")

# User input for password
password = input("Enter your password to check its strength: ")
check_password_strength(password)
