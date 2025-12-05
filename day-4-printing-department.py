import numpy as np

def main():
    #Read the input file
    # with open("day-4-input.txt", "r") as file:
    #     paper_matrix = [line.strip() for line in file.readlines()]
    #     paper_matrix = np.array(paper_matrix)
    #     print(type(paper_matrix))
        
    paper_matrix = np.genfromtxt("day-4-input.txt", delimiter=(1), dtype=str)
    #print(paper_matrix[0])
    #print(paper_matrix[0][9])
    
    available_paper_rolls = 0
    removable_rolls = True
    while removable_rolls:
        removable_rolls = False
        for i, line in enumerate(paper_matrix):
            for j, cell in enumerate(line):
                paper_count = 0
                print(f"Matrix Position: {cell} [{i},{j}]")

                if paper_matrix[i, j] == '@':
                    paper_matrix[i, j] = 'X'
                    l_start = max(i - 1, 0)
                    l_end = min(i + 2, 140)
                    c_start = max(j - 1, 0)
                    c_end = min(j + 2, 140)
                    neighborhood = paper_matrix[l_start:l_end, c_start:c_end]
                    paper_count = neighborhood.flatten()
                    paper_count = paper_count == '@'
                    paper_count = np.sum(paper_count)
                    print(f"Line:{l_start}, {l_end} Column: {c_start}, {c_end} Count = {paper_count}")
                    print(neighborhood)
                    #paper_matrix[i, j] = '@'
                    if paper_count < 4:
                        available_paper_rolls += 1
                        removable_rolls = True
                    else:
                        paper_matrix[i, j] = '@'
        print(available_paper_rolls)
    

    
    
if __name__ == "__main__":
    main()