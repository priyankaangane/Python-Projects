#Excercise 1 : 
def lists_stats(numbers):
    total = sum(numbers)
    mean = total/len(numbers)
    return{
        "Length" : len(numbers),
        "total" : total,
        #"mean" : {f"{mean}:2f"},
        "mean" : round(mean,2),
        "maximum" : max(numbers),
        "minimum" : min(numbers),
        "sorted_asec" : sorted(numbers),
        "sorted_desc" : sorted(numbers,reverse = True) #numbers.sort() changes the original list and returns None.
    }
print(lists_stats([88, 45, 92, 38, 76, 55, 61]))

#Excercise 2 :
def process_scores(scores):
    valid_scores = []

    for score in scores:
        if 0 <= score <= 100:
            valid_scores.append(score)
    ##valid_scores = [score for score in scores if 0<=score<=100]
    invalid_scores = [score for score in scores if score<0 or score>100]
    passing = [score for score in valid_scores if score >= 50]
    failing = [score for score in valid_scores if score < 50]

    return {
        "Valid": valid_scores ,
        "Invalid": invalid_scores,
        "passing": passing,
        "failing":failing
     }

print(process_scores([88, -5, 45, 110, 92, 38, 76, 101, 55]))

#Excersicse 3: Given this nested list representing a 3x3 matrix:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
def flatten(matrix):
    
    flat=[num for row in matrix for num in row]
    return flat
    
print(flatten(matrix))
    
def row_sum(matrix):
    total = [sum(row) for row in matrix]
    return total
    
print(row_sum(matrix))

def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):  #Column pos,Loop through the column positions (indexes) of the first row
        new_row = []
        
        for row in matrix: #collects that pos in every row
            new_row.append(row[i])
            
        result.append(new_row)
        #return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return result
print(transpose(matrix))
    



#NOTE : # numbers.sort() changes the original list and returns None
# sorted(numbers) returns a new list, original unchanged
















