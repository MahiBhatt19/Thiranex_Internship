from main import password_strength_analyzer
def run_tests():
    tests = [
        "hello",             # weak
        "Hello123",          # missing symbol
        "Hello123!",         # easy password
        "Hello123!AB",       # medium password
        "Hello123!ABcd",     # strong password
        "Hello 123!",        # no space allowed
        "H3yyyyy!",          # easy password
    ]

    for pwd in tests:
        print("\nPassword: ", pwd)
        result = password_strength_analyzer(pwd)
        print("Result: ", result)

if __name__ == "__main__":
    run_tests()
