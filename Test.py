import streamlit as st
st.title("แอปพลีเคชั่นแปลง พ.ศ. เป็น ค.ศ.")
bh_year = st.number_input("กรอก พ.ศ. ที่ต้องการแปลง", value=2569)
ce_year = bh_year - 543
before = True
if bh_year < 0:
    st.warning("ปีติดลบ")
    st.stop() 

def Reset():
    if ce_year >= 0: 
      if before:
         bh_year = -abs(bh_year)
         st.header(f"ปี ค.ศ. {ce_year}")
      else:
         st.header(f"ปี {abs(ce_year)} ก่อนคริสตกาล ")
    
if st.button("หลังพุทธศักราช"):
    before = False
    Reset()
if st.button("ก่อนปีพุทธศักราช"):
    before = True
    Reset()

Reset()
