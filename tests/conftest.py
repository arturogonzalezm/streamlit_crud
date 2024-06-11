"""
This file contains the fixtures that are used in the tests.
"""

import pytest
from backend.snowflake_connection import SnowflakeConnection
from unittest.mock import MagicMock


@pytest.fixture(scope="module")
def mock_snowflake_session():
    """
    Mocks the Snowflake session
    :return: Snowflake session
    """
    mock_session = MagicMock()
    mock_session.table.return_value.to_pandas.return_value = {"id": [1, 2, 3]}
    mock_session.sql.return_value.to_pandas.return_value = {"DB": ["test_db"], "CS": ["test_schema"]}
    return mock_session


@pytest.fixture(scope="module")
def snowflake_connection(mocker, mock_snowflake_session):
    """
    Creates a Snowflake connection
    :param mocker:
    :param mock_snowflake_session:
    :return: Snowflake connection
    """
    mocker.patch.object(SnowflakeConnection, '_create_session', return_value=mock_snowflake_session)
    return SnowflakeConnection()
