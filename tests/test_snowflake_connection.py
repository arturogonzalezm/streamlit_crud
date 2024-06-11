from backend.snowflake_connection import SnowflakeConnection


def test_singleton_pattern(snowflake_connection):
    instance1 = SnowflakeConnection()
    instance2 = SnowflakeConnection()
    assert instance1 is instance2
