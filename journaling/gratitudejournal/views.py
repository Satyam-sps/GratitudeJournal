from django.shortcuts import render
from django.views import View
# from .models import GratitudeJournal , Attachment , LifeLogJournal
# from .forms import GratitudeForm , gratitudeAttach ,lifelogAttach
from .models import GratitudeJournal
from .forms import GratitudeForm
from django.shortcuts import redirect
from icecream import ic
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from journaling.settings import MEDIA_ROOT


# Create your views here.

path = '/home/satyam/Desktop/Desktop'



class CreateJournal(View):
    def get(self,request):
        form = GratitudeForm()
        # attach_form = gratitudeAttach()
        # cxt = {'create_form':form, 'attach_form':attach_form}
        cxr = {'create_form':form}
        return render(request,'create.html',cxr)

    def post(self,request):
        form = GratitudeForm(request.POST or None , request.FILES or None)
        data1 = request.FILES.getlist('images')
        data = request.FILES['images']
        ic(data.name)
        ic(data.size)
        ic(MEDIA_ROOT)
        img_url =[]
        for x in data1:
            img_url.append((f'{path}/{x}'))
        ic(img_url[0])
        
        cxt = {'form':form , 'img':img_url}
        if form.is_valid():
            form.save()
            return render(request , 'index.html' , cxt)
        else:
            return form.errors.as_json
        # journal_entry =request.POST.get('journal_entry')
        # positive_experience = request.POST.get('positive_experience')
        # rate_your_day = request.POST.get('rate_your_day')
        # images = request.FILES.getlist('image')
        # journal_instance = GratitudeJournal.objects.create(journal_entry=journal_entry,positive_experience=positive_experience,rate_your_day=rate_your_day)
        # print(request.POST)
        # for img in images:
        #     Attachment.objects.create(grat_attach_img=img,gratitude_attach_key=journal_instance)
        
        return redirect('gratitudejournal:index')
     
class Index(View):
    def get(self,request):
        data = GratitudeJournal.objects.all().order_by('-id')
        context = {'data':data}
        return render(request ,'index.html',context)
    


class DeleteJournal(View):
    def get(self,request , pk):
        print(request)
        journal_instance = GratitudeJournal.objects.get(id=pk)
        journal_instance.delete()
        return redirect ('gratitudejournal:index')



class UpdateJournal(View):
    def get(self,request,pk):
        journal_instance = GratitudeJournal.objects.get(id = pk)
        form = GratitudeForm(instance = journal_instance)
        cxt = {'form':form}
        return render(request , 'update.html' , cxt)

    def post(self , request , pk):
        form = GratitudeForm(request.POST, request.FILES)
        print(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gratitudejournal:index')
        else:
            print(form.errors.as_json)



class DetailJournal(View):
    def get(self , request , pk):
        detail_data = GratitudeJournal.objects.get(id = pk)
        # images = Attachment.objects.filter(gratitude_attach_key=pk).values()
        # cxt = {'detail':detail_data, 'img':images}
        cxt = {'detail':detail_data}
        return render(request , 'detail.html', cxt)

        
# class CreateLifeLog(View):
#     def get(self, request):
#         print(dir(request))
#         form = lifelogAttach()
#         cxt = {'form':form , 'txt':'This is form'}
#         return render(request,'life-log-create.html',cxt)

#     def post(self,request):
#         print(request)
#         print(dir(request))
#         entry = request.POST.get('life_log_entry')
#         images = request.FILES.getlist('images')
#         print(entry)
#         print(images)
#         life_log_instance = LifeLogJournal.objects.create(entry=entry)

#         for img in images:
#             Attachment.objects.create(lifelog_attach_image = img, lifelog_attach_key= life_log_instance)
            
#         return redirect('gratitudejournal:index')
