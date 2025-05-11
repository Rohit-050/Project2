# Project 2 : Fake Job Title Generator

import random

# Lists
adjectives = ["Global", "Certified", "Professional", "Dynamic", "Innovative", "Quantum"]
roles = ["Meme", "Cloud", "Unicorn", "AI", "Rocket", "Innovation"]
suffixes = ["Strategist", "Engineer", "Guru", "Consultant", "Architect", "Ninja"]

def generate_job_title():
    adj = random.choice(adjectives)
    role = random.choice(roles)
    suffix = random.choice(suffixes)
    return f"{adj} {role} {suffix}"

# Generate and display
while True:
    print("\nYour Fake Job Title is:")
    print(generate_job_title())

    # Ask user to continue or not
    again = input("\nDo you want another title? (Yes/No): ").strip().lower()
    if again != "yes":
        print("Thanks for using the Fake Job Title Generator!")
        break