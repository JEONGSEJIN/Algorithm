from copy import deepcopy    # copy 모듈을 불러옴. 

# 작업 시간을 짧은 작업 시간을 우선으로 오름차순 정렬
def shortest_job_sort(S) :
    S_gap = []                # [ 작업 시간, [시작 시간, 종료 시간]]을 저장할 리스트 선언
    for u in S :
        a = u[0]              # 시작 시간
        b = u[1]              # 종료 시간
        S_gap.append([ b - a, u ])    # 리스트에 추가 [ 작업 시간, [시작 시간, 종료 시간]]
    S_gap.sort()              # 작업 시간에 따라 리스트 오름차순 정렬
    
    S_new = []                # 작업 시간에 따라 정렬된, 작업 시간이 들어갈 새로운 리스트
    for v in S_gap :
        S_new.append(v[1])    # 작업 시간에 따라 정렬된, 작업 시간을 새로운 리스트에 추가 [ 시작시간, 종료 시간 ]
    return S_new             # 리스트 반환

# 작업 시간을 빠른 작업 시작 시간을 우선으로 오름차순 정렬
def earlist_start_time_sort(S) :
    S.sort()    # 작업시간의 오름차순에 따라 리스트 정렬
    return S

# 두 수의 크기를 비교하여 최댓값을 반환해 주는 함수
def max_num(a, b) :
    if a < b :      # a < b 이면
        return b    # b 반환
    else :          # b < a 이면
        return a   # a 반환

# 초기의 기계 리스트의 크기를 찾아 반환해 주는 함수
def M_size(S) :
    end_Time = S[0][1]             # 맨 처음 작업의 종료 시간
    m_num = end_Time               # 전체 작업의 종료 시간 중 가장 큰 값 m_num (= 일단 첫 번째 값 할당)
    for i in range(1, len(S)) :   # 전체 작업 순회
        end_Time = S[i][1]         # 작업의 종료 시간
        m_num = max_num(m_num, end_Time)   # 가장 큰 값 = max_num(가장 큰 값, 종료 시간) 할당
    return m_num                  # 최대 종료 시간 반환
    
# 초기의 기계 리스트를 종료 시간 만큼 None으로 초기화하여, 스케줄러에 추가하여 반환해 주는 함수
def insert_Machine(S, M, M_s) :
    m = []                      # 종료 시간 만큼 None을 저장할 기계 리스트(이중리스트 안의 리스트)
    for ind in range(M_s) :    # 최대 종료 시간만큼 for문 순회
        m.append(None)         # None값으로 기계 리스트 초기화
    M.append(m)                 # 초기화된 기계 리스트 스케줄러에 추가
    return M                   # 새로운 기계 리스트가 추가된 스케줄러 반환

# 작업들의 작업 스케줄링을 반환해 주는 함수
def TaskScheduling(S) :
    M = []                          # 작업 전체를 저장할 스케줄러_(이중리스트)
    M_s = M_size(S)                 # 스케줄링의 기계리스트의 전체 길이 M_s_(리스트 사이즈)
    M = insert_Machine(S, M, M_s)   # 스케줄러에 첫 기계 리스트를 초기화하여 추가(이중리스트 안의 리스트)
    
    while(len(S) != 0):      # 작업을 모두 할당해 줄 때까지 while문 순회
        v = S.pop(0)         # 작업을 하나씩 pop()해줌
        start_Time = v[0]    # 시작 시간
        end_Time = v[1]      # 종료 시간

        # 스케줄러를 순회하면서 주어진 작업을 할당해줄 기계가 있는지 검사
        for m_num in range(0,len(M)) :                 # 스케줄러를 순회
            count = 0                                  # 기계 안에 작업이 들어갈 자리를 세어주는 count
            for i in range(start_Time, end_Time) :     # 기계 안의 가능한 자리 탐색 
                if M[m_num][i] != None :              # 작업을 수행할 기계의 자리가 없으면
                    break
                else :
                    count = count + 1                  # 기계 안에 작업이 들어갈 기계의 자리 수 하나 증가
                
            if count == (end_Time - start_Time) :    # "기계 안의 자리수 = 작업 시간" 이면
                if M[m_num][i] == None :            # 작업을 수행할 기계의 자리가 있으면
                    M = insert_Machine(S, M, M_s)    # 우선, 스케줄러에 새로운 기계를 초기화하여 추가해 줌
                j = start_Time                       # j = start_Time = 시작 시간
                while j < end_Time :                # 스케줄러를 순회
                    if M[m_num][j] == None :        # 작업을 수행할 기계의 자리가 있으면
                        M[m_num][j] = v              # 작업을 그 자리에 배치
                        j = j + 1                    # 기계의 다음 자리로 이동
                break
                
    # 완성된 작업 스케줄러 출력            
    for m in M :                     # 스케줄러 순회
        count = 0                    # 초기화할 때 사용한 None의 개수를 세어주는 count
        for i in m :                 # 스케줄러 안의 기계 순회
            if i == None :          # 기계안의 작업 시간이 None이면 
                count = count + 1    # count 증가
        if count != len(m) :         # count의 개수 != 스케줄러 안의 각 기계의 총 작업 시간 이면
            print(m)                 # 스케줄러 안의 기계 출력

def main():
    # 주어진 작업들의 집합 Job
    JOB = [ [11,12], [1,3], [7,10], [8,12], [3,8], [1,7], [3,11] ]    # 전체 작업들
    JOB2 = deepcopy(JOB)   # 전체 작업들 깊은 복사
    print("주어진 작업들의 집합:", JOB)    # 전체 작업들 출력
    
    print("\nTaskScheduling(by Shortest Job First) :")
    TaskScheduling(shortest_job_sort(JOB))    # 전체 작업들을 짧은 작업 시간을 우선으로 오름차순 정렬 후 스케줄링
    
    print("\nTaskScheduling(by Earlist Start Time First) (최적해) :")
    TaskScheduling(earlist_start_time_sort(JOB))    # 전체 작업들을 빠른 작업 시작 시간을 우선으로 오름차순 정렬 후 스케줄링

main()
