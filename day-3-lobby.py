def main():
    test_input = "939800232324"

    #Read the input file
    with open("day-3-input.txt", "r") as file:
        battery_banks = [line.strip() for line in file.readlines()]
    
    total_output = 0
    # Find the highest battery
    for bank in battery_banks:
        top_joltage = (0, 0)
        for battery_idx in range(len(bank)):
            battery = int(bank[battery_idx])
            if battery_idx < len(bank):
                if battery > top_joltage[0]:
                    top_joltage[0] = battery
                    top_joltage[1] = 0
            if battery <= top_joltage[0] and battery > top_joltage[1]:
                top_joltage[1] = battery
            print()
        total_output += int(top_joltage[0] + top_joltage[1])
            
if __name__ == "__main__":
    main()