import streamlit as st
import pickle
import pandas as pd
from PIL import Image
from datetime import datetime

image = Image.open('Mental Health.png')
st.image(image, caption='', width=150)

pkl_filename = "pickle_model.pkl"
st.header("AI-Driven Mental Health Risk Assmt. Webapp")
st.write("Please answer the questions to the best of your ability.")
col1, col2 = st.columns(2)

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

# with col1:
    with st.form('Form1'):
        Time = datetime.now()

        age = st.slider(label='1.What is your age?', min_value=18, max_value=72)

        gender_options = ['Female', 'Male', 'Transgender/Non Binary']
        gender = st.radio("2.To which gender identity do you most identify?", gender_options, index=0)
        gender_index = gender_options.index(gender)

        country_options = [
            'Australia', 'Austria', 'Belgium', 'Bosnia and Herzegovina', 'Brazil', 'Bulgaria',
            'Canada', 'China', 'Colombia', 'Costa Rica', 'Croatia', 'Czech Republic', 'Denmark',
            'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland',
            'Israel', 'Italy', 'Japan', 'Latvia', 'Mexico', 'Moldova', 'Netherlands', 'New Zealand',
            'Nigeria', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Romania', 'Russia',
            'Singapore', 'Slovenia', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Thailand',
            'United Kingdom', 'United States', 'Uruguay', 'Zimbabwe'
        ]
        country = st.selectbox('3.What country do you live in?', country_options, index=country_options.index('United States'))
        country_index = country_options.index(country)

        employment_options = ['No', 'Yes']
        employment = st.radio('4.Are you self employed?', employment_options, index=0)
        employment_index = employment_options.index(employment)

        family_history_options = ['No', 'Yes']
        family_history = st.radio('5.Do you have a family history of mental illness?', family_history_options, index=0)
        family_history_index = family_history_options.index(family_history)

        work_interfere_options = ["Don't know", 'Never', 'Often', 'Rarely', 'Sometimes']
        work_interfere = st.radio(
            '6.If you have a mental health condition, do you feel that it interferes with your work?',
            work_interfere_options, index=0)
        work_interfere_index = work_interfere_options.index(work_interfere)

        employees_options = ['1-5', '100-500', '26-100', '500-1000', '6-25', 'More than 1000']
        employees = st.radio('7.How many employees does your company or organization have?', employees_options,
                             index=0)
        employees_index = employees_options.index(employees)

        remote_options = ['No', 'Yes']
        remote = st.radio('8.Do you work remotely (outside of an office) at least half of the time?', remote_options,
                          index=0)
        remote_index = remote_options.index(remote)

        tech_company_options = ['No', 'Yes']
        tech_company = st.radio('9.Is your employer primarily a tech company/organization?', tech_company_options,
                                index=0)
        tech_company_index = tech_company_options.index(tech_company)

        benefits_options = ['Do not know', 'No', 'Yes']
        benefits = st.radio('10.Does your employer provide mental health benefits?', benefits_options, index=0)
        benefits_index = benefits_options.index(benefits)

        care_options = ['No', 'Not sure', 'Yes']
        care = st.radio('11.Do you know the options for mental health care your employer provides?', care_options, index=1)
        care_options_index = care_options.index(care)

        wellness_program_options = ['Do not know', 'No', 'Yes']
        wellness_program = st.radio(
            '12.Has your employer ever discussed mental health as part of an employee wellness program?',
            wellness_program_options, index=0)
        wellness_program_index = wellness_program_options.index(wellness_program)

        resources_mh_issues_options = ['Do not know', 'No', 'Yes']
        resources_mh_issues = st.radio(
            '13.Does your employer provide resources to learn more about mental health issues and how to seek help?',
            resources_mh_issues_options, index=0)
        resources_mh_issues_index = resources_mh_issues_options.index(resources_mh_issues)

        anonymity_options = ['Do not know', 'No', 'Yes']
        anonymity = st.radio(
            '14.Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?',
            anonymity_options, index=0)
        anonymity_index = anonymity_options.index(anonymity)

        leave_options = ['Do not know', 'Somewhat Difficult', 'Somewhat Easy', 'Very difficult', 'Very easy']
        leave = st.radio('15.How easy is it for you to take medical leave for a mental health condition?', leave_options,
                         index=0)
        leave_index = leave_options.index(leave)

        neg_conseq_mh_options = ['Maybe', 'No', 'Yes']
        neg_conseq_mh = st.radio(
            '16.Do you think that discussing a mental health issue with your employer would have negative consequences?',
            neg_conseq_mh_options, index=1)
        neg_conseq_mh_index = neg_conseq_mh_options.index(neg_conseq_mh)

        neg_conseq_ph_options = ['Maybe', 'No', 'Yes']
        neg_conseq_ph = st.radio(
            '17.Do you think that discussing a physical health issue with your employer would have negative consequences?',
            neg_conseq_ph_options, index=1)
        neg_conseq_ph_index = neg_conseq_ph_options.index(neg_conseq_ph)

        discuss_coworkers_options = ['No', 'Some of them', 'Yes']
        discuss_coworkers = st.radio('18.Would you be willing to discuss a mental health issue with your coworkers?',
                                     discuss_coworkers_options, index=0)
        discuss_coworkers_index = discuss_coworkers_options.index(discuss_coworkers)

        discuss_supervisors_options = ['No', 'Some of Them', 'Yes']
        discuss_supervisors = st.radio(
            '19.Would you be willing to discuss a mental health issue with your direct supervisor(s)?',
            discuss_supervisors_options, index=0)
        discuss_supervisors_index = discuss_supervisors_options.index(discuss_supervisors)

        discuss_potential_mh_options = ['Maybe', 'No', 'Yes']
        discuss_potential_mh = st.radio(
            '20.Would you bring up a mental health issue with a potential employer in an interview?',
            discuss_potential_mh_options, index=0)
        discuss_potential_mh_index = discuss_potential_mh_options.index(discuss_potential_mh)

        discuss_potential_ph_options = ['Maybe', 'No', 'Yes']
        discuss_potential_ph = st.radio(
            '21.Would you bring up a physical health issue with a potential employer in an interview?',
            discuss_potential_ph_options, index=0)
        discuss_potential_ph_index = discuss_potential_ph_options.index(discuss_potential_ph)

        takes_mh_seriously_options = ['Do not know', 'No', 'Yes']
        takes_mh_seriously = st.radio(
            '22.Do you feel that your employer takes mental health as seriously as physical health?',
            takes_mh_seriously_options, index=0)
        takes_mh_seriously_index = takes_mh_seriously_options.index(takes_mh_seriously)

        observed_neg_conseq_options = ['No', 'Yes']
        observed_neg_conseq = st.radio(
            '23.Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?',
            observed_neg_conseq_options, index=0)
        observed_neg_conseq_index = observed_neg_conseq_options.index(observed_neg_conseq)

        comment = st.text_input("24.Any additional notes or comments:")

        submitted = st.form_submit_button('Submit')

        if submitted:
            X_temp = {
                'Time': [Time],
                'Age': [age],
                "Gender": [gender],
                "Country": [country],
                "self_employment": [employment],
                "family_history": [family_history],
                "work_interfere": [work_interfere],
                "no_employees": [employees],
                "remote_work": [remote],
                "tech_company": [tech_company],
                "benefits": [benefits],
                "care_options": [care],
                "wellness_program": [wellness_program],
                "seek_help": [resources_mh_issues],
                "anonymity": [anonymity],
                "leave": [leave],
                "mental_health_consequence": [neg_conseq_mh],
                "physical_health_consequence": [neg_conseq_ph],
                "coworkers": [discuss_coworkers],
                "supervisor": [discuss_supervisors],
                "mental_health_interview": [discuss_potential_mh],
                "physical_health_interview": [discuss_potential_ph],
                "mental_vs_physical": [takes_mh_seriously],
                "obs_consequence": [observed_neg_conseq],
                "comments": [comment]
            }
            X_test = {
                'Age': [(age - 18) / (72 - 18)],
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
            st.write(X_temp.T)
            st.write("The probability that one should be treated of mental health:")
            st.write(round(Ypredict[0][1], 2))
            X_temp.to_csv('mental_health_survey_date.csv', mode='a', index=False, header=False)
            df = pd.read_csv('mental_health_survey_date.csv')
            st.write(df.shape)

st.divider()
st.write("**_This web app was developed by CYD mental health group and thanks for the public dataset from Kaggle.com._**")


