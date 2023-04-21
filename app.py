import streamlit as st
import pandas as pd
from subprocess import call # Import subprocess to run tiktok script from command line
import plotly.express as px

# Set page width to wide
st.set_page_config(layout='wide')

st.title("Tiktok Analysis")
# Create sidebar
st.sidebar.markdown("<div><img src='https://media1.giphy.com/media/wTCTufYunsSmFPxjcr/giphy.gif?cid=ecf05e47fyqv6w1ctxepd3anve29lo78crgf6ltjtwc5975d&rid=giphy.gif&ct=s' width = 200></h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to analyse trending tiktoks using Python and Streamlit.")
st.sidebar.markdown("To get started <ol><li>Enter the <i>hashtag</i> you wish to analyse</li> <li>Hit <i>Analyze</i>.</li> <li>Get analyzing</li></ol>",unsafe_allow_html=True)

# Input 
hashtag = st.text_input('Search for a hashtag here', value="")

# Tab
tab1, tab2, tab3 = st.tabs(["Histogram", "Scatter", "Tabular Data"])

# Button
if st.button('Analyze'):
    # Run get data function here
    call(['python', 'tiktok.py', hashtag])
    # Load in existing data to test it out
    df = pd.read_csv('tiktokdata.csv')

    with tab1:
        #1 Plotly viz here
        fig = px.histogram(df, x='desc', hover_data=['desc'], y='stats_diggCount', height=300) 
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        # Split columns
        left_col, right_col = st.columns(2)

        # First Chart - video stats
        scatter1 = px.scatter(df, x='stats_shareCount', y='stats_commentCount', hover_data=['desc'], size='stats_playCount', color='stats_playCount')
        left_col.plotly_chart(scatter1, use_container_width=True)

        # Second Chart
        scatter2 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
        right_col.plotly_chart(scatter2, use_container_width=True)

    with tab3:
        # Show tabular dataframe in streamlit
        df