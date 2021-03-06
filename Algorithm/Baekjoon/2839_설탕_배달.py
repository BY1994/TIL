""" 
백준 알고리즘 2558
백준 Online Judge - 문제 - 단계별로 풀어보기 - 사칙연산 도전하기 - 설탕 배달

문제)
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
18
4
6
9
11

출력)
상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
4
-1
2
3
3


최초 작성 시작 2019.01.08 PBY
최종 제출 2019.01.09 PBY
"""

# 초기화 및 사용자에게서 input 받기
num_3kg = 0
result = -1 # default
total_sugar = int(input())


# 3kg 봉지의 최대 개수를 검사
num_3kg = total_sugar//3

# 3kg 봉지 개수를 하나씩 줄여가면서 5kg 봉지와 검사
for cnum_3kg in range(num_3kg, -1, -1):
    if (total_sugar - 3 * cnum_3kg ) % 5 == 0:
        result = cnum_3kg + (total_sugar - 3 * cnum_3kg)//5

print(result, end = "")


# 시도 1
# (2019-01-08)

# check_max = 0
# num_of_total_bag = 100000 # large value
# 3kg 봉지의 최대 개수를 검사
# while check_max == 0:
#     if total_sugar > num_3kg:
#         num_3kg += 1
#     else:
#         check_max = 1

# 3kg 봉지 개수를 하나씩 줄여가면서 5kg 봉지와 검사
# for num_bag in range(num_3kg, 0, -1):
#     if (num_bag*3 + (num_3kg - num_bag)*5) == total_sugar and num_of_total_bag >= num_bag + num_3kg - num_bag
#     # 그리고 전체 개수가 최소이면, 지금 개수랑 같다. 봉지 개수가 전체 슈가랑 같아야함
#     result = 

# 위 코드의 문제는 3kg 봉지를 줄이면서 5kg 봉지를 늘리면 오히려 설탕 총량이 증가해버린다.
# 그것보다 더 큰 문제는 두 봉지의 합계가 처음부터 input 값과 맞지 않게 짠 것이다.


# 시도 2
# (2019-01-09)

# 코드로 작성하지는 않았지만
# total_sugar 인풋값을 % 3으로 나머지를 보고,
# 그 나머지가 5의 배수인지 보고
# 반대로 % 5로 나머지를 보고,
# 다시 그것의 나머지가 3의 배수인지를 확인해서
# 둘 중 하나라도 만족하면 출력하게 하려고 했다.

# 그런데 위 코드의 문제는 % 5를 하면 5가 1개 처럼 일부분으로는 볼 수 없고,
# 무조건 5가 가장 많이 몇 개 들어가는지를 알려줘서
# 결과값으로 5가 2개, 3이 2개 이런 애매한 상태를 만들 수가 없었다.

# 그래서 시도 3에서는 for 문을 이용해서 비교하였다.

# 시도 3
# 여기에 주어진 입출력으로만 테스트하는 것이 아닌지, range(num_3kg, 0, -1)을
# range(num_3kg, -1, -1)로 바꾸니 돌아갔다....
# 5의 배수도 테스트 케이스에 있었던 것 같다.