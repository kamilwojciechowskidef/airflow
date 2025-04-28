from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Funkcja, którą zadanie wykona
def say_hello():
    print("Hello Airflow!")

# Definicja DAG
with DAG(
    dag_id="hello_airflow",         # unikalny ID DAG-a
    start_date=datetime(2024, 1, 1), # kiedy zacząć (ważne: w przeszłości)
    schedule_interval="@once",       # wykona się tylko raz po aktywacji
    catchup=False,                   # nie nadrabiaj "zaległych" uruchomień
    tags=["example"],                # opcjonalnie: tagi w UI
) as dag:

    hello_task = PythonOperator(
        task_id="say_hello_task",
        python_callable=say_hello,    # przypisanie funkcji
    )

    hello_task  # tylko jedno zadanie
