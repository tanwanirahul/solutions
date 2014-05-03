'''
Created on 03-May-2014

@author: rahul
'''


def fibo_gen(upper_bound):
    '''
        Generates fibo series for even valued items.
    '''
    second_last = 0
    last = 1
    count = 0
    while count < upper_bound:
        current = second_last + last
        count += 1
        second_last = last
        last = current
        print current, " "
        if current % 2 == 0:
            yield current

if __name__ == "__main__":
    upper_bound = 1000
    print "Sum: ", sum(fibo_gen(upper_bound))
