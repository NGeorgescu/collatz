def reduce(n, out='listed'):
    """
    Reduces an integer or list of integers down to 1
    
    Parameters
    ----------
    n : int or list
        collapses a down, see returned for the attributes of the returned values
        
    out:
        'listed' returns either a list or list of lists from n to 1.
        'graph' returns all connecting tuples for all n
        'dist' returns just the distance or list of distances from n to 1

    Examples
    --------
    >>> reduce(3)
    [3, 10, 5, 16, 8, 4, 2, 1]

    >>> reduce(3, out='dist')
    8

    >>> reduce(range(4),out='graph')
    [[16, 8], [10, 5], [8, 4], [5, 16], [4, 2], [3, 10], [2, 1]]    

    >>> reduce(4,out='graph')
    [[4, 2], [2, 1]]

    """
    if isinstance(n,int):
        l = [n]
        while n>1:
            if n%2==0:
                n=n//2
            else:
                n=3*n+1
            l+=[n]
        if out =='listed':
            return l
        elif out=='graph':
            return [l[i:i+2] for i in range(len(l)-1)]
        elif out=='dist':
            return len(l)
        else:
            raise Exception('invalid output selected')
    else:
        try:
            iter(n)
        except:
            raise Exception('n is not iterable and not an int')
        else:
            if out =='listed':
                return [reduce(i) for i in n]
            elif out=='graph':
                l = []
                [[l.append(j) for j in reduce(i,out='graph') if j not in l] for i in n]
                return sorted(l,key=lambda x:x[0],reverse=True)
            elif out=='dist':
                return [reduce(i,out='dist') for i in n]
            else:
                raise Exception('invalid output selected')



def tree(n, start=1):
    """
    builds a tree to depth n starting at the desired value
    
    Examples
    --------
    
    >>>tree(4)
    [[1, 2], [2, 4], [4, 8], [8, 16]]
    
    >>>tree(5)
    [[1, 2], [2, 4], [16, 5], [4, 8], [8, 16], [16, 32]]
    
    >>>tree(6)
    [[1, 2], [2, 4], [16, 5], [4, 8], [5, 10], [8, 16], [16, 32], [32, 64]]

    """
    l = []
    new_last = [start]
    for i in range(n):
        last, new_last = [new_last, []]
        for old_val in last:
            l.append([old_val,old_val*2])
            new_last.append(old_val*2)
            new_val = (old_val-1)/3
            if new_val>1 and new_val%1==0:
                l.append([old_val,int(new_val)])
                new_last.append(int(new_val))
        
    return sorted(l,key=lambda x:x[1])


