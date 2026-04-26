#  Ryan Josh S. Sabunod
#  BSIT - IT1R2
#  Exercise 3 - Finals: File + Error Handling

try:
    username = input("Enter Username: ")

    # Check username if letters and numbers only
    if not username.isalnum():
        print("Error: Username should contain letters and numbers only.")

    else:
        age = int(input("Enter Age: "))

        if age <= 0:
            print("Error: Age must be greater than 0.")

        else:
            with open("users.txt", "a") as file:
                file.write(username + " - " + str(age) + "\n")

            print("\nUser saved successfully!")

            print("\nSaved Users:")
            with open("users.txt", "r") as file:
                print(file.read())

except ValueError:
    print("Error: Age must be a number.")

finally:
    print("\nSystem complete.")