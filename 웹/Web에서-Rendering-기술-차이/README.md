# Web에서 Rendering 기술 차이
> :bulb: Client Side Rendering vs Server Side Rendering

## 목표
- SPA와 MPA의 개념을 이해한다.



## SPA, MPA

- SPA(Single Page Application)는 한 개(Single)의 Page로 구성된 Application이다.
  MPA(Multiple Page Application)는 여러 개(Single)의 Page로 구성된 Application이다.
- MPA는 새로운 페이지를 요청할 때마다 정적 리소스가 다운로드된다. 매번 전체 페이지가 다시 렌더링 된다.
  반면 SPA는 웹 에플리케이션에 필요한 모든 정적 리소스를 최초 한 번에 다운로드한다. 그 이후 새로운 페이지 요청이 있을 때, 페이지 갱신에 필요한 데이터만 전달 받아서 페이지를 갱신한다.
- 그래서 SPA를 **CSR(Client Side Rendering) 방식으로 렌더링**한다고 말한다.
  그래서 MPA를 **SSR(Server Side Rendering) 방식으로 렌더링**한다고 말한다.

![SPA step1](https://linked2ev.github.io/assets/img/devlog/201808/2018-08-01-SPA-step1.png)



## CSR, SSR
- CSR
  - 브라우저(client)에서 js에 의해 View(HTML)을 동적으로 생성
  - 페이지 전환이 SSR보다 빠르다
  - 최초 접속시 모든 js와 정적파일을 가져와야 하기 때문에 최초 접속 로딩은 SSR보다 느리다.



- SSR
  - Web Server에서 View를 생성한다.
  - 페이지가 전환될 때 마다, client가 server에 view를 요청
  - server는 그것을 생성하고 client에 보내준다.
  - 때문에 view 전환 속도가 CSR에 비해 느리다.
  - 요청이 빈번해 질수록 부하가 더 커진다.

## 참고자료
- https://linked2ev.github.io/devlog/2018/08/01/WEB-What-is-SPA/
- https://hanamon.kr/spa-mpa-ssr-csr-%EC%9E%A5%EB%8B%A8%EC%A0%90-%EB%9C%BB%EC%A0%95%EB%A6%AC/

## 과제제출
- [기본과제](기본과제)
- [심화과제](심화과제)