""" 
2442 별찍기-5
문제 내용)
첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제
별은 가운데를 기준으로 대칭이어야 한다.

입력)
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력)
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

최초작성 2019.03.03 PBY
"""

N = int(input())

for row in range(N):
    print(' '*(N-1-row)+'*'*((row+1)*2-1))


"""
계속 출력형식이 잘못되었습니다가 떠서 뒤에 공백을 넣었다가 뺐다가 했는데,
그게 문제가 아니라 처음 공백 크기를 5칸으로 잡아버려서 N=5 이외에는 별이 찌그러져 나온 것이었다.
테스트 케이스를 여러 개 넣어봐야한다!!!

"""
# visual studio는 실행시 ctrl + f5

