import streamlit as st
import plotly.express as px
import plotly.data

# getting a dataset from plotly
data_frame = plotly.data.gapminder()

# unique country list
countries = data_frame['country'].unique()

st.header('Visualisation of the gapmider data')
st.write('Cras vel massa vitae neque euismod suscipit. Phasellus fringilla eget justo vitae consectetur. Proin lacus nibh, volutpat ac aliquet eu, viverra vel risus. Vestibulum eleifend magna non mi hendrerit, at efficitur arcu tempor. Nulla facilisi. Vestibulum lorem velit, dignissim eu nisi et, venenatis ultrices lacus. Cras volutpat blandit est. Mauris gravida nisl ut nunc sodales egestas. Nam nec nunc scelerisque, semper orci vel, convallis mi. In semper felis nulla, quis volutpat massa suscipit nec. Quisque at mi vitae magna interdum sollicitudin et vitae libero. Duis cursus massa at felis maximus fermentum. Nunc ornare, augue sed pulvinar condimentum, dui sapien dapibus purus, vitae laoreet sem lectus eu odio. Duis sit amet tempus tortor. Nunc venenatis ut dui sed lobortis.')

options = st.multiselect('Choose one or more countries from the dropdown list', countries)

if options:
    # filter based on the chosen countries
    updated_df = data_frame[data_frame['country'].isin(options)]
    st.subheader('2D line plot of year vs life expectency')
    fig = px.line(updated_df, x="year", y="lifeExp", color="country") 
    st.plotly_chart(fig)
    
    st.subheader('3D line plot of year vs life expectency vs GDP per capital')
    fig_2 = px.line_3d(updated_df, x="year", y="lifeExp", z="gdpPercap", color="country") 
    st.plotly_chart(fig_2)


