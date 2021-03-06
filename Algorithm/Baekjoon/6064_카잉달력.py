""" 
백준 알고리즘 6064
백준 Online Judge - 문제 - 단계별로 풀어보기 - 규칙 찾기 - 카잉달력

문제)
최근에 ICPC 탐사대는 남아메리카의 잉카 제국이 놀라운 문명을 지닌 카잉 제국을 토대로 하여 세워졌다는 사실을 발견했다. 카잉 제국의 백성들은 특이한 달력을 사용한 것으로 알려져 있다. 그들은 M과 N보다 작거나 같은 두 개의 자연수 x, y를 가지고 각 년도를 <x:y>와 같은 형식으로 표현하였다. 그들은 이 세상의 시초에 해당하는 첫 번째 해를 <1:1>로 표현하고, 두 번째 해를 <2:2>로 표현하였다. <x:y>의 다음 해를 표현한 것을 <x':y'>이라고 하자. 만일 x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1이다. 같은 방식으로 만일 y < N이면 y' = y + 1이고, 그렇지 않으면 y' = 1이다. <M:N>은 그들 달력의 마지막 해로서, 이 해에 세상의 종말이 도래한다는 예언이 전해 온다.
예를 들어, M = 10 이고 N = 12라고 하자. 첫 번째 해는 <1:1>로 표현되고, 11번째 해는 <1:11>로 표현된다. <3:1>은 13번째 해를 나타내고, <10:12>는 마지막인 60번째 해를 나타낸다.
네 개의 정수 M, N, x와 y가 주어질 때, <M:N>이 카잉 달력의 마지막 해라고 하면 <x:y>는 몇 번째 해를 나타내는지 구하는 프로그램을 작성하라.

입력)
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터는 한 줄로 구성된다. 각 줄에는 네 개의 정수 M, N, x와 y가 주어진다. (1 ≤ M, N ≤ 40,000, 1 ≤ x ≤ M, 1 ≤ y ≤ N) 여기서 <M:N>은 카잉 달력의 마지막 해를 나타낸다.
3
10 12 3 9
10 12 7 2
13 11 5 6

출력)
출력은 표준 출력을 사용한다. 각 테스트 데이터에 대해, 정수 k를 한 줄에 출력한다. 여기서 k는 <x:y>가 k번째 해를 나타내는 것을 의미한다. 만일 <x:y>에 의해 표현되는 해가 없다면, 즉, <x:y>가 유효하지 않은 표현이면, -1을 출력한다.
33
-1
83

최초 작성 2019.02.19 PBY
최종 제출 2019.03.13 PBY 와우!!!!!!!!!!!!!
"""

testcase = int(input())
for tc in range(testcase):
    M, N, x, y = map(int, input().split())
    ans = x
# while로 빼는 것으로 구현하자 => 성공!!!!!!!!!!!!!!!!!!!
    while ans > N:
        ans -= N
#    if ans > N:
#        ans %= N # N이 1인 경우 안 된다!!!!!!! => 이거 때문에 모든 반례에 걸렸다!!!!!!!!!!!
    cycle = x
    if ans == y: # 이 조건을 안 넣어서 틀렸다고 생각했는데...
        print(cycle)
    else:
        while True:
            cycle += M
            ans += M
            while ans > N:
                ans -= N
#            if ans > N:
#                ans %= N
                    
            if ans == y:
                print(cycle)
                break

            # 종료 조건은 최대 cycle
            if cycle > M*N:
                print(-1)
                break
        
"""
# 시간 초과
testcase = int(input())
for tc in range(testcase):
    M, N, x, y = map(int, input().split())
    bound = M * N
    if M <= N:  # 짧은 거 기준
        x2 = y2 = x  # x2 고정
        count = x2
        while count < bound:  # 모든 수를 다 돌았는데 없으면, 최소공배수 구하면 더 빠를 듯
            if x2 == x and y2 == y:
                break
            if y2 + M > N:
                y2 += M - N
            else:
                y2 += M
            count += M
        else:
            count = -1
    else:
        x2 = y2 = y
        count = y2
        while count < bound:
            if x2 == x and y2 == y:
                break
            if x2 + N > M:
                x2 += N - M
            else:
                x2 += N
            count += N
        else:
            count = -1
    print(count)

# 시간 초과
testcase = int(input())
for tc in range(testcase):    
    M, N, x, y = map(int, input().split())
    x2 = y2 = 1 # 첫번째 해
    count = 1
    while x2 != x or y2 != y:
        if x2 ==M and y2 == N:
            count = -1
            break
        if x2 < M:
            x2 = x2+1
        else:
            x2 = 1
        if y2 < N:
            y2 = y2+1
        else:
            y2 = 1
        count += 1
    print(count)
"""

"""
https://www.acmicpc.net/board/view/21503

15
40000 39999 39999 39998
40000 39999 40000 39999
40000 40000 40000 39999
40000 39998 40000 39997
39999 2 39998 2
3 40000 3 39999
40000 3 40000 3
8 2 4 2
10 12 2 12
12 10 12 10
12 10 1 1
12 6 12 6
10 1 5 1
1 10 1 5
1 1 1 1

답:
1599959999
1599960000
-1
-1
39998
39999
120000
4
12
60
1
12
5
5
1

"""
# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
