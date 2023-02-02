"""
                   1
                 1   1
               1   2   1
             1   3   3   1
           1   4   6   4   1
         1   5  10  10   5   1
       1   6  15  20  15   6   1
     1   7  21  35  35  21   7   1
   1   8  28  56  70  56  28   8   1
 1   9  36  84  126 126 84  36   9   1

0: [0 1 0]
1: [0 1 1 0]
2: [0 1 2 1 0]
3: [0 1 3 3 1 0]
4: [0 1 4 6 4 1 0]

"""

# Version 1

def print_pascal_triangle(height: int):
    pascals_tri = [[0, 1, 0]]
    for i in range(height-1):
        pascals_tri.append(gen_next_row(pascals_tri[i], len(pascals_tri[i])))
    padding_size = find_max_num_len_of_array(pascals_tri)+2
    
    # Remove zeros
    pascals_tri = [[x for x in row if x!=0] for row in pascals_tri]
    
    # Padding numbers
    for i, row in enumerate(pascals_tri):
        for j, number in enumerate(row):
            pascals_tri[i][j] = str(number).center(padding_size)
        pascals_tri[i] = "".join(pascals_tri[i])
    
    # Centre row
    tri_width = len(max(pascals_tri))
    for row in range(len(pascals_tri)):
        pascals_tri[row] = pascals_tri[row].center(tri_width)
        print(pascals_tri[row])
    
    
def gen_next_row(previous_row, row_length):
    current_row = [0]*row_length
    for index in range(len(current_row)-1):
        current_row[index] = previous_row[index] + previous_row[index+1]
    current_row.insert(0, 0)
    return current_row

def find_max_num_len_of_array(array, global_max=0):
    for row in array:
        local_max = len(str(max(row)))
        if local_max > global_max:
            global_max = local_max
    return global_max

print_pascal_triangle(10)
print_pascal_triangle(5)
