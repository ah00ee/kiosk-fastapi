# FastAPI로 구현하는 키오스크

## Framework
### 백엔드
- Language: Python
- Framework: FastAPI
- Database: SQLite

## ERD
<img src="img/erd.png" width=400>

## How to start server
```
uvicorn apis.main:kiosk --reload  
```

## API
- ### <a href="http://127.0.0.1/docs">docs</a>
- ### user 명세(prefix: /kiosk/user)
|API 명|URL|METHOD|설명|
|--|--|--|--|
|회원가입|/create|POST|회원을 등록한다.|
|로그인|/login|POST|로그인을 한다.|
|로그아웃|/logout|POST|로그아웃을 한다.|

- ### place 명세(prefix: /kiosk/place)
|API 명|URL|METHOD|설명|
|--|--|--|--|
|가게 불러오기|/|GET|사용자에 등록된 모든 가게를 불러온다.|
|가게 등록하기|/create|POST|가게를 등록한다.|
