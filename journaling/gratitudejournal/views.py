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
from journaling.settings import MEDIA_ROOT ,MEDIA_URL
from django.core.files.storage import FileSystemStorage
from .function import img_format , writefile_to_dir

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage



# Create your views here.

path = '/home/satyam/Desktop/Desktop'

def img_name_formatter(img):
    pass


class CreateJournal(View):
    def get(self,request):
        form = GratitudeForm()
        cxr = {'create_form':form}
        return render(request,'create.html',cxr)

    def post(self,request):
        form = GratitudeForm(request.POST or None , request.FILES or None)
        journal_entry =request.POST.get('journal_entry')
        positive_experience = request.POST.get('positive_experience')
        rate_your_day = request.POST.get('rate_your_day')
        images = request.FILES.getlist('image')
        journal_type = request.POST.get('journal_type')
        ic(journal_type)
        username = request.POST.get('username')
        user_id = request.POST.get('user_id')

        #This return formatted Image name
        format_img = img_format(images, journal_type,user_id,username)
        ic(format_img)

        
        # This code created directory of the on the basis of username if it does not exists

        if journal_type == 'gratitude_journal':
            img_dir = os.path.join(MEDIA_ROOT,'gratitude_journal')
            new_usr_path = os.path.join(img_dir,username)
            if not os.path.exists(new_usr_path):
                os.makedirs(new_usr_path)
        else:
            img_dir = os.path.join(MEDIA_ROOT,'lifelog_journal')
            new_usr_path = os.path.join(img_dir,username)
            if not os.path.exists(new_usr_path):
                os.makedirs(new_usr_path)   
            ic(new_usr_path)

        
        ic(MEDIA_ROOT)
        ic(format_img)
        upload_path = f'{MEDIA_ROOT}/{journal_type}/{username}'
        ic(upload_path)

        data = writefile_to_dir(upload_path,images,format_img)
        ic(data)


        # This is stores images in username specific directory
        # for x in format_img:
        #     ic(x)
        #     fs = FileSystemStorage(location=new_usr_path).save(x.name,x)
        #     ic(fs)
        

        """
        Below code on basis of type of journal creates path from mediaurl to journal_type 
        """
        if journal_type == 'gratitude_journal':
            img_dir = os.path.join(MEDIA_URL,'gratitude_journal')
        else:
            img_dir = os.path.join(MEDIA_URL , 'lifelog_journal')

        new_img_path = os.path.join(img_dir,username)
        ic(new_img_path)

        GratitudeJournal.objects.create(journal_entry=journal_entry,positive_experience=positive_experience, user_id = user_id,rate_your_day=rate_your_day,images=new_img_path,journal_type=journal_type,user_name=username)
        print(request.POST)
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
        ic(detail_data)
        ic(request)
        # images = Attachment.objects.filter(gratitude_attach_key=pk).values()
        # cxt = {'detail':detail_data, 'img':images}
        img_detail = GratitudeJournal.objects.get(id = pk)
        user_name = img_detail.user_name
        journal_type = img_detail.journal_type

        ic(MEDIA_ROOT)
        img_path = os.path.join(MEDIA_ROOT,f'{journal_type}/{user_name}')
        ic(img_path)
        list_img = []
        for file in os.listdir(img_path):
            list_img.append(file)
        cxt = {'detail':detail_data,'img_name':list_img,'img_folder':img_detail}
        
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
