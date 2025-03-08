#Question 2

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data

df = pd.read_csv("university_student_dashboard_data.csv")

# Sidebar filters

years = sorted(df['Year'].unique())
selected_year = st.sidebar.selectbox("Select Year", years)

# Filtered data
year_data = df[df['Year'] == selected_year]

# Dashboard Title
st.title("University Admissions & Student Satisfaction Dashboard")

# KPI Metrics

applications = year_data["Applications"].sum()
admissions = year_data["Admitted"].sum()
enrollments = year_data["Enrolled"].sum()
retention = year_data["Retention Rate (%)"].mean()
satisfaction = year_data["Student Satisfaction (%)"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Applications", applications)
col2.metric("Total Admissions", admissions)
col3.metric("Total Enrollments", enrollments)
col4, col5 = st.columns(2)
col4.metric("Retention Rate (%)", round(retention, 2))
col5.metric("Student Satisfaction (%)", round(satisfaction, 2))

# Enrollment Breakdown by Department

dept_enrollments = year_data[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum()
st.bar_chart(dept_enrollments)

# Spring vs. Fall Enrollment

tenure_data = year_data.groupby("Term")["Enrolled"].sum()
st.bar_chart(tenure_data)

# Retention & Satisfaction Over Time

yearly_trends = df.groupby("Year")[["Retention Rate (%)", "Student Satisfaction (%)"]].mean()
st.line_chart(yearly_trends)

# Set style

sns.set_theme(style="whitegrid")

# Aggregating data for analysis

yearly_data = df.groupby("Year").sum()
spring_data = df[df["Term"] == "Spring"].groupby("Year").sum()
fall_data = df[df["Term"] == "Fall"].groupby("Year").sum()

# Plot Applications, Admissions, and Enrollments over time

plt.figure(figsize=(12, 5))
plt.plot(yearly_data.index, yearly_data["Applications"], marker="o", label="Applications")
plt.plot(yearly_data.index, yearly_data["Admitted"], marker="o", label="Admitted")
plt.plot(yearly_data.index, yearly_data["Enrolled"], marker="o", label="Enrolled")
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Applications, Admissions, and Enrollments Over Time")
plt.legend()
plt.show()

# Plot Retention Rate and Satisfaction over time

fig, ax1 = plt.subplots(figsize=(12, 5))
ax1.set_xlabel("Year")
ax1.set_ylabel("Retention Rate (%)", color="tab:blue")
ax1.plot(yearly_data.index, yearly_data["Retention Rate (%)"], marker="o", color="tab:blue", label="Retention Rate")
ax1.tick_params(axis="y", labelcolor="tab:blue")
ax2 = ax1.twinx()
ax2.set_ylabel("Satisfaction (%)", color="tab:red")
ax2.plot(yearly_data.index, yearly_data["Student Satisfaction (%)"], marker="o", color="tab:red", linestyle="dashed", label="Satisfaction")
ax2.tick_params(axis="y", labelcolor="tab:red")
plt.title("Retention Rate and Student Satisfaction Over Time")
fig.tight_layout()
plt.show()

