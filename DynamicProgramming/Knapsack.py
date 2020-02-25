def Knapsack(C, W, V):    # C: 배낭 용량, W: 물건 무게, V: 물건 가치
    n = len(W)    # 물건의 개수
    K = [ [0 for i in range(C+1)] for i in range(n+1)]    # 각 물건에 대한 가치를 저장할 2차원 배열 0으로 초기화
    
    for i in range(1,n+1) :            # 각 물건을 순회
        for w in range(1,C+1) :        # 배낭의 (임시)용량을 순회, 마지막에는 w = C가 되어 배낭의 용량이 됨.
            if(W[i-1] > w) :           # 물건의 무게가 임시 배낭의 용량을 초과하면
                K[i][w] = K[i-1][w]    # 물건을 배낭에 못 담음
            else :                     # 물건의 무게가 현재 배낭의 용량보다 같거나 작으면
                K[i][w] = max(K[i-1][w], K[i-1][w-W[i-1]] + V[i-1])    # 물건을 배낭에 담아 가치를 추가함
    print(K)
    return K[n][C]

def main() :
    C = int(input("배낭의 용량은? "))    # 배낭 용량
    W = [ 2, 3, 4, 5 ]                   # 물건 무게
    V = [ 30, 40, 50, 60 ]               # 물건 가치
    print("배낭에 담을 수 있는 물건의 최대 가치:",Knapsack(C, W, V))             # 배낭 용량, 물건 무게, 물건 가치
main()
