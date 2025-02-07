import streamlit as st
import sqlite3
import pandas as pd

# Set page configuration for a wider layout and a title
st.set_page_config(page_title="Public Libraries Data", layout="wide")

# Add custom CSS for styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f5f5;
            padding: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Database setup
db_name = "libraries.db"

# Function to get data from the database
def get_data(state=None):
    conn = sqlite3.connect(db_name)
    if state:
        query = "SELECT city, library, address, zip, phone FROM libraries WHERE state = ?"
        df = pd.read_sql_query(query, conn, params=(state,))
    else:
        query = "SELECT state, city, library, address, zip, phone FROM libraries"
        df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Streamlit app
st.title("📚 Public Libraries Data")

# Sidebar for state selection
states = [
    "All States", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "District of Columbia", "Florida"
]

selected_state = st.sidebar.selectbox("Select a State to View Libraries", states)

# Display data based on selected state
if selected_state == "All States":
    st.subheader("📑 All Public Libraries")
    data = get_data()  # Fetch all data
else:
    st.subheader(f"📑 Public Libraries in {selected_state}")
    data = get_data(selected_state)  # Fetch data for the selected state

# Search and filter within the table
search_term = st.text_input(f"Search within {selected_state}:", "")
if search_term:
    data = data[
        data.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
    ]

# Display data in a styled table
st.dataframe(
    data,
    width=1500,
    height=600,
    use_container_width=True
)



