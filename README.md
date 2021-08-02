# 설치 및 사용 방법
1. [git](https://git-scm.com/downloads) 및 [python3](https://www.python.org/downloads/) 설치
1. 이 project clone 및 directory 접근
    ```bash
    git clone https://github.com/k-young-passionate/riot_api_test.git
    cd riot_api_test
    ```
1. python3 virtual env 생성 및 필요 package 설치
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
1. `config.py`의 `API_KEY`에 자신의 api_key 값 할당
1. 아래의 명령어를 통해 실행
    ```bash
    python runner.py --user_name "검색할 user의 닉네임 입력"
    ```
