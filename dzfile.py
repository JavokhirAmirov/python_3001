#import os
from urllib.parse import urlparse
def parssite(fil):
    for i in fil:
        z = urlparse(i)
        l = {z.scheme, i}
    print(l)
    fil.close()

fil = open(input("Input file name: "), 'r')
parssite(fil)

#fsffs
