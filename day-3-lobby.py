def main():
    test_input = "939800232324"

    #Read the input file
    with open("day-3-input.txt", "r") as file:
        battery_banks = [line.strip() for line in file.readlines()]
    
    total_output = 0
    # Find the highest battery
    for bank in battery_banks:
        top_joltage = [0, 0]
        for battery_idx in range(len(bank)):
            battery = int(bank[battery_idx])
            if battery > top_joltage[0] and battery_idx < len(bank) - 1:
                top_joltage[0] = battery
                top_joltage[1] = 0
            elif battery > top_joltage[1]:
                top_joltage[1] = battery
        print(bank)
        print(top_joltage)
        print(top_joltage[0]*10 + top_joltage[1])
        total_output += top_joltage[0]*10 + top_joltage[1]
    print(f"Total Output: {total_output}")
    
    
    
if __name__ == "__main__":
    main()
    
    
    2525252122335344154213543554324533232121114451542423242331144254232355335331541343523141344524346789