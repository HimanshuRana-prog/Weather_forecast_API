import streamlit as st
import plotly.express as px
from backend import get_data

# Add Title, text_input, sliders, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecat Days",min_value=1,max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("select data to view",
                      ('Temperature','sky'))
st.subheader(f"{option} for the next {days} days in {place.title()}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place,days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a Temperature plot
            figure = px.line(x =dates,y=temperature,labels={"x":"Date","y":"Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {'Clear': "images/clear.png","Clouds": "images/cloud.png",
                    "Rain": "images/rain.png","Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width =111)

    except KeyError:
        st.info("Please Enter a vaild Place")
        st.info(f"{place.title()} is not a Vaild Place")