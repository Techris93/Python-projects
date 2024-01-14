def convert_to_snake_case(pascal_or_camel_cased_string):
    """
    Convert a Pascal or Camel cased string to snake case.

    Args:
    pascal_or_camel_cased_string (str): The input string in Pascal or Camel case.

    Returns:
    str: The input string converted to snake case.
    """
    snake_cased_char_list = [
        # Add '_' and convert to lowercase if the character is uppercase
        '_' + char.lower() if char.isupper()
        # Otherwise, keep the character as is
        else char
        # Iterate through each character in the input string
        for char in pascal_or_camel_cased_string  ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    """
    Test the convert_to_snake_case function by printing the result for a sample input.
    """
    print(convert_to_snake_case('IAmAPascalCasedString'))

if __name__ == '__main__':
    main()
