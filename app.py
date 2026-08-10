import streamlit as st

# st.title("My Streamlit App")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is a text element.")
# st.write("This is a write element.")
# st.markdown("This is a **markdown** example.")
# st.code("def hello():\n\tprint('Hello, Streamlit!')")


# Ask user for length n feet and display that on centimeters

st.title("Length Converter")
st.text("This application coverts length from feet to centimeters.")
length_feet = st.number_input("Enter the length in feet:", min_value=0.0, step=0.1)
button_clicked = st.button("Convert")
if button_clicked:
    length_cm = length_feet * 30.48
    st.warning(f"{length_feet} ft = {length_cm:.2f} cm")



