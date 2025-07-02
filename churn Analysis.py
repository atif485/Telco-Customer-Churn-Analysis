#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd


# In[31]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[32]:


df=pd.read_csv("Telco_Customer_Churn (1).csv")


# In[33]:


df


# In[34]:


df.head()


# In[35]:


df.tail()


# In[36]:


df.info()


# In[37]:


df["TotalCharges"]=df["TotalCharges"].replace(" ",0)
df["TotalCharges"]=df["TotalCharges"].astype("float")


# In[38]:


df.info()


# In[39]:


df.isnull().sum().sum()


# In[40]:


df.describe()


# In[41]:


df["customerID"].duplicated().sum()


# In[44]:


def conv(value):
    if value == 0:
        return "No"
    else:
        return "Yes"
    
    
        
    



df["SeniorCitizen"]=df["SeniorCitizen"].apply(conv)


# In[46]:


df.head()


# # Analysis

# In[60]:


ax= sns.countplot(x="Churn" ,data=df)
ax.bar_label(ax.containers[0])
plt.title("Count of the churn")
plt.show()


# In[52]:


gb=df.groupby("Churn").agg({"Churn":"count"})
gb


# In[59]:


gb=df.groupby("Churn").agg({"Churn":"count"})
plt.pie(gb['Churn'], labels=gb.index , autopct = "%1.2f%%")
plt.title("Percentage of churned")
plt.show


# In[65]:


plt.figure(figsize=(4,4))
sns.countplot(x="gender" ,data=df , hue="Churn")
plt.title("Churn by Gender")
plt.show()


# In[66]:


plt.figure(figsize=(4,4))
sns.countplot(x="SeniorCitizen" ,data=df , hue="Churn")
plt.title("Churn by SeniorCitizen ")
plt.show()


# In[67]:


count_data = pd.crosstab(df['SeniorCitizen'], df['Churn'])

# Step 2: Convert counts to percentages
percentage_data = count_data.div(count_data.sum(axis=1), axis=0) * 100

# Step 3: Plot stacked bar chart
ax = percentage_data.plot(kind='bar', stacked=True, figsize=(6, 4), colormap='Set2')

# Step 4: Add percentage labels
for i, (index, row) in enumerate(percentage_data.iterrows()):
    cum_sum = 0
    for churn_status in percentage_data.columns:
        pct = row[churn_status]
        if pct > 0:
            ax.text(i, cum_sum + pct / 2, f"{pct:.1f}%", ha='center', va='center', fontsize=9, color='black')
        cum_sum += pct

# Customizations
plt.title("Churn by SeniorCitizen (Stacked %)")
plt.ylabel("Percentage (%)")
plt.xlabel("Senior Citizen")
plt.legend(title="Churn")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# comparitive a greater percentage of people in senior citizen category

# In[72]:


plt.figure(figsize=(8,4))
sns.histplot(x="tenure" ,data=df , hue="Churn",bins=70)
plt.title("Churn by tenure ")
plt.show()


# people who have used our sevices for long time stayed andpeople who have used our sevices for one or two months have churnes

# In[74]:


ax= sns.countplot(x="Contract" ,data=df ,hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of the Contract")
plt.show()


# #people who have month to month contract have likely churned then people who have 1 year and two year contract 

# In[78]:


df.columns.values


# In[84]:


cols = ['PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies']

# Setup subplot grid: 3 rows x 3 columns
n_cols = 3
n_rows = (len(cols) + n_cols - 1) // n_cols  # auto calculate rows

# Create figure and axes
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 12))
axes = axes.flatten()

# Plot each column
for i, col in enumerate(cols):
    sns.countplot(x=col, data=df, ax=axes[i], palette="Set2",hue="Churn")
    axes[i].set_title(f"{col} Count", fontsize=10)
    axes[i].set_xlabel("")
    axes[i].set_ylabel("Count")
    axes[i].tick_params(axis='x', rotation=45)

# Hide any unused subplots
for j in range(i+1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


#  PhoneService, InternetService, and related services like OnlineSecurity, TechSupport, and StreamingTV are less likely to churn compared to those without these services. Features labeled as "No internet service" consistently show low churn, possibly because these customers are less engaged. Conversely, churn appears higher among customers with active internet-based services but without added protections (like OnlineBackup or DeviceProtection), suggesting service add-ons may influence customer retention.

# In[86]:


ax= sns.countplot(x="PaymentMethod" ,data=df ,hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of the PaymentMethod")
plt.xticks(rotation=45)
plt.show()


# customer is likely to churn when customer using electronic check for payment method

# In[ ]:




