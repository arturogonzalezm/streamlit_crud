from snowflake.snowpark import Session


class SnowflakeConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SnowflakeConnection, cls).__new__(cls)
            cls._instance._session = cls._create_session()
        return cls._instance

    @property
    def session(self):
        return self._session

    @staticmethod
    def _create_session():
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
