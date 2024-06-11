import streamlit as st
from backend.data_operations import get_tables, get_dataset
from backend.snowflake_connection import SnowflakeConnection
from backend.sql_statements import delete_cols, insert_cols, process_cols, select_cols

st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")

sf_conn = SnowflakeConnection()

st.title("Snowflake Table Editor ❄️")

# Form to select the table
with st.form("table_selector_form"):
    tdf = get_tables()
    tab_name = st.selectbox("Select Table to Edit:", tdf)
    table_submit_button = st.form_submit_button("Select ...")

if table_submit_button:
    st.session_state['HAVE_TABLE'] = True
    st.session_state['tab_name'] = tab_name
    st.experimental_rerun()

# Check if a table has been selected
if 'HAVE_TABLE' in st.session_state:
    tab_name = st.session_state['tab_name']
    with st.form("data_editor_form"):
        dataset = get_dataset(tab_name)
        st.caption("Edit the dataframe below")
        edited_data = st.data_editor(dataset, use_container_width=True, num_rows="dynamic", key='ed')
        debug = st.checkbox('Debug')
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        try:
            # Process updated rows
            for rec in edited_data.get("edited_rows", {}):
                idx = int(rec)
                update_stmt = f"UPDATE {tab_name} SET {process_cols(edited_data['edited_rows'][rec])} WHERE {select_cols(dataset, idx)}"
                if debug:
                    st.write("Update SQL:", update_stmt)
                sf_conn.session.sql(update_stmt).collect()

            # Process inserted rows
            for irec in edited_data.get("added_rows", []):
                insert_stmt = insert_cols(irec, tab_name)
                if debug:
                    st.write("Insert SQL:", insert_stmt)
                sf_conn.session.sql(insert_stmt).collect()

            # Process deleted rows
            for rec in edited_data.get("deleted_rows", []):
                idx = int(rec)
                delete_stmt = delete_cols(idx, dataset, tab_name)
                if debug:
                    st.write("Delete SQL:", delete_stmt)
                sf_conn.session.sql(delete_stmt).collect()

            st.success("Table updated successfully")
        except Exception as e:
            st.warning(f"Error updating table: {e}")
