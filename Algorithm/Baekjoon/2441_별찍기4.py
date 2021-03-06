""" 
백준 알고리즘 2441
백준 Online Judge - 문제 - 단계별로 풀어보기 - for문 사용해보기 - 별 찍기4

문제)
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

입력)
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
5

출력)
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
*****
 ****
  ***
   **
    *

최초 작성 2019.01.09 PBY
"""

N = int(input())
for i in range(N, 0, -1):
    print(" "*(N-i) + "*"*(i))
