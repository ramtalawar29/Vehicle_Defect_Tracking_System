import sqlite3

# -------------------------------
# Database Setup
# -------------------------------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

conn.commit()


# -------------------------------
# Register Function
# -------------------------------
def register():

    print("\n========== USER REGISTRATION ==========")

    username = input("Enter Username : ")
    password = input("Enter Password : ")
    confirm = input("Confirm Password : ")

    if password != confirm:
        print("Passwords do not match!")
        return

    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES(?, ?)",
            (username, password)
        )
        conn.commit()
        print("Registration Successful.")

    except sqlite3.IntegrityError:
        print("Username already exists.")


# -------------------------------
# Login Function
# -------------------------------
def login():

    print("\n========== LOGIN ==========")

    attempts = 3

    while attempts > 0:

        username = input("Username : ")
        password = input("Password : ")

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        if user:
            print("\nLogin Successful!")
            print("Welcome,", user[1])
            return True

        else:
            attempts -= 1
            print("Invalid Username or Password")
            print("Attempts Left :", attempts)

    print("\nAccount Locked!")
    return False


# -------------------------------
# Main Program
# -------------------------------
while True:

    print("\n================================")
    print("      USER MANAGEMENT SYSTEM")
    print("================================")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("================================")

    choice = input("Enter Choice : ")

    if choice == "1":
        register()

    elif choice == "2":
        if login():
            print("\nAccess Granted.")
            # Call your Vehicle Defect Tracking System here
            # Example:
            # start_work()

    elif choice == "3":
        print("\nThank You!")
        break

    else:
        print("Invalid Choice!")

conn.close()
