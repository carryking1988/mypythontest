def hannuota(n,a,b,c):
    if n == 1:
        print(f'{a} ==> {c}')
        return None
    hannuota(n-1,a,c,b)
    print(f'{a} ==> {c}')
    hannuota(n-1,b,a,c)

if __name__ == "__main__":
    hannuota(3,"A","B","C")
