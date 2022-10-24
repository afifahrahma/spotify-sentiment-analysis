import streamlit as st
import pandas as pd
import seaborn  as sns
import matplotlib.pyplot as plt

def run():
    #Set page_title and title
    st.title ('Exploratory Data Analysis')

    # Make Sub  Header
    st.subheader('EDA of Spotify Reviews Dataset')

    # Make Description
    st.write('Afifah Rahma - Batch-015-RMT')

    # Make a line
    st.markdown('-----------')

    # Make brief explanation
    st.write("Below are some of the simple exploratory data analysis of Spotify Analysis Review Dataset. The dataset was collected from kaggle.com.")
    st.write("[Access Dataset >](https://www.kaggle.com/datasets/mfaaris/spotify-app-reviews-2022)")

    st.markdown("-----------")


    # Show DataFrame
    st.write('### Spotify App Reviews Dataset')
    df = pd.read_csv('https://raw.githubusercontent.com/afifahrahma/learning_data/main/reviews.csv')

    st.dataframe(df)

    # Membuat Barplot
    fig= plt.figure(figsize = (10,8))
    sns.countplot(x = 'Rating', data = df)
    plt.title('Frequency of Ratings', weight='bold', fontsize=15)
    st.pyplot(fig)

    def ratings(rating):
        if rating > 3:
            return "Good"
        else:
            return "Bad"

    df['Rating'] = df['Rating'].apply(ratings)

    st.write('#### Percentage of Sentiments')
    fig = plt.figure(figsize=(4,4))
    df.Rating.value_counts().plot(kind='pie', autopct='%1.1f%%')
    st.pyplot(fig)

if __name__ == '__main__':
    run()