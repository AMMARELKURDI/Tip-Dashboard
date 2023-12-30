import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

#st.set_page_config(page_title="Tip Dashboard",layout="wide")
#st.set_page_config

df=pd.read_csv("tips.csv")
st.sidebar.header("Tips Dashborad")
st.sidebar.image("images.png")
st.sidebar.write("Filter Your Data")
Cat_1=st.sidebar.selectbox("Categorial",[None,"sex","time","day","smoker"])
Num_1=st.sidebar.selectbox("Numerical",[None,"total_bill","tip","size"])
row_filter=st.sidebar.selectbox("Row Filter",[None,"sex","time","day","smoker"])
col_filter=st.sidebar.selectbox("Columns Filter",[None,"sex","time","day","smoker"])

st.sidebar.write("This Dashboard is based on Tips Dataset from Seaborn for Education Purpose")
st.sidebar.write("")

st.sidebar.markdown("Made with :heart_eyes: by [Ammar ELKURDI]")
a1,a2,a3,a4=st.columns(4)

a1.metric("Max Tota bill",df["total_bill"].max(),delta_color="inverse")
a2.metric("Min Tota bill",df["total_bill"].min(),delta_color="inverse")
a3.metric("Max tip",df["tip"].max(),delta_color="inverse")
a4.metric("Min tip",df["tip"].min(),delta_color="inverse")

st.subheader("Total Bill Vs Tips")
fig1=px.scatter(data_frame=df,x="total_bill",y="tip",size=Num_1,color=Cat_1,facet_col=col_filter,facet_row=row_filter)
st.plotly_chart(fig1,use_container_width=True)

b1,b2,b3=st.columns((4,3,3))
with b1:
    st.text("Sex Vs Total_bill")
    fig2=px.bar(data_frame=df,x="sex",y="total_bill",color=Cat_1)
    st.plotly_chart(fig2,use_container_width=True)

with b2:
    st.text("Smoker Vs Tip")
    fig3=px.pie(data_frame=df,names="smoker",values="tip",color=Cat_1)
    st.plotly_chart(fig3,use_container_width=True)

with b3:
    st.text("Day Vs Tips")
    fig4=px.pie(data_frame=df,names="day",values="tip",hole=0.4,color=Cat_1)
    st.plotly_chart(fig4,use_container_width=True)
