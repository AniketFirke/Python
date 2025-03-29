def display_lcd(number):
    digits = {
        0: [" - ", "| |", "|_|"],
        1: ["   ", "  |", "  |"],
        2: [" - ", " _|", "|_ "],
        3: [" - ", " _|", " _|"],
        4: ["   ", "|_|", "  |"],
        5: [" - ", "|_ ", " _|"],
        6: [" - ", "|_ ", "|_|"],
        7: [" - ", "  |", "  |"],
        8: [" - ", "|_|", "|_|"],
        9: [" - ", "|_|", " _|"],
    }

    lines = [""] * 3
    for digit in str(number):
        digit_lines = digits[int(digit)]
        for i, line in enumerate(digit_lines):
            lines[i] += line + " "
    
    for line in lines:
        print(line)


display_lcd(12345678910)
