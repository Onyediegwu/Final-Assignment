#!/usr/bin/env python
# coding: utf-8

# In[72]:


get_ipython().system('pip3 install yfinance')
#!pip install pandas
#!pip install requests
get_ipython().system('pip3 install bs4')
get_ipython().system('pip3 install html5lib')
#!pip install plotly


# In[73]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[74]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[75]:


tesla = yf.Ticker('TSLA')


# In[76]:


tesla_data = tesla.history(period="max")


# In[77]:


tesla_data.reset_index(inplace=True)
tesla_data.head()


# In[82]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillNetwork-PY0220EN-SkillNetwork/labs/project/stock.htm"
html_data = requests.get(url).text


# In[83]:


soup = BeautifulSoup(html_data,"lxml")


# In[89]:


tesla_revenue = pd.DataFrame(columns=['Date', 'Revenue'])

for table in soup.find_all('table'):

    if ('Tesla Quarterly Revenue' in table.find('th').text):
        rows = table.find_all('tr')
        
        for row in rows:
            col = row.find_all('td')
            
            if col != []:
                date = col[0].text
                revenue = col[1].text.replace(',','').replace('$','')

                tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)


# In[90]:


tesla_revenue.head()


# In[91]:


tesla_revenue


# In[92]:


tesla_revenue.dropna(inplace=True)
tesla_revenue.tail()


# In[93]:


gamestop = yf.Ticker("GME")


# In[94]:


gme_data=gamestop.history(period="max")


# In[95]:


gme_data.reset_index(inplace=True)
gme_data.head()


# In[109]:


url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillNetwork-PY0220EN-SkillNetwork/labs/project/stock.htm"
html_data=requests.get(url).text


# In[110]:


soup = BeautifulSoup(html_data,"lxml")


# In[ ]:





# In[ ]:


gme_revenue.dropna(inplace=True)
gme_revenue.tail()


# In[ ]:




