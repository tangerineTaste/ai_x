def fibonacci(n):
    a,b = 0,1
    while a < n :
        print(a, end=' ')
        a, b = b, a+b
    print()
    
def fibonacci_return(n):
    '''
    입력한 값 이하의 값들을 
    피보나치 수열로 반환하는 함수.
    '''
    a,b = 0,1
    data = list()
    while a < n:
        data.append(a)
        a, b = b, a+b 
    return data

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1: 
        n = int(sys.argv[1])
        print('1, print test : ',end='')
        fibonacci(n)
        print('2, teturn test : ', fibonacci_return(n))
    else:
        print('1, print test : ',end='')
        fibonacci(100)
        print('2, teturn test : ', fibonacci_return(100))