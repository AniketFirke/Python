def WERTYU(input_string):
    keyboard_layout = {
        "`": "1", "1": "2", "2": "3", "3": "4", "4": "5", "5": "6", "6": "7", "7": "8", "8": "9", "9": "0", "0": "-", "-": "=",
        "q": "w", "w": "e", "e": "r", "r": "t", "t": "y", "y": "u", "u": "i", "i": "o", "o": "p", "p": "[", "[": "]", "]": "\\",
        "a": "s", "s": "d", "d": "f", "f": "g", "g": "h", "h": "j", "j": "k", "k": "l", "l": ";", ";": "'", "'": "`",
        "z": "x", "x": "c", "c": "v", "v": "b", "b": "n", "n": "m", "m": ",", ",": ".", ".": "/"
    }
    output_string = ""
    for char in input_string:
        if char in keyboard_layout:
            output_string += keyboard_layout[char]
        else:
            output_string += char
    return output_string

input_string = input("Enter a string: ")
print("Output string: ", WERTYU(input_string))