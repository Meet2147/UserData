import streamlit as st
import requests
import base64
import json
def generate_qr_code(details):
    base_url = "https://quickchart.io/qr"
    params = {"text": details}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.content

    return None

def main():
    st.title('User Details QR Code Generator')

    name = st.text_input('Enter your name:')
    age = str(st.number_input('Enter your age:', min_value=0, max_value=150, value=0))
    phone_number = st.text_input('Enter your phone number:')
    para = st.text_input('Enter your para/vistar:')
    edu = st.text_input('Enter your education:')
    email = st.text_input('Enter your email address:')
    status = st.selectbox('Are you a student or Professional?',('Student', 'Professional'))

    # user_details = f"Name: {name}, Age: {age}, Phone Number: {phone_number}, Address: {para}, Education: {edu}, Email: {email}, Status: {status}"
    user_details = ', '.join([name, age, phone_number, para, edu, email, status])
    details = f"{name}, {age}, {phone_number}, {para}, {edu}, {email}, {status}"

    st.write(details)
    
    

    if st.button('Generate QR Code'):
        
        qr_image = generate_qr_code(details)

        if qr_image:
            st.image(qr_image, caption='Generated QR Code', use_column_width=False)
            st.markdown(get_binary_file_downloader_html(qr_image, 'QR_Code.png', 'Download QR Code'), unsafe_allow_html=True)
        else:
            st.warning("Failed to generate QR code. Please check your input and try again.")

def get_binary_file_downloader_html(bin_file, file_label='File', button_label='Download'):
    bin_file_b64 = base64.b64encode(bin_file).decode()
    return f'<a href="data:image/png;base64,{bin_file_b64}" download="{file_label}">{button_label}</a>'

if __name__ == '__main__':
    main()
