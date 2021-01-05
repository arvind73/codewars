Parameters the function takes are
t: i.e., maximum sum of distances, integer >= 0 [example: 240,228,etc thats limits the total kilometers driven].
k: is number of towns to visit, k >= 1)[example: 3]
ls: is list of distances, all distances are positive or null integers and this list has at least one element.
The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null,
None, Nothing.[Example: [22,69,42,101,0]]

Logic using combinations: Use combinations() from itertools to print all combinations of specific order.
Example:
def rSubset(arr, r): 
  
    # return list of all subsets of length r 
    # to deal with duplicate subsets use set(list(combinations(arr, r))) 
    
    return list(combinations(arr, r))
    
For arr = [1, 2, 3, 4] and r = 2, we get [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

So, introduce a new variable(highest) and assign it 0. Loop through combinations(lst,max_towns) and assign another variable(total_distance)  to  sum of loop iterator.
Now apply condition to check if maximum miles number is greater than total_distance) that is greater than 'highest' initially assigned to 0. If condition is true,
highest will be replaced by total_distance value.
