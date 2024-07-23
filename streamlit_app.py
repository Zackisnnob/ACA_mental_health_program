import streamlit as st
import pickle
import pandas as pd

pkl_filename = "pickle_model.pkl"
st.header("AI-Driven Mental Health Risk Assmt. Webapp")
st.write("Please answer the questions to the best of your ability.")
col1, col2 = st.columns(2)

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

# with col1:
    with st.form('Form1'):
        age = st.slider(label='1.What is your age?', min_value=18, max_value=100, key=0)

        gender_options = ['Male', 'Female', 'Transgender/Non Binary']
        gender = st.radio("2.Gender ", gender_options, index=0)
        gender_index = gender_options.index(gender)

        family_history_options = ['No', 'Yes']
        family_history = st.radio('3.Do you have a family history of mental illness?', family_history_options, index=0)
        family_history_index = family_history_options.index(family_history)

        benefits_options = ['Do not know', 'No', 'Yes']
        benefits = st.radio('4.Does your employer provide mental health benefits?', benefits_options, index=0)
        benefits_index = benefits_options.index(benefits)

        care_options = ['No', 'Not sure', 'Yes']
        care = st.radio('5.Do you know the options for mental health care your employer provides?', care_options, index=0)
        care_options_index = care_options.index(care)

        anonymity_options = ['Do not know', 'No', 'Yes']
        anonymity = st.radio('6.Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?', anonymity_options, index=0)
        anonymity_index = anonymity_options.index(anonymity)

        leave_options = ['Do not know', 'Somewhat Difficult','Somewhat Easy', 'Very difficult', 'Very easy']
        leave = st.radio('7.How easy is it for you to take medical leave for a mental health condition?', leave_options, index=0)
        leave_index = leave_options.index(leave)

        work_interfere_options = ["Don't know", 'Never', 'Often', 'Rarely', 'Sometimes']
        work_interfere = st.radio('8.If you have a mental health condition, do you feel that it interferes with your work?', work_interfere_options, index=0)
        work_interfere_index = work_interfere_options.index(work_interfere)


        # v2 = st.selectbox('Select Gender', ['Male', 'Female', 'Transgender/Non Binary'], key=1)
        # v3 = st.selectbox('What country do you live in?', ['Australia', 'Austria', 'Belgium', 'Bosnia and Herzegovina', 'Brazil', 'Bulgaria', 'Canada', 'China', 'Colombia', 'Costa Rica', 'Croatia', 'Czech Republic', 'Denmark', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Latvia', 'Mexic o', 'Moldova', 'Netherlands', 'New Zealand', 'Nigeria', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Romania', 'Russia', 'Singapore', 'Slovenia', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'United Kingdom', 'United States', 'Uruguay', 'Zimbabwe'], key=2)
        # v4 = st.selectbox('Are you self employed?', ['No','Yes'], key=3)
        # v5 = st.selectbox('Do you have a family history of mental illness?', ['No', 'Yes'], key=4)
        # v6 = st.selectbox('If you have a mental health condition, do you feel that it interferes with your work?', ['No', 'Yes'], key=5)
        # v7 = st.selectbox('How many employees does your company or organization have?', ['1-5','100-500', '26-100', '500-1000', '6-25', 'More than 1000'], key=6)
        # v8 = st.selectbox('Do you work remotely (outside of an office) at least half of the time?', ['No', 'Yes'], key=7)
        # v9 = st.selectbox('Is your employer primarily a tech company/organization?', ['No', 'Yes'], key=8)
        # v10 = st.selectbox('Does your employer provide mental health benefits?', ['Do not know', 'No', 'Yes'], key=9)
        # v11 = st.selectbox('Do you know the options for mental health care your employer provides?', ['No', 'Not sure', 'Yes'], key=10)
        # v12 = st.selectbox('Has your employer ever discussed mental health as part of an employee wellness program?', ['Do not know', 'No', 'Yes'], key=11)
        # v13 = st.selectbox('Does your employer provide resources to learn more about mental health issues and how to seek help?', ['Do not know', 'No', 'Yes'], key=12)
        # v14 = st.selectbox('Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?', ['Do not know', 'No', 'Yes'], key=13)
        # v15 = st.selectbox('How easy is it for you to take medical leave for a mental health condition?', ['Do not know', 'Somewhat Difficult','Somewhat Easy', 'Very difficult', 'Very easy'], key=14)
        # v16 = st.selectbox('Do you think that discussing a mental health issue with your employer would have negative consequences?', ['No', 'Some of Them', 'Yes'], key=15)
        # v17 = st.selectbox('Do you think that discussing a physical health issue with your employer would have negative consequences?', ['No', 'Some of Them', 'Yes'], key=16)
        # v18 = st.selectbox('Would you be willing to discuss a mental health issue with your coworkers?', ['No', 'Some of Them', 'Yes'], key=17)
        # v19 = st.selectbox('Would you be willing to discuss a mental health issue with your direct supervisor(s)?', ['No', 'Some of Them', 'Yes'], key=18)
        # v20 = st.selectbox('Would you bring up a mental health issue with a potential employer in an interview?', ['Maybe', 'No', 'Yes'], key=19)
        # v21 = st.selectbox('Would you bring up a physical health issue with a potential employer in an interview?', ['Maybe', 'No', 'Yes'], key=20)
        # v22 = st.selectbox('Do you feel that your employer takes mental health as seriously as physical health?', ['Do not know', 'No', 'Yes'], key=21)
        # v23 = st.selectbox('Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?', ['No', 'Yes'], key=22)
        submitted = st.form_submit_button('Submit')

        if submitted:
            X_temp = {
                'Age': [age],
                "Gender": [gender],
                "family_history": [family_history],
                "benefits": [benefits],
                "care_options": [care],
                "anonymity": [anonymity],
                "leave": [leave],
                "work_interfere": [work_interfere]
            }

            X_test = {
                'Age': [(age - 18)/(72 - 18)],
                "Gender": [gender_index],
                "family_history": [family_history_index],
                "benefits": [benefits_index],
                "care_options": [care_options_index],
                "anonymity": [anonymity_index],
                "leave": [leave_index],
                "work_interfere": [work_interfere_index]
            }

            X_temp = pd.DataFrame(X_temp)
            X_test = pd.DataFrame(X_test)
            Ypredict = pickle_model.predict_proba(X_test)

            st.divider()
            st.subheader("Mental Health Risk Assessment")
            st.write("The data collected from the above survey form:")
            st.write(X_temp)
            st.write("The probability that one should be treated of mental health:")
            st.write(round(Ypredict[0][1], 2))


st.divider()
st.write("**_Thanks for the training data from Kaggle.com._**")

            
# X_test=[[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23]]
# st.write(X_test)

# with col2:
#     with st.form('Form2'):
#         submitted4 = st.slider(label='How would you rate this survey?', min_value=0, max_value=100, key=100)
#         submitted5 = st.form_submit_button('Submit')
