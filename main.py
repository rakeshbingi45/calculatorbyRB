import streamlit as st

st.title("Calculator")

fn=st.number_input("Enter Your First Number: ")
sn=st.number_input("Enter Your Second Number: ")
        
c1,c2,c3,c4=st.columns(4)
with c1:
    add=st.button("Addition (+)")
    if add:
        st.write(f"{fn+sn}")

with c2:   
    sub=st.button("Subtraction (-)")
    if sub:
        st.write(f"{fn-sn}")

with c3:   
    mul = st.button("Multiplication (*)")
    if mul:
        st.write(f"{fn*sn}")

with c4: 
    div=st.button("Division (/)")
    if div:
        print(sn)
        if(sn == 0.00):
            st.write("Cannot be divided by Zero")
        else:
            st.write(f"{fn/sn:.2f}")