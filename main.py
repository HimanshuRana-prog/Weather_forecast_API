import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecat Days",min_value=1,max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("select data to view",
                      ("Temperature","sky"))
st.subheader(f"{option} for the next {days} days in {place}")

d, t = get_data(place,days, option)
# def get_data(days):
#     dates = ["2022-25-10","2022-26-10","2022-27-10"]
#     temperature = [10,11,15]
#     temperature = [days * i for i in temperature]
#     return dates,temperature

# d, t =get_data(days)

figure = px.line(x =d,y=t,labels={"x":"Date","y":"Temperature (C)"})
st.plotly_chart(figure)