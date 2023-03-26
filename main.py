import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# set page title
st.set_page_config(page_title="Employee Satisfaction Dashboard")

# create sidebar with file upload widget
st.sidebar.title("Upload CSV file")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# if file is uploaded, load data and display charts and summary statistics
if uploaded_file is not None:
    # load the employee satisfaction data from the uploaded file
    satisfaction_data = pd.read_csv(uploaded_file)

    # calculate the average satisfaction score for each department
    department_scores = satisfaction_data.groupby('Department')['EmpSatisfaction'].mean()

    # plot a bar chart of the average satisfaction scores for each department
    st.write("## Average Employee Satisfaction by Department")
    fig, ax = plt.subplots()
    ax.bar(department_scores.index, department_scores.values)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # calculate the overall average satisfaction score for all employees
    overall_average = satisfaction_data['EmpSatisfaction'].mean()
    st.write(f"Overall Average Satisfaction Score: {overall_average:.2f}")

    # categorize employees as satisfied or dissatisfied based on their satisfaction score
    satisfied_employees = satisfaction_data[satisfaction_data['EmpSatisfaction'] >= 3.0]
    dissatisfied_employees = satisfaction_data[satisfaction_data['EmpSatisfaction'] < 3.0]

    # calculate the percentage of employees who are satisfied
    satisfaction_percentage = len(satisfied_employees) / len(satisfaction_data) * 100
    st.write(f"Satisfied Employees: {satisfaction_percentage:.2f}%")

    # calculate the average satisfaction score for satisfied and dissatisfied employees
    satisfied_average = satisfied_employees['EmpSatisfaction'].mean()
    dissatisfied_average = dissatisfied_employees['EmpSatisfaction'].mean()
    st.write(f"Average Satisfaction Score for Satisfied Employees: {satisfied_average:.2f}")
    st.write(f"Average Satisfaction Score for Dissatisfied Employees: {dissatisfied_average:.2f}")