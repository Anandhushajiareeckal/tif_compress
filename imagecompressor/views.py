from rest_framework.views import APIView
from django.http import HttpResponse
from PIL import Image
import io

from .serializers import ImageUploadSerializer

class ImageCompressView(APIView):
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image_file = request.FILES['image']
            image = Image.open(image_file)

            # Compress the image
            output = io.BytesIO()
            image.save(output, format='TIFF', compression='tiff_lzw')
            output.seek(0)

            # Return the compressed image as a response
            return HttpResponse(output.read(), content_type='image/tiff')

        return HttpResponse(serializer.errors, status=400)
