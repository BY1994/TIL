# 2022-02-04 (Pentium FDIV bug)

프로그래머가 몰랐던 멀티코어 CPU 이야기에서 소개된 펜티엄 프로세서의 유명한 버그이다.

FDIV (floating division) 버그인데, 속도를 빠르게 하기 위해 테이블을 이용해 빠르게 계산하는 SRT 알고리즘을 도입하였다. 그런데 실수로 인텔 엔지니어가 5개의 항목을 빠뜨렸다고 했다. 일상 생활에서 이 버그를 만날 확률은 낮지만, 엄밀한 계산이 필요한 분야에서는 큰 문제가 될 수 밖에 없다. 한 교수에 의해 버그가 발견되었다.

해당 내용에 대한 설명은 아래에서 잘 설명되어있었다.

https://johngrib.github.io/wiki/pentium-fdiv-bug/