import streamlit as st
st.title("menabung")

with st.form("nabung"):
    nama = st.text_input("nama")
    jumlah = st.number_input("jumlah duid (Rp.)", min_value=0)
    tanggal = st.date_input("tanggal")
    waktu = st.time_input("jam/waktu")
    submit_button = st.form_submit_button(label="menabung")
    
    if submit_button and jumlah >=5000:
        st.session_state['total_semua'].append({
            'tipe' : 'menabung',
            'jumlah' : jumlah
        })
        st.success("menabung berhasil")
    else:
        st.error("menabung gagal")
        