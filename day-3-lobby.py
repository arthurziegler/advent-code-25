def main():
    #Read the input file
    with open("day-3-input.txt", "r") as file:
        battery_banks = [line.strip() for line in file.readlines()]
    
    total_output = 0
    # Find the highest battery
    for bank in battery_banks:
        top_joltage = [0, 0]
        for idx, battery in enumerate(bank):
            battery = int(battery)
            if battery > top_joltage[0] and idx < len(bank) - 1:
                top_joltage[0] = battery
                top_joltage[1] = 0
            elif battery > top_joltage[1]:
                top_joltage[1] = battery
        #print(top_joltage[0]*10 + top_joltage[1])
        total_output += top_joltage[0]*10 + top_joltage[1]
    print(f"Total Output: {total_output}")
    
    
    
if __name__ == "__main__":
    main()
