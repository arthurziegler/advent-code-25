import numpy as np
import pandas as pd

def main():
    fresh_ranges = pd.read_csv("day-5-input.txt", sep='-', nrows=190, dtype=int, header=None)
    fresh_ranges.columns = ['lower_bound', 'upper_bound']
    ingredient_list = pd.read_csv("day-5-input.txt", skiprows=190, header=None).squeeze()
    #print(fresh_ranges)
    #print(ingredient_list)
    #print(type(fresh_ranges))
    #print(type(ingredient_list))
    
    print(ingredient_list.apply(item_in_range, args=(fresh_ranges,)).sum())
    
       
def item_in_range(item, range_df):
    valid_ranges = range_df[(item >= range_df['lower_bound']) &
                            (item <= range_df['upper_bound'])]
    return (not valid_ranges.empty)
    
if __name__ == "__main__":
    main()