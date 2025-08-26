#!/bin/bash

# 1. 데이터베이스 초기화 또는 업그레이드
airflow db upgrade

# 2. .env 파일에 정의된 정보로 관리자 계정 생성
# (이미 존재하면 정보를 업데이트합니다)
airflow users create \
    --username "${_AIRFLOW_WWW_USER_USERNAME}" \
    --password "${_AIRFLOW_WWW_USER_PASSWORD}" \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email "${_AIRFLOW_WWW_USER_EMAIL}"

# 3. 웹서버와 스케줄러를 동시에 실행 (standalone과 비슷한 효과)
exec airflow scheduler & exec airflow webserver