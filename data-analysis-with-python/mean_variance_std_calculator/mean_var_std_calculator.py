import numpy as np

def calculate(list):

    nlist = np.array(list).reshape(3,3)
    
    row_0 = nlist[0]
    row_1 = nlist[1]
    row_2 = nlist[2]

    nlist  = nlist.T

    col_0 = nlist[0]
    col_1 = nlist[1]
    col_2 = nlist[2]


    calculations = {
        'mean': [[np.mean(col_0), np.mean(col_1), np.mean(col_2)], [np.mean(row_0), np.mean(row_1), np.mean(row_2)], np.mean(list)],
        'variance': [[np.var(col_0), np.var(col_1), np.var(col_2)], [np.var(row_0), np.var(row_1), np.var(row_2)], np.var(list)],
        'standard deviation': [[np.std(col_0), np.std(col_1), np.std(col_2)], [np.std(row_0), np.std(row_1), np.std(row_2)], np.std(list)],
        'max': [[np.max(col_0), np.max(col_1), np.max(col_2)], [np.max(row_0), np.max(row_1), np.max(row_2)], np.max(list)],
        'min': [[np.min(col_0), np.min(col_1), np.min(col_2)], [np.min(row_0), np.min(row_1), np.min(row_2)], np.min(list)],
        'sum': [[np.sum(col_0), np.sum(col_1), np.sum(col_2)], [np.sum(row_0), np.sum(row_1), np.sum(row_2)], np.sum(list)]
    }

    print(calculations)
    return calculations



calculate([0,1,2,3,4,5,6,7,8])

'''
{
        'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
        'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
        'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
        'max': [[6, 7, 8], [2, 5, 8], 8],
        'min': [[0, 1, 2], [0, 3, 6], 0],
        'sum': [[9, 12, 15], [3, 12, 21], 36]
    }
'''