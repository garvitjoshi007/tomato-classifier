from django.shortcuts import render
from .forms import ImageUploadForm
from .predict import predict_class

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         # if form.is_valid():
#         #     image = form.cleaned_data['image']
#         if form.is_valid():
#             image_file = request.FILES['image']
#             image_data = image_file.read()
#             predicted_class = predict_class(image_data)
#             return render(request, 'result.html', {'predicted_class': predicted_class})
#     else:
#         form = ImageUploadForm()
#     return render(request, 'upload.html', {'form': form})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            instance = form.save()
            # Get the saved image path
            image_path = instance.image.path
            # Call predict_class with the image path
            predicted_class = predict_class(image_path)
            return render(request, 'result.html', {'predicted_class': predicted_class})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

