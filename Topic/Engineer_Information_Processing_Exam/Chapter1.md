---

---

# Engineer Information Processing Exam (정보처리기사 시험)

## 목차

[1. 소프트웨어 설계 (요구사항 확인)](#1-소프트웨어-설계-(요구사항-확인))

[1. 소프트웨어 설계 (화면 설계)](#1-소프트웨어-설계-(화면-설계))

[1. 소프트웨어 설계 (애플리케이션 설계)](#1-소프트웨어-설계-(애플리케이션-설계))

[1. 소프트웨어 설계 (인터페이스 설계)](#1-소프트웨어-설계-(인터페이스-설계))

[5. 정보시스템 구축관리](#5-정보시스템-구축관리)



## 1. 소프트웨어 설계 (요구사항 확인)

### 소프트웨어 생명주기

- 폭포수 모형, 프로토타입 모형, 나선형 모형 => 5. 정보시스템 구축 관리 참고

- ***애자일 모형***: 요구사항 변화에 유연하게 대응 가능한 모형. 고객과의 소통에 초점을 맞춘 방법론. 애자일 모형의 종류 중 하나로 XP가 있다.



### XP (eXtreme Programming) 기법

- 핵심 가치: 의사소통 (Communication), 단순성 (Simplicity), 용기 (Courage), 존중 (Respect), 피드백 (Feedback)



> 11. XP (eXtreme Programming) 의 5가지 가치로 거리가 먼 것은? 답 (3)
>
>     (1) 용기 (2) 의사소통 (3) 정형분석 (4) 피드백
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 4. 애자일 기법에 대한 설명으로 맞지 않은 것은? 답 (2)
>
>    (1) 절차와 도구보다 개인과 소통을 중요하게 생각한다.
>
>    (2) 계획에 중점을 두어 변경 대응이 난해하다.
>
>    (3) 소프트웨어가 잘 실행되는데 가치를 둔다.
>
>    (4) 고객과의 피드백을 중요하게 생각한다.
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 1. XP (eXtreme Programming) 의 기본원리로 볼 수 없는 것은? 답 (1)
>
>    (1) Linear Sequential Method
>
>    (2) Pair Programming
>
>    (3) Collective Ownership
>
>    (4) Continuous Integration
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제



> 17. 애자일 방법론에 해당하지 않는 것은? 답 (4)
>
>     (1) 기능중심 개발 (2) 스크럼 (3) 익스트림 프로그래밍 (4) 모듈중심 개발
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제



### 요구사항 개발 프로세스

- 요구사항 도출
- 요구사항 분석
- 요구사항 명세
- 요구사항 확인
  - 동료 검토 (Peer Review): 요구사항 명세서 작성자가 요구사항 명세서를 설명하고 이해관계자들이 설명을 들으면서 결함을 발견
  - 워크 스루 (Walk Through): 검토 회의 전, 명세서를 미리 배포하여 사전검토 후에 짧은 검토 회의를 통해 결함을 발견
  - 인스펙션 (Inspection): 요구사항 명세서를 작성자를 제외한 다른 검토 전문가들이 명세서를 확인하면서 결함을 발견



> 1. 검토회의 전에 요구사항 명세서를 미리 배포하여 사전 검토한 후 짧은 검토 회의를 통해 오류를 조기에 검출하는데 목적을 두는 요구 사항 검토 방법은? 답 (3)
>
>    (1) 빌드 검증 (2) 동료 검토 (3) 워크 스루 (4) 개발자 검토
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 20. 인터페이스 요구 사항 검토 방법에 대한 설명이 옳은 것은? 답 (2)
>
>     (1) 리팩토링: 작성자 이외의 전문 검토 그룹이 요구사항 명세서를 상세히 조사하여 결함, 표준 위배, 문제점 등을 파악
>
>     (2) 동료검토: 요구 사항 명세서 작성자가 요구사항 명세서를 설명하고 이해관계자들이 설명을 들으면서 결함을 발견
>
>     (3) 인스펙션: 자동화된 요구 사항 관리 도구를 이용하여 요구 사항 추적성과 일관성을 검토
>
>     (4) CASE 도구: 검토 자료를 회의 전에 배포해서 사전 검토한 후 짧은 시간 동안 검토 회의를 진행하면서 결함을 발견
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



### 요구사항 분석

> 13. 소프트웨어 개발 방법 중 요구사항 분석 (requirements analysis) 과 거리가 먼 것은? 답 (4)
>
>     (1) 비용과 일정에 대한 제약설정 (2) 타당성 조사
>
>     (3) 요구사항 정의 문서화 (4) 설계 명세서 작성
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 16. 소프트웨어 개발 단계에서 요구 분석 과정에 대한 설명으로 거리가 먼 것은? 답 (2)
>
>     (1) 분석 결과의 문서화를 통해 향후 유지보수에 유용하게 활용할 수 있다.
>
>     (2) 개발 비용이 가장 많이 소요되는 단계이다.
>
>     (3) 자료흐름도, 자료 사전 등이 효과적으로 이용될 수 있다.
>
>     (4) 보다 구체적인 명세를 위해 소단위 명세서 (Mini-spec) 가 활용될 수 있다.
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제



### 요구사항 분석에 사용하는 기능 모델링 기법

- 데이터 흐름도 (DFD, Data Flow Diagram)
- 자료사전 (DD, Data Dictionary)

[참고] https://computer-science-student.tistory.com/103



### 데이터 흐름도 (DFD, Data Flow Diagram)

- 데이터가 각 프로세스를 따라 흐르면서 변환되는 모습을 나타낸 그림
- 시스템 분석과 설계에서 매우 유용하게 사용되는 다이어그램
- 데이터 흐름도는 시스템의 모델링 도구로서 가장 보편적으로 사용되는 것 중의 하나
- 자료 흐름 그래프 또는 버블차트라고 함

[출처] https://computer-science-student.tistory.com/103

![img](https://blog.kakaocdn.net/dn/cyBvBP/btqTIoBt03B/r5e6cDTyS7uM9WQnOaUoMK/img.png)



> 데이터 흐름도 (DFD)의 구성요소에 포함되지 않는 것은? 답 (4)
>
> ​	(1) process (2) data flow (3) data store (4) data dictionary
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 18 .자료흐름도 (Data Flow Diagram) 의 구성요소로 옳은 것은? 답 (2)
>
> ​	(1) process, data flow, data store, comment
>
> ​	(2) process, data flow, data store, terminator
>
> ​	(3) data flow, data store, terminator, data dictionary
>
> ​	(4) process, data store, terminator, mini-spec
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



> 9. DFD (data flow diagram) 에 대한 설명으로 틀린 것은? 답 (3)
>
>    (1) 자료 흐름 그래프 또는 버블 (bubble) 차트라고도 한다.
>
>    (2) 구조적 분석 기법에 이용된다.
>
>    (3) 시간 흐름을 명확하게 표현할 수 있다.
>
>    (4) DFD의 요소는 화살표, 원, 사각형, 직선(단선/이중선) 으로 표시한다.
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제



### 자료사전 (DD, Data Dictionary)

- 자료사전이란? 자료 요소, 자료 요소들의 집합, 자료의 흐름, 자료 저장소의 의미와 그들 간의 관계, 관계 값, 범위, 단위들을 구체적으로 명시하는 사전

![image-20210515002458343](images/image-20210515002458343.png)

[출처] https://computer-science-student.tistory.com/103



> 8. 자료사전에서 자료의 생략을 의미하는 기호는? 답 (4)
>
>    (1) { }        (2) **     (3) =      (4)      ( )
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 16. 자료 사전에서 자료의 반복을 의미하는 것은? 답 (3)
>
>     (1) =        (2) (  )       (3) {  }    (4)  [   ]
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



> 13. 다음 중 자료사전 (Data Dictionary) 에서 선택의 의미를 나타내는 것은? 답 (1)
>
>     (1) [  ]      (2) {  }     (3)  +     (4)   =
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제



### 요구사항 확인기법

- 요구사항 검토
- 프로토타이핑
- 모델 검증
- 인수 테스트



### UML

- 사물 (Things)
- 관계
- 다이어그램



> 11. UML 의 기본 구성요소가 아닌 것은? 답 (2)
>
>     (1) Things (2) Terminal (3) Relationship (4) Diagram
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제



> 6. UML 확장 모델에서 스테레오 타입 객체를 표현할 때 사용하는 기호로 맞는 것은? 답 (1)
>
>    (1) << >> (2) (( )) (3) {{ }} (4) [[ ]]
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



### UML 관계

- 연관 관계
- 집합 관계
- 포함 관계
- 일반화 관계: 자식 클래스 a는 부모 클래스 b의 일종이다.
- 의존 관계
- 실체화 관계



> 16. 객체지향 기법에서 클래스들 사이의 '부분-전체 (part-whole)' 관계 또는 '부분 (is-a-part-of)'의 관계로 설명되는 연관성을 나타내는 용어는? 답 (4)
>
>     (1) 일반화 (2) 추상화 (3) 캡슐화 (4) 집단화
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 14. 아래 UML 모델에서 '차' 클래스와 각 클래스의 관계로 옳은 것은? 답 (3)
>
>     ![image-20210514234415315](images/image-20210514234415315.png)
>
>     (1) 추상화 관계 (2) 의존 관계 (3) 일반화 관계 (4) 그룹 관계
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



### 다이어그램

- 구조적 다이어그램
  - 클래스, 객체
  - 컴포넌트, 배치
  - 복합체 구조, 패키지
- 행위 다이어그램
  - 유스케이스, 시퀀스
  - 커뮤니케이션, 상태
  - 활동, 상호작용 개요, 타이밍



클래스 다이어그램

![A simple class diagram for a commercial software application, in UML... |  Download Scientific Diagram](https://www.researchgate.net/profile/Sergi-Valverde/publication/225686440/figure/fig3/AS:667828239732738@1536234068086/A-simple-class-diagram-for-a-commercial-software-application-in-UML-notation-The.png)



유스케이스 다이어그램

![소프트웨어 공학] 모델링과 UML, 유스케이스 다이어그램 : 네이버 블로그](https://mblogthumb-phinf.pstatic.net/MjAxNzA1MTBfNTAg/MDAxNDk0MzkxMjEyODQy._X90dmijdHf8463ZjPWEdVo_tcPpNRdsmW11L_hfjxsg.Rl9xV80ED5PgQyuz7C16vysed3yR1xYYik48Ckg9rE0g.PNG.ljh0326s/image.png?type=w800)



시퀀스 다이어그램

![UML ] 시퀀스 다이어그램(Sequence Diagram) 이론](https://blog.kakaocdn.net/dn/chJ6te/btqtSMHtMjJ/28ivQtT3KmZKCOf3burLmK/img.png)



활동 다이어그램

![활동 다이어그램 - 위키백과, 우리 모두의 백과사전](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Activity_conducting.svg/1200px-Activity_conducting.svg.png)



> 12. UML 모델에서 사용하는 Structural Diagram에 속하지 않은 것은? 답 (4)
>
>     (1) Class Diagram (2) Object Diagram (3) Component Diagram (4) Activity Diagram
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 12. UML 에서 활용되는 다이어그램 중, 시스템의 동작을 표현하는 행위 (Behavioral) 다이어그램에 해당하지 않는 것은? 답 (4)
>
>     (1) 유스케이스 다이어그램 (Use Case Diagram)
>
>     (2) 시퀀스 다이어그램 (Sequence Diagram)
>
>     (3) 활동 다이어그램 (Activity Diagram)
>
>     (4) 배치 다이어그램 (Deployment Diagram)
>
> [출처] 전자문제집 CBT 2020년 8월 22일 기출문제



> 6. UML 에서 시퀀스 다이어그램의 구성 항목에 해당하지 않는 것은? 답 (3)
>
>    (1) 생명선 (2) 실행 (3) 확장 (4) 메시지
>
> [출처] 전자문제집 CBT 2020년 8월 22일 기출문제



## 1. 소프트웨어 설계 (화면 설계)

### 사용자 인터페이스의 기본 원칙

- 직관성
- 유효성
- 학습성
- 유연성

> 10. UI 설계 원칙에서 누구나 쉽게 이해하고 사용할 수 있어야 한다는 것은? 답 (2)
>
>     (1) 유효성 (2) 직관성 (3) 무결성 (4) 유연성
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



### 사용자 인터페이스의 설계 지침

- 사용자 중심, 일관성, 단순성
- 결과예측 가능, 가시성, 표준화
- 접근성, 명확성, 오류 발생 해결



### 품질 요구사항

- 기능성
- 신뢰성
- 사용성
- 효율성
- 유지보수성
- 이식성



## 1. 소프트웨어 설계 (애플리케이션 설계)

### 소프트웨어 아키텍처

- 모듈화
- 추상화
- 단계적 분해
- 정보 은닉



> 7. 객체지향에서 정보 은닉과 가장 밀접한 관계가 있는 것은? 답 (1)
>
>    (1) Encapsulation (2) Class (3) Method (4) Instance
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



### 플랫폼 성능특성 분석

> 5. 소프트웨어 설계시 구축된 플랫폼의 성능특성 분석에 사용되는 측정 항목이 아닌 것은? 답 (4)
>
>    (1) 응답시간 (Response Time) (2) 가용성 (Availability)
>
>    (3) 사용률 (Utilization) (4) 서버 튜닝 (Server Tuning)
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



### 아키텍처 패턴

- 레이어 패턴
- 클라이언트-서버 패턴
- 파이프-필터 패턴
- 모델-뷰-컨트롤러 패턴
- 기타: 마스터-슬레이브 패턴, 브로커 패턴, 피어-투-피어 패턴, 이벤트-버스 패턴, 블랙보드 패턴, 인터프리터 패턴



> 6. 파이프 필터 형태의 소프트웨어 아키텍처에 대한 설명으로 옳은 것은? 답 (2)
>
>    (1) 노드와 간선으로 구성된다.
>
>    (2) 서브시스템이 입력데이터를 받아 처리하고 결과를 다음 서브시스템으로 넘겨주는 과정을 반복한다.
>
>    (3) 계층 모델이라고도 한다.
>
>    (4) 3개의 서브시스템 (모델, 뷰, 제어) 으로 구성되어있다.
>
> [출처] 전자문제집 CBT 2020 년 9월 26일 필기 기출문제



### 객체지향 구성요소

- 객체: 데이터 + 연산 / 메소드: 객체의 구체적인 연산을 정의한 것
- 클래스 (Class): 유사한 객체들을 모아 공통된 특성을 표현. 클래스로부터 생성된 새로운 객체는 인스턴스(Instance)라고 한다.
- 메시지 (Message): 객체들 간의 상호작용이 일어나기 위해서 메시지가 필요하며, 메시지를 통하여 객체의 동작이 수행된다.



> 3. 객체지향 프로그램에서 데이터를 추상화하는 단위는? 답 (2)
>
>    (1) 메소드 (2) 클래스 (3) 상속성 (4) 메시지
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 13. 객체지향 소프트웨어 공학에서 하나 이상의 유사한 객체들을 묶어서 하나의 공통된 특성을 표현한 것은? 답 (2)
>
>     (1) 트랜지션 (2) 클래스 (3) 시퀀스 (4) 서브루틴
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



### 객체지향 기법

- 캡슐화 (Encapsulation)
- 상속 (Inheritance)
- 추상화 (Abstraction)
- 다형성 (Polymorphism)



> 8. 객체지향에서 정보 은닉과 가장 밀접한 관계가 있는 것은? 답 (1)
>
>    (1) Encapsulation (2) Class (3) Method (4) Instance
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



> 4. 객체지향 기법의 캡슐화 (Encapsulation) 에 대한 설명으로 틀린 것은? 답 (4)
>
>    (1) 인터페이스가 단순화 된다.
>
>    (2) 소프트웨어 재사용성이 높아진다.
>
>    (3) 변경 발생 시 오류의 파급효과가 적다.
>
>    (4) 상위 클래스의 모든 속성과 연산을 하위 클래스가 물려받는 것을 의미한다.
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제



### 럼바우 객체지향 분석 기법

- 구성 요소를 그래픽 표기로 모델링하는 기법으로 OMT(Object Modeling Technique)이라고 부릅니다.
- Object 모델링 → Dynamic 모델링 → Functioanl 모델링 순서로 진행합니다.
- ★ "객 - 동 - 기" 로 암기하면 된다!
- Object 모델링: 정보 모델링으로 필요한 Object를 찾고 Object 사이의 관계를 정하는 모델링
- Dynamic 모델링:  상태도를 이용하여 제어 흐름을 모델링
- Functional 모델링: 자료 흐름도를 이용하여 다수의 프로세스 사이의 자료 흐름을 중심으로 처리 과정을 표현한 모델링

[출처] http://ehpub.co.kr/tag/%EB%9F%BC%EB%B0%94%EC%9A%B0rumbaugh%EC%9D%98-%EB%B6%84%EC%84%9D-%EA%B8%B0%EB%B2%95/



> 14. 럼바우 (Rumbaugh) 의 객체지향 분석 절차를 가장 바르게 나열한 것은? 답 (1)
>
>     (1) 객체 모형 -> 동적 모형  -> 기능 모형
>
>     (2) 객체 모형 -> 기능 모형 - > 동적 모형
>
>     (3) 기능 모형 -> 동적 모형 -> 객체 모형
>
>     (4) 기능 모형 -> 객체 모형 -> 동적 모형
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 10. 그래픽 표기법을 이용하여 소프트웨어 구성 요소를 모델링하는 럼바우 분석 기법에 포함되지 않는 것은? 답 (4)
>
>     (1) 객체 모델링 (2) 기능 모델링 (3) 동적 모델링 (4) 블랙박스 분석 모델링
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제



> 2. 럼바우 (Rumbaugh) 객체지향 분석 기법에서 동적 모델링에 활용되는 다이어그램은? 답 (3)
>
>    (1) 객체 다이어그램 (Object Diagram)
>
>    (2) 패키지 다이어그램 (Package Diagram)
>
>    (3) 상태 다이어그램 (State Diagram)
>
>    (4) 자료 흐름도 (Data Flow Diagram)
>
> [출처] 전자문제집 CBT 2020 년 9월 26일 필기 기출문제



### 모듈

- 결합도: 한 모듈과 다른 모듈간의 상호 의존도를 측정하는 것으로 독립적인 모듈이 되기 위해서는 결합도가 약해야 한다. `내용 결합도 (Content coupling) > 공통 결합도 (Common coupling) > 외부 결합도 (External coupling) > 제어 결합도 (Control coupling) > 스탬프 결합도 (Stamp coupling) > 데이터 결합도 (Data coupling)` 순으로 결합도가 강하다.
- 응집도: 한 모듈 내에 있는 구성 요소들이 서로 관련되어 있는 정도를 의미하며, 관련성을 측정하는 것으로 응집도가 높도록 설계되도록 해야한다. `기능적 응집도 (functional cohesion) > 순차적 응집도 (sequential cohesion) > 교환적 응집도 (communicational cohesion) > 절차적 응집도 (procedural cohesion) > 시간적 응집도 (temporal cohesion) > 논리적 응집도 (logical cohesion) > 우연적 응집도 (coincidental cohesion)` 순으로 응집도가 강하다.



> 20. 바람직한 소프트웨어 설계 지침이 아닌 것은? 답 (3)
>
>     (1) 적당한 모듈의 크기를 유지한다.
>
>     (2) 모듈 간의 접속 관계를 분석하여 복잡도와 중복을 줄인다.
>
>     (3) 모듈 간의 결합도는 강할수록 바람직하다.
>
>     (4) 모듈 간의 효과적인 제어를 위해 설계에서 계층적 자료 조직이 제시되어야 한다.
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



### 공통 모듈

공통모듈 명세 작성 원칙

- 정확성 / 명확성 / 완전성 / 일관성 / 추적성



> 15. 공통 모듈에 대한 명세 기법 중 해당 기능에 대해 일관되게 이해하고 한 가지로 해석될 수 있도록 작성하는 원칙은? 답 (2)
>
>     (1) 상호작용성 (2) 명확성 (3) 독립성 (4) 내용성
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



### 코드

- 주요기능: 식별 기능, 분류 기능, 배열 기능
- 코드의 종류
  - 순차코드
  - 블록코드: 코드화 대상 항목 중에서 공통성이 있는 것끼리 블록으로 구분하고, 각 블록 내에서 일련번호를 부여하는 방법 (= 구분 코드)
  - 10진코드
  - 그룹 분류 코드
  - 연상코드: 코드화 대상 항목의 명칭이나 약호와 관계있는 숫자나 문자, 기호를 이용하여 코드를 부여하는 방법
  - 표의 숫자 코드: 코드화 대상 항목의 성질, 물리적 수치를 그대로 코드에 적용시키는 방법
  - 합성 코드



> 10. 코드의 기본 기능으로 거리가 먼 것은? 답 (1)
>
>     (1) 복잡성 (2) 표준화 (3) 분류 (4) 식별
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



> 2. 코드 설계에서 일정한 일련번호를 부여하는 방식의 코드는? 답 (3)
>
>    (1) 연상 코드 (2) 블록 코드 (3) 순차 코드 (4) 표의 숫자 코드
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 7. 코드화 대상 항목의 중량, 면적, 용량 등의 물리적 수치를 이용하여 만든 코드는? 답 (3)
>
>    (1) 순차 코드 (2) 10진 코드 (3) 표의 숫자 코드 (4) 블록 코드
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



### 디자인 패턴

- 생성 패턴
  - 추상 팩토리 패턴
  - 빌더 패턴
  - Factory Method 패턴
  - 프로토타입 싱글톤
- 구조 패턴
  - 어댑터
  - 브리지
  - 컴포지트
  - 데코레이터
  - 퍼씨드
  - 플라이웨이트
  - 프록시
- 행위 패턴
  - 책임 연쇄
  - 커맨드
  - 인터프리터
  - 반복자
  - 중재자
  - 메멘토
  - 옵서버
  - ***State (상태) 패턴***  =>많이 헷갈림!
  - 전략
  - 템플릿 메소드
  - 방문자



> 8. 디자인 패턴 중에서 행위적 패턴에 속하지 않는 것은? 답 (3)
>
>    (1) 커맨드 (Command) 패턴
>
>    (2) 옵저버 (Observer) 패턴
>
>    (3) 프로토타입 (Prototype) 패턴
>
>    (4) 상태 (State) 패턴
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



> 2. 다음 내용이 설명하는 디자인 패턴은? 답 (3)
>
>    - 객체를 생성하기 위한 인터페이스를 정의하며 어떤 클래스가 인스턴스화될 것인지는 서브클래스가 결정하도록 하는 것
>    - Virtual-Constructor 패턴이라고도 함 - (Virtual Constructor: 가상 생성자)
>
>    (1) Visitor 패턴 (2) Observer 패턴 (3) Factory Method 패턴 (4) Bridge 패턴
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



> 8. 디자인 패턴 사용의 장, 단점에 대한 설명으로 거리가 먼 것은? 답 (4)
>
>    (1) 소프트웨어 구조 파악이 용이하다.
>
>    (2) 객체지향 설계 및 구현의 생산성을 높이는데 적합하다.
>
>    (3) 재사용을 위한 개발 시간이 단축된다.
>
>    (4) 절차형 언어와 함께 이용될 때 효율이 극대화된다.
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제





### GoF (Gangs of Four) 디자인 패턴

GoF(Gang of Four)에서는 23가지 디자인 패턴을 3가지 유형으로 분류합니다.

A. Creational Pattern

- 객체를 생성하는데 관련된 패턴들
- 객체가 생성되는 과정의 유연성을 높이고 코드의 유지를 쉽게 함

B. Structural Pattern

- 프로그램 구조에 관련된 패턴들
- 프로그램 내의 자료구조나 인터페이스 구조 등 프로그램의 구조를 설계하는데 활용할 수 있는 패턴들

C. Behavioral Pattern

- 반복적으로 사용되는 객체들의 상호작용을 패턴화 해놓은 것들

![img](https://realzero0.github.io/assets/img/gof_types.png)

[출처] https://realzero0.github.io/study/2017/06/12/%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8C%A8%ED%84%B4-%EC%A0%95%EB%A6%AC.html



> 7. GoF (Gangs of Four) 의 디자인 패턴에서 행위 패턴에 속하는 것은? 답 (2)
>
>    (1) Builder (2) Visitor (3) Prototype (4) Bridge
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 19. GoF (Gangs of Four) 디자인 패턴 분류에 해당하지 않는 것은? 답 (4)
>
>     (1) 생성 패턴 (2) 구조 패턴 (3) 행위 패턴 (4) 추상 패턴
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제



## 1. 소프트웨어 설계 (인터페이스 설계)

### 인터페이스 요구사항 검증

- 요구사항 검증 방법: 요구사항 검토, 프로토타이핑, 테스트 설계, CASE 도구 활용
- 검증 주요 항목: 완전성, 일관성, 명확성, 기능성, 검증가능성, 추적가능성, 변경용이성



> 17. CASE가 갖고 있는 주요 기능이 아닌 것은?
>
>     (1) 그래픽 지원 (2) 소프트웨어 생명주기 전 단계의 연결
>
>     (3) 언어번역 (4) 다양한 소프트웨어 개발 모형 지원
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 19. CASE (Computer-Aided Software Engineering) 도구에 대한 설명으로 거리가 먼 것은? 답 (4)
>
>     (1) 소프트웨어 개발 과정의 일부 또는 전체를 자동화하기 위한 도구이다.
>
>     (2) 표준화된 개발 환경 구축 및 문서 자동화 기능을 제공한다.
>
>     (3) 작업 과정 및 데이터 공유를 통해 작업자간 커뮤니케이션을 증대한다.
>
>     (4) 2000 년대 이후 소개되었으며, 객체지향 시스템에 한해 효과적으로 활용된다.
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



> 3. CASE (Computer Aided Software Engineering) 의 주요 기능으로 옳지 않은 것은? 답 (4)
>
>    (1) S/W 라이프 사이클 전 단계의 연결
>
>    (2) 그래픽 지원
>
>    (3) 다양한 소프트웨어 개발 모형 지원
>
>    (4) 언어 번역
>
> [출처] 전자문제집 CBT 2020 년 9월 26일 필기 기출문제



### 미들웨어 솔루션 명세

- 미들웨어
  - DB, RPC
  - MOM, TP-Monitor
  - ORB, WAS

> 18. 클라이언트와 서버 간의 통신을 담당하는 시스템 소프트웨어를 무엇이라고 하는가? 답 (3)
>
>     (1) 웨어러블 (2) 하이웨어 (3) 미들웨어 (4) 응용 소프트웨어
>
> [출처] 전자문제집 CBT 2020 년 8월 22일 필기 기출문제



> 9. 트랜잭션이 올바르게 처리되고 있는지 데이터를 감시하고 제어하는 미들웨어는? 답 (3)
>
>    (1) RPC (2) ORB (3) TP monitor (4) HUB
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



> 5. 미들웨어 솔루션의 유형에 포함되지 않는 것은? 답 (2)
>
>    (1) WAS (2) Web Server (3) RPC (4) ORB
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



## 5. 정보시스템 구축관리

### 소프트웨어 생명주기

- 폭포수 모형: `타당성 검토->계획->요구사항분석->구현->테스트->유지보수단계` 순으로 이루어진다. 순차적으로 한 단계씩 진행되어야한다. 전 단계가 완료되기 전에는 다음 단계로 진행할 수 없다.
- 프로토타입 모형: `요구분석->프로토타입 설계->프로토타입 개발->고객평가` 순으로 이루어진다. 개발 초기에 시스템의 모형 (prototype) 을 간단히 만들어 사용자에게 보여주고, 사용자가 정보 시스템을 직접 사용해보게 함으로써 프로토타입을 재구축하는 과정을 사용자가 만족할 때까지 반복해나가면서 시스템을 개선시켜 나가는 방식이다.
- 나선형 모형: `계획 수립->위험분석->개발 및 검증->고객 평가` 순으로 ***반복***한다. 고객과의 소통을 통하여 계획 구립과 위험분석, 구축, 고객 평가의 과정을 거쳐서 소프트웨어를 개발하는 방식이다. 
- 애자일: 고객과의 소통에 초점을 맞춘 방법론이다.



> 83. 다음 설명에 해당하는 생명주기 모형으로 가장 옳은 것은? 답 (3)
>
>     - 가장 오래된 모형으로 많은 적용 사례가 있지만 요구사항의 변경이 어려우며, 각 단계의 결과가 확인되어야지만 다음 단계로 넘어간다. 선형 순차적 모형으로 고전적 생명 주기 모형이라고도 한다.
>
>     (1) 패키지 모형 (2) 코코모 모형 (3) 폭포수 모형 (4) 관계형 모델
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제



> 94. 소프트웨어 생명주기 모형 중 고전적 생명주기 모형으로 선형 순차적 모델이라고도 하며, 타당성 검토, 계획, 요구사항 분석, 구현, 테스트, 유지보수의 단계를 통해 소프트웨어를 개발하는 모형은?
>
>     (1) 폭포수 모형 (2) 애자일 모형 (3) 컴포넌트 기반 방법론 (4) 6GT 모형
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



> 90. 소프트웨어 개발 모델 중 나선형 모델의 4가지 주요 활동이 순서대로 나열된 것은? 답 (2)
>
>     - (A) 계획 수립 / (B) 고객 평가 / (C) 개발 및 검증 / (D) 위험 분석
>
>     (1) A - B - D - C 순으로 반복
>
>     (2) A - D - C - B 순으로 반복
>
>     (3) A - B - C - D 순으로 반복
>
>     (4) A - C - B - D 순으로 반복
>
> [출처] 전자문제집 CBT 2020년 9월 26일 필기 기출문제
>
> [출처] 전자문제집 CBT 2020년 8월 22일 필기 기출문제



> 91. 프로토타입을 지속적으로 발전시켜 최종 소프트웨어 개발까지 이르는 개발방법으로 위험관리가 중심인 소프트웨어 생명주기 모형은? 답 (1)
>
>     (1) 나선형 모형 (2) 델파이 모형 (3) 폭포수 모형 (4) 기능점수 모형
>
> [출처] 전자문제집 CBT 2020년 6월 6일 필기 기출문제



## 참고 자료

- 정보처리기사 필기 요약정리: https://shlee1990.tistory.com/category/%EC%9E%90%EA%B8%B0%EA%B3%84%EB%B0%9C/%EC%9E%90%EA%B2%A9%EC%A6%9D
- 정보처리기사 필기 요약 더 자세한 정리: https://narup.tistory.com/72
- 정보처리기사 필기 전자문제집 CBT: https://www.comcbt.com/xe/iz