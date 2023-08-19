from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .predict import predict_tumor
# from .form import ImageForm,ImageUploadForm
from .models import Image
from django.conf import settings


def classify_image(request):
    if request.method == "POST":
        image = request.FILES["image"]
        print(image)
        # fs = FileSystemStorage()
        custom_location = './classify/static/images'
        # print(custom_location)
        fs=FileSystemStorage(location=custom_location)
        fs2=FileSystemStorage()
        image_path=fs.save(image.name,image)
        image_path2 = fs2.save(image.name, image)
        # print(image_path)
        prediction = predict_tumor(image_path2)
        #fs.delete(image_path)  # Delete the uploaded image after processing
        return render(request, "classify/result.html", {"prediction": prediction, "image":image})

    return render(request, "classify/upload.html")

def contact(request):
    return render(request, 'classify/contact.html')
    
# def index(request):
#     if request.method == "POST":
#     form=ImageForm(data=request.POST,files=request.FILES)
#     if form.is_valid():
#     form.save()
#     obj=form.instance
#     return render(request,"index.html",{"obj":obj})
#     else:
#     form=ImageForm()
#     img=Image.objects.all()
#     return render(request,"index.html",{"img":img,"form":form})
