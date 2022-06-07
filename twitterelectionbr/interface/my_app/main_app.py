import streamlit as st
import yfinance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
v

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

#Funcoes
def plot_graphs_mat():
    print("Loading Graphs")
    fig, ax = plt.subplots(ncols=2, figsize = (30,15))

    ax[0].plot(st.session_state.df[column])
    ax[1].plot(st.session_state.df[column])

    return st.pyplot(fig)

def plot_graphs_seaborn(df):
    print("Loading Graphs")
    fig, ax = plt.subplots(ncols=2, figsize = (30,15))

    sns.kdeplot(df[column], ax=ax[0])
    sns.boxenplot(df[column], ax=ax[1])

    return st.pyplot(fig)

def plot_plotly(df):

    fig = px.scatter(x=df['Open'], y=df['Volume'] )
    return st.plotly_chart(fig)



# Mardown para injection de css
st.markdown(
    """
    <style>
    .appview-container {

        #background-color: black;
        #background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxwbnUqIB4yY1Ya3iC7bBMIDiNoWXBy2RJXA&usqp=CAU");
    }
.css-1adrfps  {
        #background-color: coral;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""# This is a header
## This is a sub header
This is text '

""")

#Markdown usando html injection
st.markdown('''<a href="https://plotly.com/python/">plotly website</a> <br>
            <a href="https://seaborn.pydata.org/examples/index.html">Seaborn website</a> <br>
            <a href="https://matplotlib.org/stable/gallery/index">Matplotlib website</a> <br>
            <a href="https://docs.streamlit.io/library/get-started">Streamlit Docs website</a><br>
            <a href="http://awesome-streamlit.org/">Exemplos Streamlit</a>


            ''', unsafe_allow_html=True)


ticker= st.sidebar.selectbox('escolha ticker', ['BTC', 'AAPL'])

try:
    if len(st.session_state.last_ticker) != 0:
        print("sessao reiniciada")
    if (str(type(st.session_state.fig)) == "<class 'streamlit.delta_generator.DeltaGenerator'>"):
        print("Agora temos uma imagem")

except:
    st.session_state.last_ticker = ''


#Variaveis
df = ''


if 'count' not in st.session_state or (st.session_state.last_ticker != ticker) :
    st.session_state.count = 0
    @st.cache()
    def getting_data(ticker):
        df = yfinance.Ticker(ticker).history()
        pd.read_csv('/home/wagui/code/waguii/twitterelectionbr/twitterelectionbr/interface/my_app/csv_file.csv')
        #pd.read_csv('gs://bucket/csv_file.csv')
        print("Executando request")
        return df
    st.session_state.df = getting_data(ticker)
    st.session_state.fig = None


if len(st.session_state.df) != 0:
    line_count = st.slider('Select a line count', 1, 10, 3)

    # and used in order to select the displayed lines
    head_df = st.session_state.df.head(line_count)

    head_df
    column =  st.sidebar.selectbox('escolha coluna', st.session_state.df.columns.tolist())

    # if st.session_state.fig == None:
    st.markdown('Matplotlib')
    plot_graphs_mat()

    st.write("Seaborn")
    plot_graphs_seaborn(st.session_state.df)

    st.write("Plotly")
    plot_plotly(st.session_state.df)


#Session States
st.session_state.count += 1
st.session_state.last_ticker = ticker
st.write('Count = ', st.session_state.count)
