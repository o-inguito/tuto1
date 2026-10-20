# 1. 파이썬이 설치된 가벼운 리눅스 환경을 가져온다
FROM python:3.9-slim

# 2. 내 컴퓨터에 있는 코드를 도커 컨테이너 안의 /app 폴더로 복사한다
WORKDIR /app
COPY app.py .

# 3. 컨테이너가 켜질 때 실행할 명령어를 지정한다
CMD ["python", "app.py"]