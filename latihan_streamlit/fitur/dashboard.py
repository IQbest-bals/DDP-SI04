import streamlit as st 

st.title("ini halaman awal")
st.image("alphard.jpg", caption="nih mobilnya")

def total():
    total_semua = sum(t ['jumlah']
                       for t in st.session_state 
                       ['total_semua']
                       if t ['tipe'] == 'menabung')
    
    return total_semua

total_semua = st.session_state['total_semua']
total_nabung = total()

st.metric("total_menabung", f"Rp {total_nabung}")