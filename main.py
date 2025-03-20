import streamlit as st
import requests

api_key = 'cnQrGljCEWRwLWetscgmhbbuNJSc8ANj2PqR165c'

url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

response = requests.get(url)
content = response.json()

print(content)
print(type(content))

image = requests.get(content['hdurl'])
with open('image.png', 'wb') as file:
    file.write(image.content)

date = content['date']
explanation = content['explanation']
title = content['title']

st.set_page_config(layout='wide')

st.header(title)
st.image('image.png')
st.text(explanation)


