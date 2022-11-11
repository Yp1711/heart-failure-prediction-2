import streamlit as st
import joblib


def main():
    html_temp="""
    <div style="background-color:lightblue">
    <h2> heart attack prediction</h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    # load the model
    model = joblib.load('knn')
    
    p1 = st.number_input("age")
    
    s2=st.selectbox("anaemia",("Yes","No"))
    if s2=="Yes":
        p2=1
    else:
        p2=0
    s3=st.selectbox("diabetes",("Yes","No"))
    if s3=="Yes":
        p3=1
    else:
        p3=0
    
    s5=st.selectbox("high blood pressure",("Yes","No"))
    if s5=="Yes":
        p4=1
    else:
        p4=0
    p5 = st.number_input("time")
    p6= st.number_input("ejection_fraction")
    p7=st.number_input("serum_creatinine")
    
    s4=st.selectbox("Smoker",("Yes","No"))
    if s4=="Yes":
        p8=1
    else:
        p8=0
        
    
    if st.button('Predict'):
        prediction = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8]])
        #st.write(prediction)
        if prediction==1:
            st.success('high chance of heart fialure ')
        else:
            st.success('low chance of heart fialure ')
    
if __name__ == '__main__':
    main()