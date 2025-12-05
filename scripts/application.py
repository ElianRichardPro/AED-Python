import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("EAD d'une analyse de données de transactions par carte de crédit")
@st.cache_data

def load_data():
    df = pd.read_csv('./data/creditcard_clean.csv')
    return df

data = load_data()
st.subheader("Extrait des données")
st.write(data.head())
st.subheader("Distribution des classes de transactions")
class_counts = data['Class'].value_counts().sort_index()


fig = px.pie(
    names=class_counts.index,
    values=class_counts.values,
    color_discrete_sequence=['#2ecc71', '#e74c3c'],
    title='Distribution des classes de transactions',
    hole=0.4
)

fig.update_traces(textinfo='label+percent', hovertemplate='<b>%{label}</b><br>Transactions: %{value:,}<br>Percentage: %{percent}<extra></extra>')
st.plotly_chart(fig)

st.subheader("Quantité de transactions par classe")
fig_amount = px.histogram(
    data, x='Amount', color='Class',
    barmode='overlay',
    nbins=50,
    title='Quantité de transactions par classe',
    color_discrete_map={0: '#2ecc71', 1: '#e74c3c'}
)
fig_amount.update_traces(opacity=0.7)
st.plotly_chart(fig_amount)

st.subheader("Distribution du temps des transactions par classe")
fig_time = px.histogram(
    data, x='Time', color='Class',
    barmode='overlay',
    nbins=50,
    title='Distribution du temps des transactions par classe',
    color_discrete_map={0: '#2ecc71', 1: '#e74c3c'}
)
fig_time.update_traces(opacity=0.7)
st.plotly_chart(fig_time)

st.subheader("Résumé statistique de Time par classe")
stat_summary = data.groupby('Class').agg(['mean', 'median', 'std'])
st.write(stat_summary)
st.subheader("Boxplot de Time par classe")
fig_box = px.box(
    data, x='Class', y='Time',
    color='Class',
    title='Boxplot de Time par classe',
    color_discrete_map={0: '#2ecc71', 1: '#e74c3c'}
)
st.plotly_chart(fig_box)