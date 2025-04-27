import streamlit as st
import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root@localhost",
        password="Nike1@shoes",
        database="GenomicsDB"
    )
    return connection

conn = create_connection()
cursor = conn.cursor()

cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()

st.title("🧬 GenomicsDB Viewer")

for table in tables:
    st.subheader(f"📄 Table: {table[0]}")
    cursor.execute(f"SELECT * FROM {table[0]}")
    data = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    st.dataframe(data, columns=columns)
cursor.close()
conn.close()    

