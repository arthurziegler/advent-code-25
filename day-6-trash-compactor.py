import numpy as np
import pandas as pd

def main():
    
    worksheet = pd.read_csv("day-6-input.txt", sep='[ ]+', header=None)
    #print(worksheet.head())
    #print(worksheet.loc[:, 3])
    
    print(worksheet.apply(cephalopod_calc).sum())
    
def cephalopod_calc(math_problem):
    op = math_problem.loc[4]
    #print(math_problem.loc[0:3])
    ans = 0
    if op == '+':
        ans = math_problem.loc[0:3].astype(int).sum()
    elif op == '*':
        ans = math_problem.loc[0:3].astype(int).product()
    print(f"ANSWER: {ans}")
    return ans
    
    
    
if __name__ == "__main__":
    main()