import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# def return_fig(fig_sizee,x,y):
#     fig,ax = plt.subplots(x,y,figsize=(fig_sizee[0],fig_sizee[1]))
#     return fig,ax

def view_colleration(data,x_label,y_label,title):
    fig,ax = plt.subplots(1,1,figsize=(12,8))
    ax.plot(data[x_label],data[y_label])
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    # plt.savefig("my_graph.svg")
    Path_img = os.path.join(BASE_DIR, "static\image")
    name_file = "/"+title+".svg"
    plt.savefig(Path_img +name_file)


def barplot_plotting(dff,x_axiss,y_axiss,x_label,y_label,title_dt,base_dirrr):
    df = dff
    plt.clf()
    Path_img = os.path.join(base_dirrr, "static\services\img")
    if os.path.exists(Path_img+"/"+title_dt+".jpg") == False:
        plt.figure(figsize=(12,8))
        df[y_axiss] = df[y_axiss].apply(pd.to_numeric)
        df[x_axiss] = df[x_axiss].apply(pd.to_numeric)
        ax = sns.barplot(data=df,x=x_axiss,y=y_axiss,ci=None,palette="flare")
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x,loc:"{:,}".format(int(x))))
        ax.set(xlabel=x_label,ylabel=y_label,title=title_dt)
        name_file = "/" + title_dt + ".jpg"
        plt.savefig(Path_img + name_file)

def box_ploting_one(dff,x_axiss,title_dt,base_dirrr):
    df = dff
    Path_img = os.path.join(base_dirrr, "static\services\img")
    if os.path.exists(Path_img + "/" + title_dt + ".jpg") == False:
        plt.clf()
        plt.figure(figsize=(12, 8))
        # df['YearsExperience'] = df['YearsExperience'].apply(pd.to_numeric)
        df[x_axiss] = df[x_axiss].apply(pd.to_numeric)
        print(df)
        ax = sns.boxplot(y=df[x_axiss])
        ax.set(title=title_dt)
        name_file = "/" + title_dt + ".jpg"
        plt.savefig(Path_img + name_file)
    pass


def plotting_coleration(dff,title_dt,name_data,x_axiss,y_axiss,base_dirss):
    path_img = os.path.join(base_dirss,"static\services\img")
    if(os.path.exists(path_img + "/" + name_data + ".jpg") == False):
        plt.clf()
        plt.figure(figsize=(12,6))
        df = dff
        df[y_axiss] = df[y_axiss].apply(pd.to_numeric)
        df[x_axiss] = df[x_axiss].apply(pd.to_numeric)
        sns.set_theme(context="notebook", style="whitegrid", palette="deep")
        ax = sns.heatmap(df.corr())
        plt.title(title_dt)
        name_file = "/" + name_data + ".jpg"
        plt.savefig(path_img+name_file)