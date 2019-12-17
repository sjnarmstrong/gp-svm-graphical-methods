from multiprocessing import Pool

def f(x):
    return x, x*x

if __name__ == '__main__':
    p=Pool(10)
    
    a,d=zip(*p.map(f,range(100)))
    print(a)
    print("____")
    print(d)
        
        