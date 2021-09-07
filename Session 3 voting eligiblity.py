# input age
age = int(input("Enter Your Age : "))

# condition to check voting eligibility
if age>=18:
        status="Eligible"
else:
    status="Not Eligible"

print("You are ",status," for Vote.")
