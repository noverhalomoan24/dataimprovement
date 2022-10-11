import pandas as pd
import csv,io,json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
import os
from pathlib import Path
from . import plotting_data as pld
from ..models import temp_json


BASE_DIR = Path(__file__).resolve().parent.parent




def get_jsondata(name_files):
    check_data = temp_json.objects.filter(name_file=name_files).exists()
    return_json = ''
    if(check_data):
        dta_te = temp_json.objects.get(name_file=name_files)
        return_json = dta_te.the_json
    return return_json

def save_jsondata(name_files,json_data):
    check_data = temp_json.objects.filter(name_file=name_files).exists()
    data_tempss = temp_json.objects
    if(check_data):
        dta_te = data_tempss.get(name_file=name_files) #this is for change data
        dta_te.name_file = name_files
        dta_te.the_json = json_data
        dta_te.save()
    else:
        dta_te = data_tempss.create(name_file=name_files,the_json=json_data)
        dta_te.save()

    # mymembers = temp_json.objects.all().values() #way to get all data from table in object
    # temp_jsons.objects.create(name_file=name_files,the_json=json_data)

def get_urlrequest(request):
    url_request= ''
    if request.__contains__('nfldata'):
        url_request = 'nfldata'
    elif request.__contains__('salery'):
        url_request = 'salery'
    elif request.__contains__('dua'):
        url_request = 'dua'
    elif request.__contains__('last'):
        url_request = 'last'
    return url_request


def get_scatter(dtframes):
    df = dtframes
    df['YearsExperience'] = df['YearsExperience'].apply(pd.to_numeric)
    df['Salary'] = df['Salary'].apply(pd.to_numeric)
    df = df.apply(pd.to_numeric)
    fig = px.scatter(df, x="YearsExperience", y="Salary", color="Salary",
                     title="Scatter of Salary on Experience")
    """
    data = go.Scatter(x=df['YearsExperience'],
                      y=df['Salary'],
                      textposition='top right',
                      textfont=dict(color='#E58606'),
                      mode='markers',
                      marker=dict(color='#5D69B1', size=8),
                      name='citations')
    fig = go.Figure(data)
    """
    Path_img = os.path.join(BASE_DIR,"static\image")
    if not os.path.exists(Path_img):
        print("Tidak Ada")

    """
    fig.update_layout(title_text="Scatter Plot Data Salary of Experience",
                      xaxis_title="Year Experience",yaxis_title="Salary",
                      title_x=0.5)
    """
    fig.write_image(Path_img+"/fig1.svg")

def drop_header(df,header_name):
    df_ = df
    df_.drop(df_.loc[df_[header_name] == header_name, :].index, inplace=True)
    return df_

# get_scatter(_example)
def try_convert(dataFrames,columns):
    dff = dataFrames
    for i in columns:
        try:
            dff[i]=dff[i].apply(pd.to_numeric)
        except:
            try:
                dff[i]=dff[i].apply(pd.to_datetime())
            except:
                print("Kagak Bisa")
    return dff


def descrive_data(datas,columns):
    df = pd.DataFrame(datas).convert_dtypes()
    df = try_convert(df,columns)
    header_des = ['count', 'mean', 'std', 'min', 'seperempat', 'setengah', 'sepertujuh', 'max']
    df_des_col = ['header'] + list(df.describe().columns)
    df_des = df.describe()

    return df_des.to_json(),list(df_des.columns)


def get_data(datas):
    df = drop_header(pd.DataFrame(datas),'YearsExperience')
    df['YearsExperience'] = df['YearsExperience'].apply(pd.to_numeric)
    df['Salary'] = df['Salary'].apply(pd.to_numeric)
    # get_scatter(df)
    pld.view_colleration(df,'YearsExperience','Salary','Salary_of_Experience')
    df = df.apply(pd.to_numeric)
    describe_data = df.describe()
    return_data = []
    header_des = ['count', 'mean', 'std', 'min', 'seperempat', 'setengah', 'sepertujuh', 'max']
    columns_name = ['header'] + describe_data.columns.to_list()
    json_string = dict(zip(columns_name,columns_name))
    return_data.append(json_string)
    for x in range(0,len(header_des)):
        x_head =  header_des[x]
        if x_head == 'seperempat':
            x_head = '25%'
        if x_head == 'setengah':
            x_head = '50%'
        if x_head == 'sepertujuh':
            x_head = '75%'
        list_dt = [x_head,round(describe_data[columns_name[1]].to_list()[x],4),round(describe_data[columns_name[2]].to_list()[x],4)]
        json_string = dict(zip(columns_name,list_dt))
        return_data.append(json_string)

    return return_data



def convert_to_json(datas,name_filess,delimeted,header):
    data_header = [x.strip() for x in header.split(delimeted)]
    json_string = ''
    all_data = []
    i=0
    for columns in csv.reader(datas, delimiter=delimeted, quotechar='|'):
        columns = [x.strip() if x !='null' and x!='' else 0 for x in columns]
        if (len(columns) == len(data_header)):
            json_string = dict(zip(data_header, columns))
            i=1
            all_data.append(json_string)

    students = json.loads(json.dumps(all_data))
    save_jsondata(name_filess,students)
    return  students


def return_pandas(datas,header):
    df = drop_header(pd.DataFrame(datas), header)
    return df