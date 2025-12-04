def main():
    #Read the input file
    with open("day-3-input.txt", "r") as file:
        battery_banks = [line.strip() for line in file.readlines()]
    
    total_output = 0
    BATTERY_SIZE = 12
    
    # Find the highest battery
    for bank in battery_banks:
        # Create a dictionary in the format: {on_idx: [bank_idx, joltage]}
        online_battery = [[0,0] for _ in range(BATTERY_SIZE)]
        prev_slot_idx = 0
        bank_output = ''
        
        #Find each of the twelve batteries that need to be online
        for slot_idx in range(BATTERY_SIZE):
            #Battery to turn on will be chosen from the following sub-string of bank
            slice_end = -(BATTERY_SIZE - slot_idx)+1
            if slice_end == 0:
                slice_end = None
            valid_bank_win = bank[prev_slot_idx:slice_end]
            
            #Loop through the sub-string of bank
            for win_idx, battery in enumerate(valid_bank_win, start=prev_slot_idx):
                battery = int(battery)
                if battery > online_battery[slot_idx][1]:
                    online_battery[slot_idx][0] = win_idx
                    online_battery[slot_idx][1] = battery
                    prev_slot_idx = win_idx + 1
                    
            bank_output += str(online_battery[slot_idx][1])
            
        total_output += int(bank_output)

        
        
        # # Part 1 solution
        # for idx, battery in enumerate(bank):
        #     battery = int(battery)           
        #     if battery > top_joltage[0] and idx < len(bank) - 1:
        #         top_joltage[0] = battery
        #         top_joltage[1] = 0
        #     elif battery > top_joltage[1]:
        #         top_joltage[1] = battery
  
    print(f"Total Output: {total_output}")
    
    
    
if __name__ == "__main__":
    main()