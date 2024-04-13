import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Загрузка данных и автоматическое кэширование с помощью st.cache
@st.cache_data
def load_data():
    return pd.read_csv("sallary2000-2023.csv")

# Загрузка данных и кэширование
df = load_data()

# Отображение данных
st.write(df)


fig, ax = plt.subplots()
ax.plot(df.columns[1:], df.iloc[0, 1:], label='Всего по экономике')
ax.plot(df.columns[1:], df.iloc[1, 1:], label='Строительство')
ax.plot(df.columns[1:], df.iloc[2, 1:], label='Финансовая деятельность')
ax.plot(df.columns[1:], df.iloc[3, 1:], label='Образование')
ax.set_xlabel('Год')
ax.set_ylabel('Значение')
ax.set_title('Динамика данных по годам')
ax.legend()
st.pyplot(fig)

fig = go.Figure()

fig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[0, 1:], mode='lines', name='Всего по экономике'))
fig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[1, 1:], mode='lines', name='Строительство'))
fig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[2, 1:], mode='lines', name='Финансовая деятельность'))
fig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[3, 1:], mode='lines', name='Образование'))

fig.update_layout(title='Динамика данных по годам',
                  xaxis_title='Год',
                  yaxis_title='Значение')

st.plotly_chart(fig)