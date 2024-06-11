"""
This module contains tests for the sql_statements module.
"""
from backend.sql_statements import process_cols, select_cols, insert_cols, delete_cols


def test_process_cols():
    """
    Test the process_cols function
    :return:
    """
    columns = {"col1": "val1", "col2": "val2"}
    result = process_cols(columns)
    assert result == "col1 = 'val1', col2 = 'val2'"


def test_select_cols():
    """
    Test the select_cols function
    :return:
    """
    df = {"col1": ["val1"], "col2": ["val2"]}
    result = select_cols(df, 0)
    assert result == "col1 = 'val1' AND col2 = 'val2'"


def test_insert_cols():
    """
    Test the insert_cols function
    :return:
    """
    cols = {"col1": "val1", "col2": "val2"}
    tab_name = "test_table"
    result = insert_cols(cols, tab_name)
    assert result == "INSERT INTO test_table (col1, col2) VALUES ('val1', 'val2')"


def test_delete_cols():
    """
    Test the delete_cols function
    :return:
    """
    df = {"col1": ["val1"], "col2": ["val2"]}
    idx = 0
    tab_name = "test_table"
    result = delete_cols(idx, df, tab_name)
    assert result == "DELETE FROM test_table WHERE col1 = 'val1' AND col2 = 'val2'"
