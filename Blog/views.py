from django.shortcuts import render,HttpResponse
from django.views import View
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def index(request):
    context = {
        'title':'About',
        'Heading':'Profesional Jurnal',
    }
    return render(request,'blog/index_b.html',context={'context':context})

def render_templates(template_src,context_dic={}):
    template = get_template(template_src)
    html = template.render()
    results = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),results)
    if not pdf.err:
        return HttpResponse(results.getvalue(),content_type='application/pdf')
    return None



class DownloadPDF(View):
    def get(self,request,*args,**kwargs):
        pdf = render_templates('Blog/index_b.html')
        response = HttpResponse(pdf,content_type='application/pdf')
        filename = "Blog_.pdf"
        content = "attachment; filename='%s'"%(filename)
        response['Content-Disposition'] = content
        return response