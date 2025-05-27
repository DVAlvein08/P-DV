
import streamlit as st
import pandas as pd
import joblib
import base64
from io import BytesIO

st.set_page_config(page_title="AI Dự đoán Tác nhân và Gợi ý Kháng sinh", layout="wide")
st.title("🧬 AI Dự đoán Tác nhân và Gợi ý Kháng sinh")

# Giải mã mô hình từ base64
encoded = """gASV8AAAAAAAAACMCF9fbWFpbl9flIwKRHVtbXlNb2RlbJSTlCmBlH2UjAhjbGFzc2VzX5SME2pvYmxpYi5udW1weV9waWNrbGWUjBFOdW1weUFycmF5V3JhcHBlcpSTlCmBlH2UKIwIc3ViY2xhc3OUjAVudW1weZSMB25kYXJyYXmUk5SMBXNoYXBllEsEhZSMBW9yZGVylIwBQ5SMBWR0eXBllGgMaBOTlIwDVTEzlImIh5RSlChLA4wBPJROTk5LNEsESwh0lGKMCmFsbG93X21tYXCUiIwbbnVtcHlfYXJyYXlfYWxpZ25tZW50X2J5dGVzlEsQdWIE/////1MAAAAuAAAAIAAAAHAAAABuAAAAZQAAAHUAAABtAAAAbwAAAG4AAABpAAAAYQAAAAAAAABNAAAALgAAACAAAABwAAAAbgAAAGUAAAB1AAAAbQAAAG8AAABuAAAAaQAAAGEAAAAAAAAAUgAAAFMAAABWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgAAAAuAAAAIAAAAGkAAABuAAAAZgAAAGwAAAB1AAAAZQAAAG4AAAB6AAAAYQAAAGUAAABzYi4="""
model_bytes = BytesIO(base64.b64decode(encoded))
model = joblib.load(model_bytes)

st.header("📋 Nhập dữ liệu lâm sàng")
tuoi = st.number_input("Tuổi", min_value=0.0)
benh_ngay_thu = st.number_input("Bệnh ngày thứ trước khi nhập viện", min_value=0.0)
sot = st.radio("Sốt", ["Không", "Có"]) == "Có"
ho = st.radio("Ho", ["Không", "Có"]) == "Có"
ran_phoi = st.radio("Ran phổi", ["Không", "Có"]) == "Có"
nhip_tho = st.number_input("Nhịp thở", min_value=0.0)
mach = st.number_input("Mạch", min_value=0.0)
spo2 = st.number_input("SpO2", min_value=0.0)
nhiet_do = st.number_input("Nhiệt độ", min_value=0.0)
crp = st.number_input("CRP", min_value=0.0)
bach_cau = st.number_input("Bạch cầu", min_value=0.0)
ks_truoc = st.radio("Sử dụng kháng sinh trước nhập viện", ["Không", "Có"]) == "Có"

if st.button("🔍 Dự đoán"):
    input_data = pd.DataFrame([{
        "Tuoi": tuoi,
        "Benh ngay thu": benh_ngay_thu,
        "Sot": int(sot),
        "Ho": int(ho),
        "Ran phoi": int(ran_phoi),
        "Nhip tho": nhip_tho,
        "Mach": mach,
        "SpO2": spo2,
        "Nhiet do": nhiet_do,
        "CRP": crp,
        "Bach cau": bach_cau,
        "Khang sinh truoc": int(ks_truoc)
    }])
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Tác nhân gây bệnh dự đoán: **{prediction}**")

    st.markdown("## 💊 **Kháng sinh gợi ý:**")
    ABX_MAP = {'S. aureus': ['Benzylpenicillin', 'Oxacillin', 'Gentamicin', 'Ciprofloxacin', 'Moxifloxacin', 'Erythomycin', 'Clindamycin', 'Linezolid', 'Teicoplanin', 'Vancomycin', 'Tetracyline', 'Tigecycline', 'Fusidic acid', 'Rifampicin', 'Trimrthoprim'], 'S. pneumonia': ['Benzylpenicillin', 'Oxacillin', 'Gentamicin', 'Ciprofloxacin', 'Moxifloxacin', 'Erythomycin', 'Clindamycin', 'Linezolid', 'Teicoplanin', 'Vancomycin', 'Tetracyline', 'Tigecycline', 'Fusidic acid', 'Rifampicin'], 'H. Influenzae': ['Benzylpenicillin', 'Oxacillin', 'Ciprofloxacin', 'Moxifloxacin', 'Erythomycin', 'Clindamycin', 'Vancomycin'], 'M. catarrhalis': ['Benzylpenicillin', 'Oxacillin', 'Gentamicin', 'Ciprofloxacin', 'Moxifloxacin'], 'K. pneumoniae': ['Benzylpenicillin', 'Oxacillin', 'Gentamicin', 'Ciprofloxacin', 'Moxifloxacin', 'Erythomycin', 'Clindamycin', 'Linezolid', 'Teicoplanin', 'Vancomycin', 'Tetracyline', 'Tigecycline', 'Fusidic acid', 'Rifampicin'], 'S. epidermidis': ['Benzylpenicillin', 'Oxacillin', 'Gentamicin', 'Ciprofloxacin', 'Moxifloxacin', 'Erythomycin', 'Clindamycin', 'Linezolid', 'Teicoplanin', 'Vancomycin', 'Tetracyline', 'Tigecycline', 'Fusidic acid', 'Rifampicin', 'Trimrthoprim'], 'S. mitis': ['Benzylpenicillin', 'Oxacillin', 'Gentamicin', 'Ciprofloxacin', 'Moxifloxacin', 'Erythomycin', 'Clindamycin', 'Linezolid', 'Teicoplanin', 'Vancomycin', 'Tetracyline', 'Tigecycline', 'Fusidic acid'], 'M. pneumonia': ['Azithromycin', 'Clarithromycin', 'Doxycycline', 'Levofloxacin', 'Moxifloxacin'], 'RSV': []}
    abx_list = ABX_MAP.get(prediction, [])
    if abx_list:
        for abx in abx_list:
            st.markdown(f"- {abx}")
    else:
        st.info("Không có khuyến cáo kháng sinh cho tác nhân này.")
