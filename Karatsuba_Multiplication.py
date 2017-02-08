# Karatsuba Multiplication


def karatsuba(x,y):
    # x*y = 10**n (ac) + 10**(n/2) ( ad + bc ) + bd
    # ad + bc = (a+b)(c+d) -ac -bd
    
    # Set n
    n = max(len(str(x)),len(str(y)))
    
    if n <= 1: # Base case
        return x*y
    else:
        # Compute a,b,c,d
        a = x / 10**(n/2)
        b = x % 10**(n/2)
        c = y / 10**(n/2)
        d = y % 10**(n/2)
        # Compute ac, bd, adbc
        ac = karatsuba(a,c)
	bd = karatsuba(b,d)
	ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        return ( (10**(2*(n/2))) * ac + (10**(n/2)) * ad_plus_bc + bd )


def main():
    x,y = 12345,56789
    print "\nx = %d\ty = %d\n%d * %d = %d" % (x,y,x,y,karatsuba(x,y))
    x, y = 123456789, 987654321
    print "\nx = %d\ty = %d\n%d * %d = %d" % (x,y,x,y,karatsuba(x,y))
    # Check algorithm correctness
    assert 12345 * 56789 == karatsuba(12345,56789)
    assert 123456789 * 987654321 == karatsuba(123456789,987654321)

if __name__ == '__main__':
    main()    