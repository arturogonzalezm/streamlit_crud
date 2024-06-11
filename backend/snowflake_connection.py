"""
This module is responsible for creating a Snowflake connection and returning the session.
The session is used to interact with the Snowflake database.
"""

from snowflake.snowpark import Session


class SnowflakeConnection:
    """
    Singleton class to create a Snowflake connection
    """
    _instance = None

    def __new__(cls):
        """
        Creates a singleton instance of the Snowflake connection
        :return: Snowflake connection instance
        """
        if cls._instance is None:
            cls._instance = super(SnowflakeConnection, cls).__new__(cls)
            cls._instance._session = cls._create_session()
        return cls._instance

    @property
    def session(self):
        """
        Returns the Snowflake session
        :return: Snowflake session
        """
        return self._session

    @staticmethod
    def _create_session():
        """
        Creates a Snowflake session
        :return: Snowflake session
        """
        connection_parameters = {
            "account": "<YOUR_ACCOUNT>",
            "user": "<YOUR_USER>",
            "password": "<YOUR_PASSWORD>",
            "role": "<YOUR_ROLE>",
            "warehouse": "<YOUR_WAREHOUSE>",
            "database": "<YOUR_DATABASE>",
            "schema": "<YOUR_SCHEMA>"
        }
        return Session.builder.configs(connection_parameters).create()
