def process_cols(columns):
    return ", ".join([f"{col} = '{val}'" for col, val in columns.items()])


def select_cols(df, idx):
    conditions = [f"{col} = '{df.iloc[idx][col]}'" if df.iloc[idx][col] is not None else f"{col} IS NULL" for col in
                  df.columns]
    return " AND ".join(conditions)


def insert_cols(cols, tabname):
    columns = ", ".join(cols.keys())
    values = ", ".join([f"'{val}'" for val in cols.values()])
    return f"INSERT INTO {tabname} ({columns}) VALUES ({values})"


def delete_cols(idx, df, tabname):
    conditions = [f"{col} = '{df.iloc[idx][col]}'" if df.iloc[idx][col] is not None else f"{col} IS NULL" for col in
                  df.columns]
    return f"DELETE FROM {tabname} WHERE " + " AND ".join(conditions)
