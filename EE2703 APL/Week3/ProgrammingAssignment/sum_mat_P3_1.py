def mean(x, axis=0):
    if axis == 0:
        x_zipped = zip(*x) # The * argument, unpacks the matrix!, it passes each row (a list) as an argument! 
        summed_columns = []
        for x_r in x_zipped:
            summed_columns.append(sum(x_r)/len(x))
        return summed_columns
        # return summed_columns
    elif axis == 1:
        summed_rows = [sum(r)/len(r) for r in x]
        return summed_rows
    
print(mean([[1,2],[3,4],[5,6]],0))