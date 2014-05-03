'''
Created on 03-May-2014

@author: rahul
'''


def add_multiples_of_3_and_5(upper_limit):
    '''
        Returns multiples of 3 and 5
    '''
    data = (x for x in xrange(upper_limit) if x % 3 == 0 or x % 5 == 0)
    return sum(data)

if __name__ == "__main__":
    upper_bound = 1000
    print "Sum : ", add_multiples_of_3_and_5(upper_bound)
