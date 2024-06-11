from backend.snowflake_connection import SnowflakeConnection

sf_conn = SnowflakeConnection()


def get_dataset(table_name):
    df = sf_conn.session.table(table_name).to_pandas()
    df.reset_index(drop=True, inplace=True)
    return df


def get_tables():
    db_name = sf_conn.session.sql("select current_database() as DB").to_pandas()['DB'][0]
    schema = sf_conn.session.sql("select current_schema() as CS").to_pandas()['CS'][0]
    sql = f"SELECT table_name FROM {db_name}.information_schema.tables WHERE table_schema = '{schema}'"
    return sf_conn.session.sql(sql).to_pandas()
