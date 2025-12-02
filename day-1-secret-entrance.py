def main():
    print("Day 1: Secret Entrance")
    
    #Read the input file
    with open("day-1-input.txt", "r") as file:
        instructions = [line.strip() for line in file.readlines()]
    
    current_pos = 50
    instruct_n = 0
    zero_positions = 0
    zero_passes = 0
    
    for instruction in instructions:
        overflowed = False
        instruct_n += 1
        direction, turns, full_turns = read_instruction(instruction)
        
        zero_passes += full_turns
        
        if direction == 'R':
            new_pos = current_pos + turns
        else:
            new_pos = current_pos - turns
        
        #Treat cases when dial loops
        if new_pos >= 100:
            new_pos = new_pos - 100
            overflowed = True
        elif new_pos < 0:
            new_pos = new_pos + 100
            overflowed = True

        # Count cases when dial passes through 0 without stopping on it
        if overflowed == True and current_pos != 0:
            zero_passes += 1
        if overflowed == False and new_pos == 0:
            zero_passes += 1


        if new_pos == 0:
            zero_positions += 1
            
        current_pos = new_pos
        #print(f"The dial is rotated {instruction} to point at {new_pos} at instruction number: {instruct_n}. Full turns: {full_turns}. Overflowed: {overflowed}")
        
    print(f"The password is: {zero_positions}")
    print(f"The password using method 0x434C49434B is: {zero_passes}")

            
        
def read_instruction(instruction):
    direction = instruction[0]
    turns = instruction[1:]
    full_turns = 0
    
    if int(turns) >= 100:
        full_turns = int(turns[:-2])
    turns = int(turns[-2:]) #Gets only the value below 100. Anything above is a full turn of the dial.
    
    return direction, turns, full_turns


if __name__ == "__main__":
    main()
