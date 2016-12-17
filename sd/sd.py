# aim: calculate the standard deviation of a bunch of values
# input: a bunch of values,a list
# output: the standard deviation of these values, numerical

def standard_deviation(x):

    n = len(x)
    mean = sum(x) / n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    return(stdev)

standard_error = lambda x: standard_deviation(x)/len(x)**0.5
