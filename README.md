[![codecov](https://codecov.io/gh/arturogonzalezm/update_snowflake_tables_from_streamlit/graph/badge.svg?token=aPB4a2ulm9)](https://codecov.io/gh/arturogonzalezm/update_snowflake_tables_from_streamlit)
[![PyLint](https://github.com/arturogonzalezm/update_snowflake_tables_from_streamlit/actions/workflows/workflow.yml/badge.svg)](https://github.com/arturogonzalezm/update_snowflake_tables_from_streamlit/actions/workflows/workflow.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)

# StreamLit CRUD App

This project is a Streamlit application for editing Snowflake tables. The application allows users to select a table from Snowflake, edit the data, and apply changes (update, insert, delete) directly to the Snowflake database.

## Project Structure

```python
streamlit_crud/
│
├── app.py
├── backend/
│ ├── init.py
│ ├── data_operations.py
│ ├── snowflake_connection.py
│ └── sql_statements.py
├── tests/
│ ├── init.py
│ ├── test_data_operations.py
│ ├── test_snowflake_connection.py
│ └── test_sql_statements.py
```

## Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant StreamlitApp
    participant DataOperations
    participant SQLStatements
    participant SnowflakeConnection

    User->>StreamlitApp: Select Table
    StreamlitApp->>DataOperations: get_tables()
    DataOperations->>SnowflakeConnection: session
    SnowflakeConnection-->>DataOperations: return session
    DataOperations-->>StreamlitApp: return tables

    User->>StreamlitApp: Edit Data
    StreamlitApp->>DataOperations: get_dataset(tabname)
    DataOperations->>SnowflakeConnection: session
    SnowflakeConnection-->>DataOperations: return session
    DataOperations-->>StreamlitApp: return dataset

    User->>StreamlitApp: Submit Changes
    StreamlitApp->>SQLStatements: process_cols(edited_rows)
    StreamlitApp->>SQLStatements: select_cols(dataset, idx)
    StreamlitApp->>SQLStatements: insert_cols(added_rows, tabname)
    StreamlitApp->>SQLStatements: delete_cols(idx, dataset, tabname)
    SQLStatements-->>StreamlitApp: return SQL statements

    StreamlitApp->>SnowflakeConnection: Execute SQL Statements
    SnowflakeConnection-->>StreamlitApp: return execution result

    StreamlitApp->>User: Display Success/Error Message
```

### Files Description

- `main.py`: The main Streamlit application file that includes the UI for selecting and editing Snowflake tables.
- `backend/`: Directory containing the backend logic.
  - `__init__.py`: Indicates that the directory is a Python package.
  - `data_operations.py`: Functions for interacting with Snowflake tables (e.g., `get_dataset`, `get_tables`).
  - `snowflake_connection.py`: Singleton class for managing the Snowflake connection.
  - `sql_statements.py`: Functions for generating SQL statements (e.g., `process_cols`, `select_cols`, `insert_cols`, `delete_cols`).
- `tests/`: Directory containing the unit tests.
  - `__init__.py`: Indicates that the directory is a Python package.
  - `test_data_operations.py`: Unit tests for the `data_operations.py` module.
  - `test_snowflake_connection.py`: Unit tests for the `snowflake_connection.py` module.
  - `test_sql_statements.py`: Unit tests for the `sql_statements.py` module.

## Running the Application

To run the Streamlit application, execute the following command in your terminal:

```sh
streamlit run app.py
```

This will start the Streamlit server and open the application in your default web browser.

## Running the Tests

To run the unit tests, execute the following command in your terminal:

```sh
pytest
```

This will run all the tests in the `tests/` directory and display the results in the terminal.

## Class Diagram

```mermaid
classDiagram
    class SnowflakeConnection {
        -session: Session
        +session: Session
        +_create_session(): Session
    }

    class data_operations {
        +get_dataset(table_name: str): DataFrame
        +get_tables(): DataFrame
    }

    class sql_statements {
        +process_cols(columns: dict): str
        +select_cols(df: DataFrame, idx: int): str
        +insert_cols(cols: dict, tabname: str): str
        +delete_cols(idx: int, df: DataFrame, tabname: str): str
    }

    SnowflakeConnection --> data_operations : Uses
    SnowflakeConnection --> sql_statements : Uses
```

## License

This project is licensed under the terms of the MIT license.
