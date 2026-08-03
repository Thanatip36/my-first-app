import streamlit as st
st.title("แอปพลีเคชั่นแปลง พ.ศ. เป็น ค.ศ.")
bh_year = st.number_input("กรอก พ.ศ. ที่ต้องการแปลง", value=2569)
ce_year = bh_year - 543
if ce_year > 0: 
  st.header(f"ปี ค.ศ.คือ : {ce_year}")
else:
  st.header(f"ปี : {abs(ce_year)} ก่อนคริสตกาล ")
