# Airflow의 기본 라이브러리들을 가져옵니다.
from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# DAG 정의를 시작합니다.
# 'with' 구문을 사용하면 이 블록 안에 있는 모든 Task가 이 DAG에 자동으로 포함됩니다.
with DAG(
    dag_id="hello_world_dag",  # Airflow UI에 표시될 DAG의 고유한 이름
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),  # 이 DAG가 언제부터 유효한지 설정
    schedule=None,  # None으로 설정하면 수동으로만 실행됩니다. (예: '@daily'는 매일 실행)
    catchup=False,  # 과거에 실행되지 않은 DAG Run을 실행할지 여부 (보통 False로 둠)
    tags=["example"],  # UI에서 DAG를 쉽게 찾기 위한 태그
) as dag:
    # 첫 번째 Task를 정의합니다.
    # BashOperator는 터미널 명령어를 실행하는 가장 간단한 Operator입니다.
    task_prints_hello = BashOperator(
        task_id="prints_hello",  # DAG 내에서 Task의 고유한 이름
        bash_command="echo 'Hello!'",  # 실행할 터미널 명령어
    )

    # 두 번째 Task를 정의합니다.
    task_prints_world = BashOperator(
        task_id="prints_world",
        bash_command="echo 'World!'",
    )
    
    # 세 번째 Task를 정의합니다.
    task_sleeps = BashOperator(
        task_id="sleeps_for_5_seconds",
        bash_command="sleep 5", # 5초 동안 대기하는 명령어
    )
    
    # 네 번째 Task를 정의합니다.
    task_prints_goodbye = BashOperator(
        task_id="prints_goodbye",
        bash_command="echo 'Goodbye!'",
    )


    # Task 간의 실행 순서를 정의합니다. (의존성 설정)
    # >> 연산자는 "왼쪽 Task가 성공하면 오른쪽 Task를 실행하라"는 의미입니다.
    # [A, B] >> C 는 A와 B가 모두 성공하면 C를 실행하라는 의미입니다.
    task_prints_hello >> task_sleeps >> task_prints_goodbye
    task_prints_world >> task_sleeps >> task_prints_goodbye
