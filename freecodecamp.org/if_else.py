answer = input("Are you a male? (yes/no): ")
answer = answer.strip().lower()
is_male = answer == "yes"

answer1 = input("Are you hardworker? (yes/no): ")
answer1 = answer1.strip().lower()
is_hardworker = answer1 == "yes"

answer2 = input("Are you a millionaire? (yes/no): ")
answer2 = answer2.strip().lower()
is_millionaire = answer2 == "yes"

if is_male and (is_hardworker or is_millionaire): 
    print("You can date my daughter.")
elif is_male and not (is_hardworker or is_millionaire):
    print("You cannot date my daughter.")
elif not is_male and (is_hardworker or is_millionaire):
    print("You can be my daughter's friend.")
else:      
    print("You cannot be my daughter's friend.")
    