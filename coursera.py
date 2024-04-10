import streamlit as st
import pandas as pd

st.balloons()
st.write("""
## Filter Coursera Courses🪄
""")

# Form for user input
with st.form("course_filter_form"):
    company = st.selectbox('🏢Company', ('Google', 'Microsoft', 'Meta','DeepLearning.AI','Amazon Web Services','Google Cloud'))
    rating = st.selectbox('😶Ratings', ('3.0', '4.0', '4.5'))
    difficulty = st.selectbox('🪫Difficulty', ('Beginner', 'Intermediate', 'Advanced'))
    submitted = st.form_submit_button("Submit")

# Handle form submission
if submitted:
    st.write("Selected Company:", company)
    st.write("Selected Ratings:", rating)
    st.write("Selected Difficulty:", difficulty)

    # Load dataset
    file = pd.read_csv('./excelfile.csv')

    def filter_df(input_df, company, difficulty, rating):
        try:
            filtered_data = input_df.loc[
                (input_df['Company_Name'] == company) &
                (input_df['Difficulty'] == difficulty) &
                (input_df['Ratings'] >= float(rating))
            ]
            return filtered_data[['Course_Name', 'Ratings', 'Link']].sort_values(by='Ratings', ascending=False)
        except KeyError:
            print("KeyError occurred")
            return pd.DataFrame()

    # Display filtered data
    filtered_data = filter_df(file, company, difficulty, rating)
    if not filtered_data.empty:
        filtered_data = filtered_data.reset_index(drop=True)
        filtered_data.index += 1
        # Make the 'Link' column clickable
        filtered_data['Link'] = filtered_data['Link'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
        st.write(filtered_data.to_html(escape=False), unsafe_allow_html=True)
    else:
        st.write("No courses match the selected criteria.")
