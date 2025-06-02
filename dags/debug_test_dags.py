from airflow.decorators import dag, task
from datetime import datetime

@dag(schedule="@once", start_date=datetime(2025, 1, 1), catchup=False)
def debug_test_dag():
    @task()
    def hello():
        print("✅ DAG is loading correctly.")
    hello()

debug_test_dag = debug_test_dag()
