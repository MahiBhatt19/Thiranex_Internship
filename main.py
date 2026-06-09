import re
def password_strength_analyzer(password):
    check = [] 
    if " " in password:
        check.append("No Spaces Allowed")

    if len(password) < 8:
        check.append("Password must contain atleast 8 characters")
    
    if len(password) > 20:
        check.append("Password must contain atmost 20 characters") 

    if not re.search("[A-Z]", password):
        check.append("Password must contain atleast 1 capital letter")

    if not re.search("\\d", password):
        check.append("Password must contain atleast 1 number")  

    if not re.search("[!@#$%^&*()_+-=?~<>]", password):
        check.append("Password must contain atleast one of these: !@#$%^&*()_+-=?~<>")

    if len(check) == 0:
        if len(password) >= 8 and len(password) <= 11:
             return "🟥 Password is Easy"
        elif len(password) >= 12 and len(password) <= 15:
            return "🟨 Password is Medium"
        else:
            return "🟩 Password is Strong"
    else:
        return check


password = input("Enter your password: ")
result = password_strength_analyzer(password)
if isinstance(result, list):
    print("\n❌ Password is INVALID\n")
    for issue in result:
        print(" -", issue)
else:
    print(result)


