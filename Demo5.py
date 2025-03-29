def simulate_hartals(days, parties, hartal_parameters):
    total_days = int(days)
    party_count = int(parties)
    hartal_parameters = [int(x) for x in hartal_parameters.split()]
    hartals = [0] * total_days
    for h in hartal_parameters:
        for i in range(h - 1, total_days, h):
            day = i % 7
            if day != 5 and day != 6:
                hartals[i] = 1
    return sum(hartals)

def main():
    test_cases = int(input("Enter the number of test cases: "))
    for _ in range(test_cases):
        days = input("Enter the number of days: ")
        parties = input("Enter the number of political parties: ")
        hartal_parameters = input("Enter the hartal parameters separated by space: ")
        lost_days = simulate_hartals(days, parties, hartal_parameters)
        print("Total lost days:", lost_days)

if __name__ == "__main__":
    main()

