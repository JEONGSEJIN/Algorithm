# 퀵정렬 함수
# input의 형태가 (x, y)이지만, 크기 비교는 x좌표만을 가지고 비교할 것임 
def quick_sort(S) :
    LEN = len(S)    # 주어진 점들의 집합의 길이 LEN
    if LEN > 1 :    # 주어진 점들의 집합의 길이가 1보다 크면
        pivot = S[LEN - 1]            # 주어진 점들의 집합을 나누기 위해 기준이 되는 피봇 선정
                                      # 여기선, 주어진 점들의 집합 중 맨 마지막 값이 피봇임
        left, mid, right = [], [], [] # 왼쪽, 중앙, 오른쪽 리스트 선언
        for i in range(LEN - 1) :    # 주어진 점들의 집합을 순회
            if S[i] < pivot :         # 주어진 점들 중 x좌표가 피봇보다 그 값이 작으면
                left.append(S[i])     # 왼쪽 리스트에 추가
            elif S[i] > pivot :      # 주어진 점들 중 x좌표가 피봇보다 그 값이 크면
                right.append(S[i])    # 오른쪽 리스트에 추가
            else :                   # 그 외
                mid.append(S[i])      # 중앙 리스트에 추가
        mid.append(pivot)    # 피봇은 당연히 중앙 리스트에 추가 된다.
        return quick_sort(left) + mid + quick_sort(right)    # 왼쪽, 오른쪽 리스트에 추가 점들의 집합은 또 다시 퀵정렬 시켜준다
                                                              # 왼쪽, 오른쪽 리스트를 퀵정렬 시켜준 뒤,
                                                              # 왼쪽, 중앙, 오른쪽 리스트 들을 다시 합쳐준 뒤 반환
    else :          # 주어진 점들의 집합의 길이가 1보다 작거나 같으면
        return S    # 주어진 점들의 집합 그대로 반환
    
# 두 점 a, b 사이의 최단 거리를 구해주는 함수
def dist(a, b) :
    return ((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5    # root((가로축 거리의 차이)^2 + (세로축 거리의 차이)^2) 반환

# 두 수의 크기를 비교하여 최솟값을 반환해 주는 함수
def min_dist(a, b) :
    if a < b :     # a < b 이면
        return a  # a 반환
    else :        # b < a 이면
        return b  # b 반환

# 최근접 점의 쌍을 찾아주는 함수
def ClosestPair(S) :
    LEN = len(S)    # 주어진 점들의 집합의 길이 LEN
    
    if (LEN <= 3) :      # 최근접 점의 쌍의 개수가 2개 또는 3개이면
        if (LEN == 3) :  # 최근접 점의 쌍의 개수가 3개이면
            a = dist(S[0], S[1])              # 첫 번째 점과 두 번째 점 사이의 거리 a
            b = dist(S[1], S[2])              # 두 번째 점과 세 번째 점 사이의 거리 b
            c = dist(S[2], S[0])              # 세 번째 점과 첫 번째 점 사이의 거리 c
            minDist = min_dist(a, b)          # a와 b 중 최솟값이 되는 거리 minDist
            minDist = min_dist(minDist, c)    # (a와 b 중 최솟값이 되는 거리)와 c중 최솟값이 되는 거리 minDist
            if minDist == a :      # minDist가 a라면
                S.remove(S[2])     # S에서 세 번째 점 삭제
                return S          # S 반환
            if minDist == b :      # minDist가 b라면
                S.remove(S[0])     # S에서 첫 번째 점 삭제
                return S          # S 반환
            if minDist == c :      # minDist가 c라면
                S.remove(S[1])     # S에서 두 번째 점 삭제
                return S          # S 반환
            
        if (LEN == 2) : # 최근접 점의 쌍의 개수가 2개이면
            return S    # 2개의 점 반환
        
    else :    # 최근접 점의 쌍의 개수가 4개 이상이면
        LEN_Div = len(S)//2    # 주어진 점들을 분할하기 위해 전체 점들의 수를 2로 나눔
        
        # < 주어진 점들 분할 작업 >
        SL, SR = [], []                         # 왼쪽 영역, 오른쪽 영역 리스트 선언
        if (len(S)%2 == 0) :                   # 점들의 개수가 짝수 개이면
            for i in range(LEN_Div) :          # 전체 리스트의 반절은
                SL.append(S[i])                 # 왼쪽 영역 리스트에 추가
            for j in range(LEN_Div, LEN) :     # 전체 리스트의 남은 반절은
                SR.append(S[j])                 # 오른쪽 영역 리스트에 추가

        else :                                 # 점들의 개수가 홀수 개이면 (왼쪽 리스트에 점을 한 개 더 추가해 줌)
            for i in range(LEN_Div + 1) :      # 전체 리스트의 반절은
                SL.append(S[i])                 # 왼쪽 영역 리스트에 추가
            for j in range(LEN_Div + 1, LEN) : # 전체 리스트의 남은 반절은
                SR.append(S[j])                 # 오른쪽 영역 리스트에 추가
                
        # < 왼쪽, 오른쪽, 중간 영역의 점들 중 최근접 점의 쌍 찾기 작업 >
        LeftToRight_EndPoint = SL[len(SL) - 1]  # 왼쪽 영역에서 가장 오른쪽의 점 LeftToRight_EndPoint
        RightToLeft_EndPoint = SR[0]            # 오른쪽 영역에서 가장 왼쪽의 점 RightToLeft_EndPoint

        CPL = ClosestPair(SL)   # 왼쪽 영역의 점들 중 최근접 점의 쌍을 모아둔 CPL
        CPR = ClosestPair(SR)   # 오른쪽 영역의 점들 중 최근접 점의 쌍을 모아둔 CPR

        CPLD = dist(CPL[0], CPL[1])              # 왼쪽 영역의 최근접 쌍의 거리
        CPRD = dist(CPR[0], CPR[1])              # 오른쪽 영역의 최근접 쌍의 거리
        CPCED = dist(LeftToRight_EndPoint, RightToLeft_EndPoint)   # EndPoint의 최근접 쌍의 거리

        # '왼쪽 영역의 최근접 쌍의 거리'와 '오른쪽 영역의 최근접 쌍의 거리', 'EndPoint의 최근접 쌍의 거리' 중 작은 값
        closest_dist = min_dist(CPLD, CPRD)         # '왼쪽 최근접 쌍의 거리'와 '오른쪽 최근접 쌍의 거리' 중 작은 값 closest_dist
        closest_dist = min_dist(closest_dist, CPCED)# '왼쪽 최근접 쌍의 거리와 오른쪽 최근접 쌍의 거리'와 
                                                    # 'EndPoint의 최근접 쌍의 거리' 중 작은 값

        # << 중간 영역의 점들 중 최근접 점의 쌍 찾기 >>
        xL, yL = LeftToRight_EndPoint   # 왼쪽 영역에서 가장 오른쪽의 점의 좌표 언패킹
        xR, yR = RightToLeft_EndPoint   # 오른쪽 영역에서 가장 왼쪽의 점의 좌표 언패킹

        CP = []    # 중간 영역 리스트 선언
        # EndPoint에서 closest_dist만큼 떨어진 중간 영역 찾기
        for v in S :    # 주어진 점들의 쌍 순회
            x, y = v    # 주어진 점 언패킹
            if (xL - closest_dist < x) and (x < xR + closest_dist) :    # EndPoint의 x좌표에서 closest_dist만큼 떨어진
                CP.append(v)                                             # 중간 영역에 속하는 점들 중간 영역 리스트에 추가

        # 중간 영역에 속한 점들 y-좌표로 정렬하기
        CP_Y = []                 # x-좌표와 y-좌표를 바꾼 점들을 넣을 리스트 선언
        for u in CP :             # < x, y 자리 바꿈 => '(x, y) -> (y, x)' >
            y, x = u              # 중간 영역에 속하는 점들 x-좌표와 y-좌표 바꾸어서 언패킹
            CP_Y.append((x,y))    # x-좌표와 y-좌표를 바꾼 점들을 CP_Y에 추가
        CP_Y = quick_sort(CP_Y)   # CP_Y 퀵정렬

        CPC = ClosestPair(CP_Y)   # (y-좌표로 정렬한) 중간 영역의 점들 중 최근접 점의 쌍을 모아둔 CPC
        CPCD = dist(CPC[0], CPC[1])    # 중간 영역의 최근접 쌍의 거리
        
        # << 왼쪽, 오른쪽, 중간 영역의 점들 중 최근접 점의 쌍의 거리 구하기 작업 >>
        minDist = min_dist(closest_dist, CPCD) # '왼쪽 영역의 최근접 쌍의 거리',
                                               # '오른쪽 영역의 최근접 쌍의 거리', 
                                               # 'EndPoint의 최근접 쌍의 거리' 중 작은 값 closest_dist와 
                                               # '중간 영역의 최근접 쌍의 거리'중 작은 값 minDist
        
        # 중간 영역에 속한 점들 중 최근접 점의 쌍(CPC)의 x-좌표, y-좌표 다시 자리 바꾸기
        CPC_X = []                  # x-좌표와 y-좌표를 다시 바꾼 점들을 넣을 리스트 선언 
        for z in CPC :              # < y, x 다시 자리 바꿈 => '(y, x) -> (x, y)' >
            y, x = z                # 바뀐 중간 영역에 속하는 점들 x-좌표와 y-좌표 바꾸어서 언패킹
            CPC_X.append((x,y))     # x-좌표와 y-좌표를 다시 바꾼 점들을 CP_X에 추가
        CPC_X = quick_sort(CPC_X)   # CPC_X 퀵정렬

        # << 왼쪽, 오른쪽, 중간 영역의 점들 중 최근접 점의 쌍 구하기 작업 >>
        if minDist == CPLD :    # minDist가 CPLD(왼쪽 영역의 최근접 쌍의 거리)라면
            return CPL          # 왼쪽 영역의 점들 중 최근접 점의 쌍을 모아둔 CPL 반환
        if minDist == CPRD :    # minDist가 CPRD(오른쪽 영역의 최근접 쌍의 거리)라면
            return CPR          # 오른쪽 영역의 점들 중 최근접 점의 쌍을 모아둔 CPR 반환
        if minDist == CPCD :    # minDist가 CPCD(왼쪽 영역의 최근접 쌍의 거리)라면
            return CPC_X        # 중간 영역의 점들 중 최근접 점의 쌍을 모아둔 CPC_X 반환

def main():
    # 주어진 점들의 집합 S
    S = [ (10,15), (5,15), (20,3), (6,1), (9,7), (15,9), (8,15), (20,14),
         (17,13), (16,11), (7,12), (10,10), (1,19), (8,8), (30,9), (22,4) ]
    print("주어진 점들의 집합:", S, "\n")    # 주어진 점들 출력    
    S = quick_sort(S)    # 주어진 점들 퀵정렬
    print("S에 있는 점들 중 최근접 점의 쌍:", ClosestPair(S), "\n")    # 주어진 점들 중 최근접 점의 쌍 출력
    # 주어진 점들 중 최근접 점의 쌍의 거리 출력
    print("S에 있는 점들 중 최근접 점의 쌍의 거리:", dist(ClosestPair(S)[0],ClosestPair(S)[1]), "\n")

main()
