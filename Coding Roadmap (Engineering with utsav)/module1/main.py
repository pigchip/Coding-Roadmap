# Module 1 - String manipulation and formatting
# Project  - Case Converter
"""
Examples:
    convert("Hello, World.", "camel")
    Output: helloWorld

    convert("Hello, World.", "snake")
    Output: hello_world

    convert("Hello, World.", "kebab")
    Output: hello-world

    convert("Hello, World.", "pascal")
    Output: HelloWorld

    convert("Hello, World.", "uppercasesnake")
    Output: HELLO_WORLD
"""


def convert(text, case):  # Convert Function
    flag = 0
    result = list('')

    """
        __camel algorithm__
            1.- Go through every char of 'text'
            2.- Ignore any char except letters
            3.- If is an uppercase change it to lowercase for the first word
            4.- Repeat until find a char of separation (space,tab,comma,_,-)
            5.- The next word should start with an uppercase and then lowercase
    """
    if case == 'camel':
        for element in text:
            is_letter = element.isupper() | element.islower()
            if is_letter:
                if flag:
                    flag = 0
                    result.append(element.upper())
                else:
                    result.append(element.lower())
            else:
                flag = 1
    """
        __snake algorithm__
            1.- Go through every char in text
            2.- Make all letters lowercase
            3.- Anything that isn't a letter make it an underscore
    """
    if case == 'snake':
        for element in text:
            is_letter = element.isupper() | element.islower()
            if is_letter:
                if flag:
                    flag = 0
                    result.append('_')
                result.append(element.lower())
            else:
                flag = 1
    """
        __kebab algorithm__
            1.- Go through every element on 'text'
            2.- Make all letters lowercase
            3.- Any char that isn't a letter change it to a hyphen
    """
    if case == 'kebab':
        for element in text:
            is_letter = element.isupper() | element.islower()
            if is_letter:
                if flag:
                    flag = 0
                    result.append('-')
                result.append(element.lower())
            else:
                flag = 1
    """
        __pascal algorithm__
            1.- Go through every element on text
            2.- Ignore anything that isn't a letter
            3.- Each word must start with a capital letter
    """
    if case == 'pascal':
        first = 1
        for element in text:
            is_letter = element.isupper() | element.islower()
            if is_letter:
                if first == 1:
                    result.append(element.upper())
                    first = 0
                else:
                    result.append(element.lower())
            else:
                first = 1
    """
        __uppercase snake algorithm__
            1.- Go through every char in 'text'
            2.- Make all letters uppercase
            3.- Non-letters make them only one underscore
    """
    if case == 'uppercasesnake':
        for element in text:
            is_letter = element.isupper() | element.islower()
            if is_letter:
                if flag:
                    flag = 0
                    result.append('_')
                result.append(element.upper())
            else:
                flag = 1
    result = ''.join(result)
    print(result)


if __name__ == '__main__':  # Main Function
    convert("Hello, World.", "uppercasesnake")  # Test
