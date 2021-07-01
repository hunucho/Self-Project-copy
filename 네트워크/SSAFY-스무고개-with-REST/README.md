# SSAFY 스무고개 with REST
> :bulb: 다양한 API 호출 방법을 익힌다

## 목표
- REST의 개념을 이해하고 특징을 이해한다.
- REST API의 개념을 이해하고 설계 규칙을 이해한다.



## REST란
- “Representational State Transfer” 의 약자
  - 자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다.
  - 즉, 자원(resource)의 표현(representation) 에 의한 상태 전달
    - 자원(resource)의 표현(representation)
      - 자원: 해당 소프트웨어가 관리하는 모든 것
      - -> Ex) 문서, 그림, 데이터, 해당 소프트웨어 자체 등
      - 자원의 표현: 그 자원을 표현하기 위한 이름
      - -> Ex) DB의 학생 정보가 자원일 때, ‘students’를 자원의 표현으로 정한다.
    - 상태(정보) 전달
      - 데이터가 요청되어지는 시점에서 자원의 상태(정보)를 전달한다.
      - JSON 혹은 XML를 통해 데이터를 주고 받는 것이 일반적이다.
- 월드 와이드 웹(www)과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식
  - REST는 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 **웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일**이다.
  - REST는 네트워크 상에서 Client와 Server 사이의 통신 방식 중 하나이다.



### REST의 구체적인 개념

- HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.
  - 즉, REST는 자원 기반의 구조(ROA, Resource Oriented Architecture) 설계의 중심에 Resource가 있고 HTTP Method를 통해 Resource를 처리하도록 설계된 아키텍쳐를 의미한다.
  - 웹 사이트의 이미지, 텍스트, DB 내용 등의 모든 자원에 고유한 ID인 HTTP URI를 부여한다.
  - CRUD Operation
    - Create : 생성(POST)
    - Read : 조회(GET)
    - Update : 수정(PUT)
    - Delete : 삭제(DELETE)
    - HEAD: header 정보 조회(HEAD)



## REST API란
- API(Application Programming Interface)란
  - 데이터와 기능의 집합을 제공하여 컴퓨터 프로그램간 상호작용을 촉진하며, 서로 정보를 교환가능 하도록 하는 것
- REST API의 정의
  - REST 기반으로 서비스 API를 구현한 것
  - 최근 OpenAPI(누구나 사용할 수 있도록 공개된 API: 구글 맵, 공공 데이터 등), 마이크로 서비스(하나의 큰 애플리케이션을 여러 개의 작은 애플리케이션으로 쪼개어 변경과 조합이 가능하도록 만든 아키텍처) 등을 제공하는 업체 대부분은 REST API를 제공한다.



### RESTP API의 특징

- 사내 시스템들도 REST 기반으로 시스템을 분산해 확장성과 재사용성을 높여 유지보수 및 운용을 편리하게 할 수 있다.
- REST는 HTTP 표준을 기반으로 구현하므로, HTTP를 지원하는 프로그램 언어로 클라이언트, 서버를 구현할 수 있다.
- 즉, REST API를 제작하면 델파이 클라이언트 뿐 아니라, 자바, C#, 웹 등을 이용해 클라이언트를 제작할 수 있다.



## RESTful이란

- RESTful은 일반적으로 REST라는 아키텍처를 구현하는 웹 서비스를 나타내기 위해 사용되는 용어이다.
  - ‘REST API’를 제공하는 웹 서비스를 ‘RESTful’하다고 할 수 있다.
- RESTful은 REST를 REST답게 쓰기 위한 방법으로, 누군가가 공식적으로 발표한 것이 아니다.
  - 즉, REST 원리를 따르는 시스템은 RESTful이란 용어로 지칭된다.



### RESTful의 목적

- 이해하기 쉽고 사용하기 쉬운 REST API를 만드는 것
- RESTful한 API를 구현하는 근본적인 목적이 성능 향상에 있는 것이 아니라 일관적인 컨벤션을 통한 API의 이해도 및 호환성을 높이는 것이 주 동기이니, 성능이 중요한 상황에서는 굳이 RESTful한 API를 구현할 필요는 없다.



## 참고자료
- REST 통신이란?
  - https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html
- Python을 이용한 REST 통신 구현
  - https://twpower.github.io/124-python-requests-usage
- Java를 이용한 REST 통신 구현
  - https://zoomkoding.github.io/codingtest/java/2019/09/20/REST-JSON.html
- Curl을 이용한 REST 통신
  - https://www.lesstif.com/pages/viewpage.action?pageId=14745703



## 과제제출
- [기본과제](기본과제)
- [심화과제](심화과제)