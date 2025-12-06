import numpy as np
import pandas as pd

def main():
    RANGES = 190
    fresh_ranges = pd.read_csv("day-5-input.txt", sep='-', nrows=RANGES, dtype=int, header=None)
    fresh_ranges.columns = ['lower_bound', 'upper_bound']

    #Task one
    #ingredient_list = pd.read_csv("day-5-test.txt", skiprows=190, header=None).squeeze()
    #print(ingredient_list.apply(item_in_range, args=(fresh_ranges,)).sum())
    
    #Task Two
    fresh_ranges['keep_lower'] = True
    fresh_ranges['keep_upper'] = True
    
    fresh_ranges = fresh_ranges.sort_values(by='lower_bound').reset_index(drop=True)
    lower_group_bound = fresh_ranges['lower_bound'].iloc[0]
    upper_group_bound = fresh_ranges['lower_bound'].iloc[0]
    upper_group_bound_idx = 0
    for idx, row in fresh_ranges.iterrows():               
        # This row belongs to the same bounding group
        if idx > 0 and (row['lower_bound'] - upper_group_bound) <= 0:
            fresh_ranges.loc[idx, 'keep_lower'] = False
            #If this upper bound is higher than the group one, replace it.
            if row['upper_bound'] - upper_group_bound >= 0:
                fresh_ranges.loc[upper_group_bound_idx, 'keep_upper'] = False
                upper_group_bound = row['upper_bound']
                upper_group_bound_idx = idx
            else:
                fresh_ranges.loc[idx, 'keep_upper'] = False
        
        #This row does not belong to the same bounding group
        else:
            lower_group_bound = row['lower_bound']
            upper_group_bound = row['upper_bound']
            upper_group_bound_idx = idx
                
    low_list = fresh_ranges['lower_bound'][fresh_ranges['keep_lower'] == True].reset_index(drop=True).sort_values()
    high_list = fresh_ranges['upper_bound'][fresh_ranges['keep_upper'] == True].reset_index(drop=True).sort_values()
    
    print(len(low_list), len(high_list))
    fresh_id_sum = 0
    for item1, item2 in zip(low_list, high_list):
        print(f"{item1:<10} {item2} = {item2 - item1 + 1}") # Adjust <10 for desired spacing
        fresh_id_sum += item2-item1+1
        
    print(fresh_id_sum)
    
def item_in_range(item, range_df):
    valid_ranges = range_df[(item > range_df['lower_bound']) &
                            (item < range_df['upper_bound'])]
    return (not valid_ranges.empty)       
    
if __name__ == "__main__":
    main()