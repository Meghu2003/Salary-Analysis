import streamlit as st
st.set_page_config(layout='wide',page_title='Salary Analysis')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

ds_salaries=pd.read_csv('ds_salaries.csv')
del ds_salaries['Unnamed: 0']
cols1=ds_salaries['job_title'].unique()
cols2=['work_year','experience_level','employment_type','salary_currency','employee_residence','company_location','company_size']
tab1,tab2=st.tabs(['Visualisation','Analysis'])
with tab1:
  col1,col2,col3=st.columns(3)
  with col1:
    st.title('Welcome to Visualisation🙂')
    st.header("Let's see the graphs and get clarity😉.(Please fill the required information)")
    sel=st.multiselect('Select the Job you want to know about',cols1)
  for i in sel:
    with col2:
      fig1=plt.figure()
      ax1=fig1.add_subplot()
      sns.barplot(x='employment_type',y='salary',hue='experience_level',data=ds_salaries[ds_salaries['job_title']==i],errorbar=None,ax=ax1)
      ax1.legend(loc='upper right',labels=['Entry','Middle','Senior','Expert'])
      fig1.suptitle(i)
      st.pyplot(fig1)
    with col3:
      fig2=plt.figure()
      ax2=fig2.add_subplot()
      ax2.plot(ds_salaries[ds_salaries['job_title']==i]['work_year'].value_counts().sort_index(),marker='+')
      ax2.set_xticks([2020,2021,2022])
      ax2.set_xlabel('Working Years')
      fig2.suptitle(i)
      st.pyplot(fig2)
with tab2:
  col1,col2=st.columns(2)
  with col1:
    st.title('Welcome to Analysis🙂')
    st.header("Let's see the content and get clarity about the particular job😉.(Please fill the required information)")
    sel=st.selectbox('Select the Job you want to know about',cols1)
    col=st.select_slider('Select the Attribute',cols2)
  with col2:
    val=ds_salaries[ds_salaries['job_title']==sel][col].value_counts()
    for j in val.index:
      st.write(j,val[j])
