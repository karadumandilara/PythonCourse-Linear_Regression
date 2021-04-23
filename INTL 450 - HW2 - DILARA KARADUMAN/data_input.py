

import pandas as pd
import numpy as np
import math
import lr_function
from bs4 import BeautifulSoup
import requests as r

# ### Data Input
wiki_page_request = r.get(
    "https://www.heritage.org/index/explore?view=by-variables&u=637545768379084285")
wiki_page_text = wiki_page_request.text

# ### read data using pandas
def loadD_pandas():

    
    df_list = pd.read_html(wiki_page_text)
    df = df_list[0]
    save_to_csv(df, "originalData")
    return df

# ### Read data using BeautifullSoup
def loadD_soup():
    soup = BeautifulSoup(wiki_page_text, 'html.parser')
    table_soup = soup.find_all('table')
    filtered_table_soup = [table for table in table_soup]

    required_table = table = filtered_table_soup[0]

    data_rows = required_table.find_all('tr')
    rows = []
    for row in data_rows:
        value = row.find_all('td')
        beautified_value = [ele.text.strip() for ele in value]
        # Remove data arrays that are empty
        if len(beautified_value) == 0:
            continue
        rows.append(beautified_value)

    #create a pandas dataframe from rows
    df = pd.DataFrame(rows, columns=["name",
                                    "Overall Score",
                                    "Tariff Rate",
                                    "Income Tax Rate",
                                    "Corporate Tax Rate",
                                    "Population (millions)",
                                    "GDP (billions)",
                                    "GDP per Capita",
                                    "Unemployment Rate",
                                    "Inflation Rate",
                                    "FDI Inflow (millions)",
                                    "Tax Burden % GDP",
                                    "Govt. Expenditure % GDP"])


    df = df.apply(pd.to_numeric, errors='coerce')
    #df.corr(method='pearson')

    save_to_csv(df,"originalData")
    return df


def save_to_csv(df,name):
    df.to_csv(f'{name}.csv',
              index=False, header=True)



def normalizeD(df):
    columns = df.columns
    for column in columns:
        df[column] = (df[column] - df[column].min()) / \
            (df[column].max() - df[column].min())
    return df


def getData():

    #df=loadD_pandas()
    df=loadD_soup()
    #df=normalize(df)

    dataXY = df[["GDP (billions)", "Population (millions)"]]
    df = df.drop(['name'], axis=1)
    
    #here you could fill the missing values with something like mean, dropping those rows is much easier
    dataXY = dataXY.dropna()
    
    # X=dataXY["Population (millions)"].to_numpy()
    # Y=dataXY["GDP (billions)"].to_numpy()
    XY = dataXY.to_numpy()
    X, Y = XY.T

    return X,Y

