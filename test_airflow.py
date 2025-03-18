import pytest
from pathlib import Path
from airflow.models import DagBag


@pytest.fixture
def dag_folder():
    return Path(__file__).parent / "dags"


@pytest.fixture
def dagbag():
    dag_folder = Path(__file__).parent / "dags"
    dagbag = DagBag(dag_folder=dag_folder, include_examples=False)
    return dagbag


def test_all_dags_work(dagbag: DagBag):
    assert dagbag.import_errors == {}


def test_hello_world_dag(dagbag: DagBag):
    dag = dagbag.get_dag(dag_id="hello_world")
    assert dag
