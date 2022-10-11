from django.shortcuts import render,redirect
from django.views.generic import View
import io,json
from django.contrib import messages
from .Proses_data import show_datas
from django.http import HttpResponseRedirect
from django.http import JsonResponse,HttpResponse

# Create your views here.

def Mylayanan(request):
    return render(request,'layanan.html')



def upload(request):
    io_string =''
    # data_csv = request.FILES['files_csv']
    # print('ini hasil')
    # print(data_csv)
    any_file = request.POST.get('files_csv',False) #check data apakah kosong
    if request.method == 'POST':
        request_url = request.POST['defaultss']
        if any_file == '' and request_url == '':
            if request_url == '':
                request_url = '/service'
            messages.info(request, 'File not found')
            return redirect(request_url)
        else:
            data_csv = request.FILES['files_csv']
            name_filess = data_csv.name.split(".")[0]
            if data_csv.name.split(".")[1] != 'csv' and data_csv.name.split(".")[1] != 'xls':
                messages.info(request,'Type of file should csv')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) #this for back to refresh this
            return_data = show_datas.get_jsondata(name_filess)
            if request_url == '':
                # if not data_csv.name.endswith('.csv'):
                #     print("Slah")
                delimeted = ","
                data_set = data_csv.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                header = io_string.readline()
                if ";" in header:
                    delimeted = ";"
                name_filess = data_csv.name.split(".")[0]
                return_data = show_datas.convert_to_json(io_string, name_filess,delimeted,header)
            # print(return_data)
            for_upload = []
            for x,y in enumerate(return_data):
                if x==9:
                    break
                for_upload.append(y)
            print(request_url)
            # return redirect('render-json/'+name_filess+'/')
            # return redirect('read-data/')
            return  render(request,'detaillayanan.html',context={'Datas':for_upload,'Regust_url':name_filess})


class postjson_wthoutrequired():
    def __getnewargs__(self):
        pass


class PostJSONListView(View):
    def get(self,*args,**kwargs):
        print(*args)
        name_files = kwargs['name_file']
        data_return = show_datas.get_jsondata(name_files)
        return JsonResponse({'data': data_return}, safe=False)


def check_data(request):
    data_return = show_datas.get_jsondata(request.POST.get('name_filehide'))
    # print(request.POST.get('column_names'))
    list_name = [x.replace("_"," ") for x in request.POST.get('column_names').split(",") if x != '']
    jum_column_select = len(list_name)
    if(len(list_name) == 0):
        list_name = list(data_return[0].keys())
    if request.POST.get('flag_button') == "delete_columns":
        if jum_column_select != 0 :
            for i in range(0,len(data_return)):
                for x in list_name:
                    if x in data_return[i]:
                        data_return[i].pop(x)
        show_datas.save_jsondata(request.POST.get('name_filehide'), data_return)
    if request.POST.get('flag_button') == "describe_data":
        data_return,list_name = show_datas.descrive_data(data_return,list_name)
        data_return = json.loads(data_return)
    return JsonResponse({"data":data_return,"list_columns":list_name})


def delete_columns(name_files):
    data_return = show_datas.get_jsondata(name_files)
    pass



# def return_layanan(request):
#     url_request = show_datas.get_urlrequest(request.path)
#     return  render(request,'detaillayanan.html',context={'Regust_url':url_request})