import streamlit as st
import plotly.express as px
import pandas as pd

# st.set_page_config(layout="wide")

# read the csv file
data_frame = pd.read_csv('TIOBE Index for December 2021.csv')
data_frame['Ratings'] = data_frame['Ratings'].astype(float)
# print(data_frame.head())
# shuffle the data frame randomly
# data_frame = data_frame.sample(frac = 1)


# creating a plotly viz
fig = px.scatter(data_frame, x="Rank", y="Programming language", 
                size='Ratings', hover_data=['Programming language'], color='Ratings')

# fig.show()
st.header('Top 20 programming languages: TIOBE Index 2021')
st.write('The TIOBE Programming Community index is an indicator of the popularity of programming languages. The index is updated once a month. The ratings are based on the number of skilled engineers world-wide, courses and third party vendors. Popular search engines such as Google, Bing, Yahoo!, Wikipedia, Amazon, YouTube and Baidu are used to calculate the ratings. It is important to note that the TIOBE index is not about the best programming language or the language in which most lines of code have been written.')

st.plotly_chart(fig, use_container_width=True)

st.write('The above plot is not that exicting. It is a linear line after all. Click the below button to make it exicting!')
if st.button('CLICK ME'):
    data_frame = data_frame.sample(frac=1)
    st.write('Check out the updated plot. Isn\'t it better?')
    fig = px.scatter(data_frame, x="Rank", y="Programming language", 
                size='Ratings', hover_data=['Programming language'], color='Ratings')
    st.plotly_chart(fig)

    st.write('Looks good. But how about grouping these programming languages into groups based on the rank. ')
    with st.expander('Click here to see yet another plot'):
        fig2 = px.scatter(data_frame, x="Rank", y="Programming language", 
                size='Ratings', hover_data=['Programming language'], color='Ratings', marginal_x="histogram")
        st.plotly_chart(fig2)
