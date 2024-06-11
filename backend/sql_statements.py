def process_cols(columns):
    """
    Process the columns to be updated
    :param columns: dict of columns
    :return: str
    """
    return ", ".join([f"{col} = '{val}'" for col, val in columns.items()])


def select_cols(df, idx):
    """
    Generate the WHERE clause for the SQL statement
    :param df:
    :param idx:
    :return: str
    """
    conditions = [f"{col} = '{df.iloc[idx][col]}'" if df.iloc[idx][col] is not None else f"{col} IS NULL" for col in
                  df.columns]
    return " AND ".join(conditions)


def insert_cols(cols, tabname):
    """
    Generate the INSERT statement
    :param cols:
    :param tabname:
    :return: str
    """
    columns = ", ".join(cols.keys())
    values = ", ".join([f"'{val}'" for val in cols.values()])
    return f"INSERT INTO {tabname} ({columns}) VALUES ({values})"


def delete_cols(idx, df, tabname):
    """
    Generate the DELETE statement
    :param idx:
    :param df:
    :param tabname:
    :return: str
    """
    conditions = [f"{col} = '{df.iloc[idx][col]}'" if df.iloc[idx][col] is not None else f"{col} IS NULL" for col in
                  df.columns]
    return f"DELETE FROM {tabname} WHERE " + " AND ".join(conditions)
