import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EireEat", page_icon="🍀")

st.title("🍀 EireEat: Irish Dietician Assistant")
st.write("Welcome to your mobile-ready nutrition tracker.")

# Sample Irish Food Data
data = {
    'Food Item': ['Porridge (Oats)', 'Irish Stew', 'Boxty (Potato Pancake)', 'Baked Salmon'],
    'Calories': [150, 350, 210, 250],
    'Protein (g)': [5, 25, 4, 22]
}
df = pd.DataFrame(data)

# Interactive UI
st.subheader("Daily Menu Options")
st.dataframe(df, use_container_width=True)

# Visualization
st.subheader("Calorie Breakdown")
fig, ax = plt.subplots()
ax.barh(df['Food Item'], df['Calories'], color='#169b62') # Irish Green
ax.set_xlabel('Calories')
st.pyplot(fig)

st.success("App is running successfully in the cloud!")
