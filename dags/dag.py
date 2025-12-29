from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator
from datetime import datetime

@dag(dag_id='taskflow_version', start_date=datetime(2021, 1, 1), catchup=False, schedule=None)
def pipeline():

    convert_to_py = BashOperator(
        task_id='convert_to_py',
        bash_command='docker exec spark_container jupyter nbconvert --to python /opt/spark/work-dir/*.ipynb',
    )


    ingestion = BashOperator(
        task_id='ingestion',
        bash_command='docker exec spark_container spark-submit /opt/spark/work-dir/raw_data_ingestion.py',
    )


    ml = BashOperator(
        task_id='ml',
        bash_command='docker exec spark_container spark-submit /opt/spark/work-dir/feature_engineering.py',
    )

    convert_to_py >> ingestion >> ml

pipeline()