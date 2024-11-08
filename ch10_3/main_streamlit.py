import streamlit as st
from CustomerDAO import CustomerDAO

def main():
    st.set_page_config(layout="wide")
    st.write('# Hello')
    dao = CustomerDAO(r'..\customers_db.db')
    customers = dao.find_all()

    name = st.text_input("Your name", " ")

    st.button("Reset", type="primary")
    if st.button("Say hello"):
        st.write(f"Hello {name}")
    else:
        st.write("Goodbye")
    
    st.table(customers)
        
        
if __name__=='__main__':
    # streamlit run .\main_streamlit.py
    main()
