# MANAM readme

# Description
코로나로 인하여 얼어붙었던 사회에 문화생활이라는 가치를 활성화하여 마을에 생기를 불어 넣고자,
단절되었던 성북구 주민과 고려대학교 학생들을 "여가"를 매개로 하여 연결하고자 M:ANAM은 기획되었다.
그동안 다양한 이유로 문화 생활에 소외되었던 사람들에게 손을 뻗고, 고려대학교 학생들로 하여금 나눔의 가치를 자연스럽게 추구할 수 있도록 하였다.
잊고 있던 성북구 내의 문화 시설들에 대한 정보를 제공하고, 최신의 데이터 분석 기법을 활용하여 나도 몰랐던 나의 취향을 발견해 새로운 문화 프로그램을 접할 수 있게 하고, 성북구 주민들 사이와 더불어 성북구 주민들과 고려대 학생들을 연결하는 만남의 장을 주최한다.
이것이 M:ANAM이 추구하는 가치이자, 행동하는 방향이다.


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
2.5 downloadRecommedation: 추천데이터 다운로드
### -html
2.1 program_list: 성북구 프로그램 목록 페이지\
2.2 program_search: 성북구 프로그램 필터링\
2.3 program_result: 추천시스템 결과\
2.4 program_detail: 프로그램 상세정보 페이지

### 3. circle, kuprogram, circlelist : 성북구X고려대 M:ANAM 구현 
### 3.1 circle
### -models.py
3.1.1 Question: 게시글 등록\
3.1.2 Answer: 댓글 등록
### -views.py
3.1.1 index: 성북구X고려대 만남 불러오기 불러오기\
3.1.2 circle_list: 동아리 모아보기 페이지 불러오기\
3.1.3 gwangjang: 성북구 어울림 페이지 불러오기 및 카테고리 필터링, 검색 적용\
3.1.4 autonomy_program: 성북구 어울림 글 중 글 종류가 "모집"인 것만 불러오는 페이지 및 카테고리 필터링, 검색 적용\
3.1.5 proposal: 성북구 어울림 글 중 글 종류가 "신청"인 것만 불러오는 페이지 및 카테고리 필터링, 검색 적용\
3.1.6 detail: 성북구 어울림 글 상세페이지
### -html
3.1.1 circle_main.html: 성북구X고려대 메인 페이지\
3.1.2 gwangjang.html: 성북구 어울림 전체글 리스트 페이지\
3.1.3 proposal.html: 성북구 어울림 글 중 종류가 "신청"에 해당하는 글 리스트 페이지\
3.1.4 question_form.html: 성북구 어울림 메뉴에 새 글을 등록하는 페이지\
3.1.5 question_detail.html: 성북구 어울림 글 상세 정보 페이지\
3.1.6 answer_form.html: 댓글 다는 페이지\
3.1.7 autonomy_program.html: 성북구 어울림 글 중 종류가 "모집"에 해당하는 글 리스트 페이지

### 3.2 kuprogram
### -models.py
3.2.1 Circleprogram: 글 등록 시 입력 양식\
3.2.2 Category: 동아리 카테고리
### -views.py
3.2.1 index: KU어울림 메인 페이지\
3.2.2 search: KU어울림 불러오기 및 카테고리 필터링, 검색 적용\
3.2.3 detail: KU어울림 글 상세페이지\
3.2.4 question_create: KU어울림 글 등록\
3.2.5 question_modify: 글 수정\
3.2.6 question_delete: 글 삭제
### -html
3.2.1 kuprogram_main: KU어울림 메인 페이지\
3.2.2 kuprogram_search: KU어울림 메인 페이지 + 검색, 카테고리 기능 추가\
3.2.3 question_detail: KU어울림 글 상세페이지\
3.2.4 question_form: KU어울림 글 등록

### 3.3 circlelist
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

### 4. common: 로그인, 회원가입 구현

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