from icecream import ic
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import datetime
from journaling.settings import MEDIA_ROOT
def img_format(image , journal_type , user_id , username):
    format_img = []
    for x in image:
        img_split = x.name.split('.')
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        new_image_name = journal_type + '_' + username + '_' + user_id + timestamp +'.'+img_split[-1]
        format_img.append(new_image_name)
    return format_img

# file_path = '/home/satyam/Documents/HealthJournal/journaling/media/GJ/satyam/'
"""
Few Changes which I have to work on tomorrow is first check why journal_type is still comming to be LJ , GJ and not life_journal and  gratitude_journal




"""





def writefile_to_dir(file_path , uploaded_images,format_img):
    data_path = []
    for x in format_img:
        data = f'{file_path}/{x}'
        data_path.append(data)
        ic(data_path)
        ic(uploaded_images)

    for i in range(len(data_path)):
        ic(data_path[i])
        ic(uploaded_images[i])
        path = default_storage.save(data_path[i],ContentFile(uploaded_images[i].read()))

    # for x in uploaded_images:
    #      path = default_storage.save(data,ContentFile(uploaded_images.read()))
    # return path