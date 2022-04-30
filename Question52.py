#Question10
mod=10000000000000
n=int(input("Enter the leement number: "))


def fibo_odd(n):
    Sum=[0]*(n+1);
    Sum[0] = 0;
    Sum[1] = 1;
    Sum[2] = 2;
    Sum[3] = 5;
    Sum[4] = 10;
    Sum[5] = 23;

    for i in range(6,n+1):
        Sum[i] = ((Sum[i - 1] +
                    (4 * Sum[i - 2]) % mod -
                    (4 * Sum[i - 3]) % mod +
                    mod) % mod + (Sum[i - 4] -
                    Sum[i - 5] + mod) % mod) % mod;
    
    print(Sum[n])
    return Sum[n];
fibo_odd(n)
    


