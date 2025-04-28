import streamlit as st
st.title("BMI Calculation")

sex = st.radio("เพศ",("ชาย","หญิง"), horizontal=True)
kg=st.number_input("น้ำหนัก(kg.)",value=60.5,min_value=10.0,max_value=200.0,
                   step=0.5)
cm=st.number_input("สวนสูง(cm.)",value=100,min_value=1,max_value=200,
                   step=1)
if st.button("CALCULATE"):
    bmi=kg/(cm/100)**2
    st.write(bmi)
    if sex=="ชาย":
        if bmi < 19:
            st.info("ผอมไป")
            st.warning("เส่ียงโรคขาดสารอาหาร")
            st.image("tung.JPEG")
        elif bmi <25:
            st.success("ปกติ")
            st.warning("โอกาสมีโรคแทรกซ้อนน้อย")
            st.image("2.png")
        elif bmi < 30:
            st.warning("เกิน")
            st.warning("ภาวะน้ำหนักเกินระยะเริ่มต้น")
            st.image("3.png")
        elif bmi >= 30: 
            st.error("อ้วนมาก")
            st.warning("ภาวะน้ำหนักเกินมากโรคอ้วน")
            st.image("5.png")

    else:
        if bmi < 18:
            st.info("ผอมไป")
            st.warning("เส่ียงโรคขาดสารอาหาร")
            st.image("bmi-fe1.png")
        elif bmi <24:
            st.success("ปกติ")
            st.warning("โอกาสมีโรคแทรกซ้อนน้อย")
            st.image("bmi-fe2.png")
        elif bmi < 29:
            st.warning("เกิน")
            st.warning("ภาวะน้ำหนักเกินระยะเริ่มต้น")
            st.image("bmi-fe3.png")
        elif bmi >= 30: 
            st.error("อ้วนมาก")
            st.warning("ภาวะน้ำหนักเกินมากโรคอ้วน")
            st.image("bmi-fe4.png")

bg1="""
<style>
.stApp {
    background-color: #008000;
    color: #ffffff;
}
</style>
"""

st.html(bg1)
