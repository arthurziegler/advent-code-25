import numpy as np
import pandas as pd

def main():
    #Read for task 1
    worksheet_task1 = pd.read_csv("day-6-input.txt", sep='[ ]+', header=None)
    
    #Read for task 2
    with open("day-6-input.txt", 'r') as file:
        worksheet_lines = file.readlines()
        
    worksheet_task2 = pd.Series(worksheet_lines).str.split('', expand=True).loc[:, 1:3693]
    worksheet_task2[3694] = [' ',' ',' ',' ', ' ']
    problem_start = 1
    
    #Find each cephalopod math problem for task 2
    answer_task2 = 0
    for col_id, column in worksheet_task2.items():
        #Check if a columns is all spaces, boundary between math problems
        if (column == ' ').all():
            answer_task2 += cephalopod_calc(worksheet_task2.loc[:, problem_start:col_id-1])
            problem_start = col_id+1
            
    print(f"TASK 1 ANS: {worksheet_task1.apply(math_calc).sum()}")
    print(f"TASK 2 ANS: {answer_task2}")
    
def math_calc(math_problem):
    op = math_problem.loc[4]
    ans = 0
    if op == '+':
        ans = math_problem.loc[0:3].astype(int).sum()
    elif op == '*':
        ans = math_problem.loc[0:3].astype(int).product()
    return ans

def cephalopod_calc(math_problem):
    op = math_problem.iloc[4, 0]
    math_nums = math_problem.loc[:3]
    ans = 0 if op == '+' else 1
    for col_name, col in math_nums.items():
        num = int(col.str.cat(sep=''))
        if op == '+':
            ans += num
        elif op == '*':
            ans *= num
    return ans
    
    
if __name__ == "__main__":
    main()