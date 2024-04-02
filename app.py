import streamlit as st

st.markdown("""
    <h1 style='color: gray;'>Hello Edvin!</h1>
    """, unsafe_allow_html=True)

st.markdown("""
    <p style='color: white;'>Edvin is an Artificial Intelligence bot (AI) who provides information about licensing</p>
    <p style='color: #89CFF0;'>The information provided is only relates to Brighton and Hove City Council, other councils may operate differently</p>
            
    <p style='color: white; margin-top: 20px;'>What can Edvin Help you with?</p>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.write("Street trading")
    st.write("- Fees and Zone information")
    st.write("- Zone B Trading Map")
    st.write("- Links to applications")

with col2:
    st.write("Personal Licences")
    st.write("- Fees and Document requirements")
    st.write("- Process of address changes and replacement requests")
    st.write("- Links to applications")

with col3:
    st.write("Temporary Event Notices (TEN)")
    st.write("- Fees and Document requirements")
    st.write("- Event notice guidance")
    st.write("- Links to applications")

st.markdown("""
    <p style='color: red;'>Please note, Edvin is still under development and it might not stick arouund, it is always the best to get intouch with the licensing department</p>
    """, unsafe_allow_html=True)