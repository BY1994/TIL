# 2021-06-09 (Certificate Authority)

### Certificate Authority (CA)

> **3.2.1 인증서의 내용물**
>
> 
>
> 상대방이 신뢰할 수 있는지 검증하기 위해 존재하는 '인증서' 라는 포맷의 파일에 대해서 먼저 알아보자. 인증서 파일 안에는 다양한 내용이 저장되어 있으며, 대표적인 내용물은 아래와 같다.
>
> 
>
> (1) 인증서의 소유자 이름, 
>
> (2) 인증서 소유자의 공개 키 (당연히 비밀 키는 소유자가 가지고 있다), 
>
> (3) 인증서의 유효 기간, 
>
> (4) 고유한 UID
>
> (5) 인증서의 기타 모든 값들을 해시화한 값 2 
>
> 그리고 가장 중요한 것은, (5) 의 값 : **인증서의 내용을 종합해 해시화한 값을 암호화한 값 (지문)** 이 마지막으로 인증서에 기록된다. 이 지문 값에 대해서는 뒤에서 다시 언급한다. 어쨌든, 인증서라는 것은 하나의 파일이며 그 안에는 위와 같이 여러 정보가 담겨져 있다고 알고 넘어가자. 

https://m.blog.naver.com/alice_k106/221468341565



### HTTPS와 SSL

> HTTPS와 SSL를 같은 의미로 이해하고 있는 경우가 많다. 이것은 맞기도 틀리기도 하다. 그것은 마치 인터넷과 웹을 같은 의미로 이해하는 것과 같다. 결론적으로 말하면 웹이 인터넷 위에서 돌아가는 서비스 중의 하나인 것처럼 HTTPS도 SSL 프로토콜 위에서 돌아가는 프로토콜이다.
>
> SSL 인증서는 클라이언트와 서버간의 통신을 제3자가 보증해주는 전자화된 문서다. 클라이언트가 서버에 접속한 직후에 서버는 클라이언트에게 이 인증서 정보를 전달한다. 클라이언트는 이 인증서 정보가 신뢰할 수 있는 것인지를 검증 한 후에 다음 절차를 수행하게 된다. SSL과 SSL 디지털 인증서를 이용했을 때의 이점은 아래와 같다.

https://opentutorials.org/course/228/4894