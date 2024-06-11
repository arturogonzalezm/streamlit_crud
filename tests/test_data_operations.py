"""
This module contains tests for the data_operations module.
"""
from backend.data_operations import get_dataset, get_tables


def test_get_dataset(mocker, snowflake_connection):
    """
    Test the get_dataset function
    :param mocker:
    :param snowflake_connection:
    :return:
    """
    table_name = "test_table"
    mock_session = snowflake_connection.session
    mock_session.table.return_value.to_pandas.return_value = {"id": [1, 2, 3]}

    df = get_dataset(table_name)

    assert "id" in df
    mock_session.table.assert_called_once_with(table_name)


def test_get_tables(mocker, snowflake_connection):
    """
    Test the get_tables function
    :param mocker:
    :param snowflake_connection:
    :return:
    """
    mock_session = snowflake_connection.session
    mock_session.sql.return_value.to_pandas.side_effect = [
        {"DB": ["test_db"]}, {"CS": ["test_schema"]}
    ]

    tables_df = get_tables()

    assert "DB" in tables_df.columns or "CS" in tables_df.columns
    mock_session.sql.assert_any_call("select current_database() as DB")
    mock_session.sql.assert_any_call("select current_schema() as CS")
