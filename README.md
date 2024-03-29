# MANAM readme

# Description
코로나로 인하여 얼어붙었던 사회에 문화생활이라는 가치를 활성화하여 마을에 생기를 불어 넣고자,
단절되었던 성북구 주민과 고려대학교 학생들을 "여가"를 매개로 하여 연결하고자 M:ANAM은 기획되었다.
그동안 다양한 이유로 문화 생활에 소외되었던 사람들에게 손을 뻗고, 고려대학교 학생들로 하여금 나눔의 가치를 자연스럽게 추구할 수 있도록 하였다.
잊고 있던 성북구 내의 문화 시설들에 대한 정보를 제공하고, 최신의 데이터 분석 기법을 활용하여 나도 몰랐던 나의 취향을 발견해 새로운 문화 프로그램을 접할 수 있게 하고, 성북구 주민들 사이와 더불어 성북구 주민들과 고려대 학생들을 연결하는 만남의 장을 주최한다.
이것이 M:ANAM이 추구하는 가치이자, 행동하는 방향이다.

![image](https://github.com/hwamminaa/manam/assets/110156673/55935a9d-2901-46b1-a75b-5251903973c7)

더 자세한 설명은 다음 PDF 에서 확인하실 수 있습니다.
[M:ANAM 소개](https://github.com/hwamminaa/manam/blob/main/MANAM%20%EC%86%8C%EA%B0%9C.pdf)


# Environment
OS: Windows 10 64-bit  
Interpreter  
CPU: Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz 2.11 GHz  
RAM: 8.00GB


# Prerequisite
- Python 3.9 Installation
- Python - Pandas library Installation
- Django Web Framework Installation
- AWS lightsail Server
- MobaXterm Installation


# Usage
## 개발 환경 - 로컬 서버 연결 
- 'python -m venv mysite'를 통해 가상환경 생성 후 Scripts의 activate 명령을 통해 가상환경에 진입.
- 가상환경 진입 후 'django-admin startproject config .' 명령을 통해 장고 프로젝트 생성, 개발 진행
- 'python manage.py runserver' 명령을 통해 개발 서버를 구동하고 웹 사이트에 접속

## 서비스 배포를 위한 운영 환경 - 원격 서버 연결
- AWS 라이트세일 인스턴스 생성: Linux/Unix, Ubuntu 20.04 LTS를 선택
- AWS 서버 접속을 위한 고정 IP 생성, 방화벽 해제 작업 진행
- 서버 작업을 위해 SSH 도구로 MobaXterm 사용
- SSH 클라이언트를 통해 서버에 접속하여 파이썬, 가상환경 설치 후 GIT 파일 내려받기
- 동적 페이지 요청을 처리하기 위해 WSGI 서버 - Gunicorn을 사용
- PostgreSQL을 database로 연결
   
  

# Apps and Files
## Files and Usage
## Apps
### 0. manam : 만남 메인페이지 & 만남 소개 구현
### -views.py
0.1 index: 메인 페이지\
0.2 intro: 만남 소개 페이지
### -html
0.1 main.html: 메인 페이지\
0.2 intro.html: 만남 소개 페이지

### 1. facility : 주변 문화 시설 찾아보기 구현
### -models.py
1.1 Facility: 성북구 전체시설 데이터\
1.2 Category: 시설 카테고리들
### -views.py
1.1 downloadFacilities: 시설 데이터 다운로드\
1.2 showFacilities: 시설 데이터 지도 페이지로 전달\
1.3 getlocation: 지도 페이지에서 입력받은 위치정보와 기본 시설 정보 전달\
1.4 showFacilitylist: 시설목록생성 및 카테고리 필터링 적용\
1.5 detail: 시설세부정보페이지
### -html
1.1 default.html: 내 위치 기반 시설 조회되는 지도 페이지\
1.2 get_location.html: 위치 검색 구현하는 페이지\
1.3 facility_list.html: 전체 시설 목록 페이지\
1.4 facility_detail.html: 시설 세부정보 페이지

### 2. program : 맞춤 프로그램 찾아보기 구현
### -models.py
2.1 Program: 프로그램 데이터 다운로드\
2.2 Category: 프로그램 카테고리들\
2.3 Recommendation: 프로그램 추천데이터 다운로드
### -views.py
2.1 downloadprogram: 성북구 프로그램 데이터 다운로드\
2.2 index: 메인 페이지\
2.3 detail: 프로그램 상세 페이지 및 추천\
2.4 program_Search: 프로그램 필터링\
2.5 downloadRecommedation: 추천데이터 다운로드\
2.6 like: 프로그램 좋아요 기능 구현
### -html
2.1 program_list: 성북구 프로그램 목록 페이지\
2.2 program_search: 성북구 프로그램 필터링\
2.3 program_result: 추천시스템 결과\
2.4 program_detail: 프로그램 상세정보 페이지

### 3. ku_manam: KU 만남
### 3.1 talent_donation: 고려대 동아리 지역 연계 프로그램\
### -models.py
3.1.1 Question: 게시글 등록\
3.1.2 Answer: 댓글 등록\
3.1.3 Article: 게시글 등록(커뮤니티)\
3.1.4 Comment: 댓글 등록(커뮤니티)
### -views.py
3.1.1 index: KU 만남 불러오기\
3.1.2 circle_list: 동아리 모아보기 페이지 불러오기\
3.1.3 talent_donation: 고려대 동아리 지역 연계 프로그램 페이지 불러오기\
3.1.4 detail: 고려대 동아리 지역 연계 프로그램 글 상세페이지\
3.1.5 like: 고려대 동아리 지역 연계 프로그램 좋아요 기능 구현\
3.1.6 detail: 성북구 어울림 글 상세페이지
3.1.7 question_create: 고려대 동아리 지역 연계 프로그램 등록\
3.1.8 question_modify: 글 수정\
3.1.9 question_delete: 글 삭제\
3.1.10 answer_create: 댓글 등록\
3.1.11 answer_modify: 댓글 수정\
3.1.12 answer_delete: 댓글 삭제
### -html
3.1.1 index.html: 고려대 동아리 지역 연계 프로그램 메인 페이지\
3.1.2 question_form.html: 고려대 동아리 지역 연계 프로그램 메뉴에 새 글을 등록하는 페이지\
3.1.3 question_detail.html: 고려대 동아리 지역 연계 프로그램 글 상세 정보 페이지

### 3.2 circlelist
### -models.py
3.3.1 Facility: 고려대 동아리 데이터\
3.3.2 Category: 동아리 카테고리들
### -views.py
3.3.1 downloadCircle: 동아리 데이터 다운\
3.3.2 detail: 동아리 세부정보 페이지\
3.3.3 circle_search: 동아리 목록 필터링
### -html
3.3.1 circle_search.html: 동아리 목록 페이지\
3.3.2 circle_detail.html: 동아리 세부정보 페이지

### 4. community
### -models.py
충돌을 막기 위하여 ku_manam의 모델을 활용함
### -views.py
4.1.1 allarticles: 커뮤니티 메인 페이지 불러오기\
4.1.2 recruitment: 커뮤니티 글 중 자율동아리 모집 글만 필터링\
4.1.3 proposal: 커뮤니티 글 중 프로그램 제안 글만 필터링\
4.1.4 detail: 커뮤니티 글 상세 페이지\
4.1.5 question_create: 커뮤니티 글 등록\
4.1.6 question_modify: 글 수정\
4.1.7 question_delete: 글 삭제\
4.1.8 answer_create: 댓글 등록\
4.1.9 answer_modify: 댓글 수정\
4.1.10 answer_delete: 댓글 삭제\
4.1.11 like: 커뮤니티 글 좋아요 기능
### -html
4.2.1 allarticles: 커뮤니티 메인 페이지\
4.2.2 proposal: 커뮤니티 글 중 프로그램 제안 글만 보기\
4.2.3 question_detail: 커뮤니티 글 상세 페이지\
4.2.4 question_form: 커뮤니티 메뉴에 새로운 글을 등록하는 페이지\
4.2.5 recruitment: 커뮤니티 글 중  글만 보기



### 5. common: 로그인, 회원가입 구현

# Acknowledgments
## References
- 점프투장고 (https://wikidocs.net/book/4223)
- https://inpa.tistory.com/
- https://western-sky.tistory.com/59
- https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Deployment
- https://django-bootstrap-v5.readthedocs.io/en/latest/

## Code References
- 지도에 시설 위치 표시: https://apis.map.kakao.com/web/sample/addr2coord/
- html 필터링 기능: https://ysyblog.tistory.com/m/44
