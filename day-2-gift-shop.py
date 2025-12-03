import pandas as pd

def main():
    #Read the input file
    ranges_df = pd.read_csv("day-2-input.txt", header=None)
    ranges = ranges_df.T.iloc[:,0].to_list()
    invalid_sum = 0
    
    for invalid_range in ranges:
        ranges = invalid_range.split('-')
        #print(ranges[0], ranges[1])
        for product_id in range(int(ranges[0]), int(ranges[1])):
            if is_invalid_id(product_id):
                invalid_sum += product_id

    print(invalid_sum)

def is_invalid_id(product_id):
    product_id = str(product_id)
    id_size = len(product_id) 
    
    divisors = get_number_divisors(id_size)
    
    for divisor in divisors:
        parts = [product_id[i:i+divisor] for i in range(0, id_size, divisor)]
        #print(parts)
        if all(parts[0] == x for x in parts):
            return True
    return False
        
def get_number_divisors(number):
    divisors = []
    for divisor in range(1,(number//2) + 1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors

if __name__ == "__main__":
    main()