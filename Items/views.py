from django.shortcuts import render
from Layanan import models
from pathlib import Path
from Layanan import Proses_data



BASE_DIRR = Path(__file__).resolve().parent

# Create your views here.
def index(request):
    context = {
        'title':'Story',
        'Heading':'Profesional Jurnal',
    }
    return render(request,'services/index_i.html',context={'context':context})


def view_salery(request):
    temp_json = Proses_data.show_datas.get_jsondata('Salary_Data')
    des_json = Proses_data.show_datas.get_data(temp_json)
    Proses_data.plotting_data.barplot_plotting(Proses_data.show_datas.return_pandas(temp_json,'YearsExperience'),"YearsExperience","Salary","YearsExperience","Salary","Salary_Base_Experiences",BASE_DIRR)
    Proses_data.plotting_data.box_ploting_one(Proses_data.show_datas.return_pandas(temp_json, 'YearsExperience'),'Salary','Boxplot_Salary', BASE_DIRR)
    Proses_data.plotting_data.box_ploting_one(Proses_data.show_datas.return_pandas(temp_json, 'YearsExperience'),
                                              'YearsExperience', 'Boxplot_YearsExperience', BASE_DIRR)
    Proses_data.plotting_data.plotting_coleration(Proses_data.show_datas.return_pandas(temp_json, 'YearsExperience'),"Heatmap Colleration of Data Salary on Experience","heatmap_salary",
                                              "YearsExperience","Salary", BASE_DIRR)
    for i in range(len(temp_json)-1):
        if i >4:
            temp_json.pop()
    # print(temp_json)
    # return redirect(request)
    return render(request,'services/salery_statitic.html',context={'salary':temp_json,'desc_salary':des_json})