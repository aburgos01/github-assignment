import streamlit as st
import pandas as pd 

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('streamlit_template/data/kart_stats.csv')

columns_to_display = ['Body', 'Weight', 'Acceleration', 'On-Road traction', 'Off-Road Traction', 'Mini-Turbo']
df_filtered = df_kart[columns_to_display]

st.dataframe(df_filtered.style
                .highlight_max(color='lightgreen', axis=0, subset=columns_to_display)
                .highlight_min(color='red', axis=0, subset=columns_to_display)
                )

st.line_chart(df_kart, x='Ground Speed', y=['Acceleration','Weight','Ground Handling','On-Road traction', 'Off-Road Traction'])

st.bar_chart(df_kart, x='Body',y=['Water Speed','Water Handling','Anti-Gravity Handling', 'Air Handling'])

chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
st.bar_chart(df_unp_kart, x='category', y='strength')