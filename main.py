import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Загрузка данных из CSV-файла
@st.cache_resource
def load_data():
    """
    Загрузка данных из CSV-файла.

    Returns:
        DataFrame: DataFrame с данными о средней зарплате и инфляции.
    """
    return pd.read_csv("infl1404Co.csv")

# Загрузка данных
df = load_data()

# Преобразование данных для построения графика
df = df.set_index('years')  # Устанавливаем годы как индекс
df_transposed = df.T  # Транспонируем таблицу для удобства

# 2.1. Сравнительный анализ средней зарплаты по секторам

# Создание интерактивного графика
fig = go.Figure()

# Добавляем данные о средних зарплатах в каждой сфере на график
fig.add_trace(go.Scatter(x=df_transposed.index, y=df_transposed['construction_avg_salary_inflation_adjusted_2000'], mode='lines', name='Construction'))
fig.add_trace(go.Scatter(x=df_transposed.index, y=df_transposed['finance_avg_salary_inflation_adjusted_2000'], mode='lines', name='Finance'))
fig.add_trace(go.Scatter(x=df_transposed.index, y=df_transposed['education_avg_salary_inflation_adjusted_2000'], mode='lines', name='Education'))

# Настройка внешнего вида графика
fig.update_layout(
    title='Средняя зарплата с учетом инфляции (2000-2023)',
    xaxis_title='Год',
    yaxis_title='Зарплата',
    legend_title='Сектор',
    xaxis=dict(tickangle=45),
    yaxis=dict(gridcolor='lightgray'),
    hovermode='x'
)

# Отображение графика
st.plotly_chart(fig)

# 2.2. Динамика общей средней зарплаты

# Создание графика
total_salary_fig = go.Figure()

# Добавляем данные о средней зарплате в общем
total_salary_fig.add_trace(go.Scatter(x=df.columns[1:], y=df.loc['total'][1:], mode='lines', name='Total Salary'))

# Настройка внешнего вида графика
total_salary_fig.update_layout(
    title='Средняя зарплата (2000-2023)',
    xaxis_title='Год',
    yaxis_title='Зарплата',
    xaxis=dict(tickangle=45),
    yaxis=dict(gridcolor='lightgray'),
    hovermode='x'
)


# Отображение графика
st.plotly_chart(total_salary_fig)

# Создание графика
inflation_fig = go.Figure()

# Добавляем данные об инфляции
inflation_fig.add_trace(go.Scatter(x=df.columns[1:], y=df.loc['inflation_year'][1:], mode='lines', name='Inflation'))

# Настройка внешнего вида графика
inflation_fig.update_layout(
    title='Уровень инфляции (2001-2023)',
    xaxis_title='Год',
    yaxis_title='Уровень инфляции',
    xaxis=dict(tickangle=45),
    yaxis=dict(gridcolor='lightgray'),
    hovermode='x'
)

# Отображение графика
st.plotly_chart(inflation_fig)

#----------------------------

# Создание графика
gdp_fig = go.Figure()

# Добавляем данные о средней зарплате в секторе "GDP_Russia"
gdp_fig.add_trace(go.Scatter(x=df.columns[1:], y=df.loc['GDP_Russia'][1:], mode='lines', name='GDP Russia'))

# Настройка внешнего вида графика
gdp_fig.update_layout(
  title='GDP Russia (2000-2023)',
  xaxis_title='Год',
  yaxis_title='Зарплата',
  xaxis=dict(tickangle=45),
  yaxis=dict(gridcolor='lightgray'),
  hovermode='x'
)

# Отображение графика
st.plotly_chart(gdp_fig)
