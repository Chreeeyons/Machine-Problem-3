import re

def custom_regex_to_python_regex(custom_regex):
    custom_regex = custom_regex.replace('+', '|')
    custom_regex = custom_regex.replace('e', '')
    custom_regex = custom_regex.replace(' ', '')
    regex = re.compile(custom_regex)
    return regex

def test_custom_regex():
    num_cases = int(input().strip())

    for _ in range(num_cases):
        custom_regex = input().strip()
        num_strings = int(input().strip())

        python_regex = custom_regex_to_python_regex(custom_regex)

        for _ in range(num_strings):
            test_string = input().replace('e', '')
            if re.fullmatch(python_regex, test_string):
                print("yes")
            else:
                print("no")

if __name__ == "__main__":
    test_custom_regex()