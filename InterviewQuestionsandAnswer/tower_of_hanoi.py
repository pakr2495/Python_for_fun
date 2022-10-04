"""
tower of hanoi problem
3 poles s,d,h
contains n circles in source(s)
move all circle from s to d such that all larger circle should be at the bottom
"""
def cal(n,s,d,h):
    if n ==1:
        print(f'moving {n} from {s} {d}')
        return
    cal(n-1,s,h,d)
    print(f'moving {n} from {s} {d}')
    cal(n-1,h,d,s)

cal(3,1,3,2)