def main():
    print("Day 1: Secret Entrance")
    
    #Read the input file
    with open("day-1-input.txt", "r") as file:
        instructions = [line.strip() for line in file.readlines()]
    print(instructions)
    
    current_pos = 50
    instruct_n = 0
    zero_positions = 0
    
    print(f"The dial starts by pointing at {current_pos}")
    for instruction in instructions:
        instruct_n += 1
        direction, turns = read_instruction(instruction)
        
        #if abs(turns) >= 100:
        #    turns = normalize_turns(turns)
        
        if direction == 'R':
            current_pos = current_pos + turns
        else:
            current_pos = current_pos - turns
            
        if current_pos >= 100:
            current_pos = current_pos - 100
        elif current_pos < 0:
            current_pos = current_pos + 100
        
        if current_pos == 0:
            zero_positions += 1
            print(f"The dial is rotated {instruction} to point at {current_pos} at instruction number: {instruct_n}")
    
    print(f"The password is: {zero_positions}")
            
        
def read_instruction(instruction):
    direction = instruction[0]
    turns = instruction[1:]
    turns = int(turns[-2:]) #Gets only the value below 100. Anything above is just a full turn of the dial.
    return direction, turns


if __name__ == "__main__":
    main()
