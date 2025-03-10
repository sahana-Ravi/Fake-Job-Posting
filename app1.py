import streamlit as st
import pandas as pd


def app():
    st.markdown("<h1 style='text-align: center; color: #f6c453';>Fake Job Postings</h1>",
                unsafe_allow_html=True)
    st.write("""## Fake Job Postings Dataset""")
    Reviews = pd.read_csv(
        r'C:\Users\a459367\Desktop\fake job detection\Fake-Job-Postings-Detection\fake_job_postings_cleaned (2).csv')
    Reviews = Reviews.drop(columns=['Unnamed: 0'])
    st.dataframe(Reviews)
    st.write('#### job_id :')
    st.write('Identification number given to each job posting')
    st.write('#### title :')
    st.write('A name that describes the position or job')
    st.write('#### location:')
    st.write('           Information about where the job is located')
    st.write('#### department : ')
    st.write('        Information about the department this job is offered by')
    st.write('#### salary_range:')
    st.write('       Expected salary range')
    st.write('#### company_profile:')
    st.write('    Information about the company')
    st.write('#### description:  ')
    st.write('      A brief description about the position offered')
    st.write('#### requirements:')
    st.write('       Pre-requisites to qualify for the job')
    st.write('#### telecommuting:')
    st.write('      Is work from home or remote work allowed')
    st.write('#### has_company_logo:')
    st.write('   Does the job posting have a company logo')
    st.write('#### has_questions:  ')
    st.write('    Does the job posting have any questions')
    st.write('#### employment_type:')
    st.write('    5 categories – Full-time, part-time, contract, temporary and other')
    st.write('#### required_experience:')
    st.write('Can be – Bachelor’s degree, high school degree, unspecified, associate degree, master’s degree, certification, some college coursework, professional, some high school coursework, vocational')
    st.write('#### Industry:')
    st.write('           The industry the job posting is relevant to')
    st.write('#### Function: ')
    st.write('          The umbrella term to determining a job’s functionality')
    st.write('#### Fraudulent:')
    st.write('      The target variable 0: Real, 1: Fake')
