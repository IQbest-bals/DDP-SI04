import streamlit as st 

st.title("Hallo Mabro")
st.write("selamat datang di mobil impian")
st.image("alphard.jpg", caption="ini gambarnya")

dashboard = st.Page("fitur/dashboard.py", title="Dashboard")
nabung = st.Page("fitur/nabung.py", title="menabung")

pg = st.navigation(
    {
    "menu utama" : [dashboard],
    "transaksi" : [nabung],
    }
)

if 'total semua' not in st.session_state:
    st.session_state['total_semua'] = []
    
pg.run()