from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import never_cache
# from .models import Transaction
from .utils import *


@api_view(['GET'])
@never_cache
def test_api(request):
    return Response({'response': "You are successfully connected to the Transaction Fraud Detection API"})


# @api_view(['POST'])
# @never_cache
# def run_inference(request):
#     property_id = request.POST.get('property_id')
#
#     # converts querydict to original dict
#     images = dict((request.data).lists())['image']
#     flag = 1
#     arr = []
#     for img_name in images:
#         modified_data = modify_input_for_multiple_files(property_id,
#                                                         img_name)
#         file_serializer = ImageSerializer(data=modified_data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             arr.append(file_serializer.data)
#         else:
#             flag = 0
#
#     if flag == 1:
#         image_path = os.path.relpath(arr[0]['image'], '/')
#         # bg_path = os.path.relpath(arr[1]['image'], '/')
#         input_image = ImageSegmentation.objects.create(input_image=image_path, name='image_%02d' % uuid.uuid1())
#         serializer = OutputImageSerializer(input_image)
#         return Response(serializer.data)
#
#
# @api_view(['POST'])
# @never_cache
# def get_images(request):
#     property_id = request.POST.get('property_id')
#
#     # converts querydict to original dict
#     images = dict((request.data).lists())['image']
#     flag = 1
#     arr = []
#     for img_name in images:
#         modified_data = modify_input_for_multiple_files(property_id,
#                                                         img_name)
#         file_serializer = ImageSerializer(data=modified_data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             arr.append(file_serializer.data)
#         else:
#             flag = 0
#
#     if flag == 1:
#         return Response(arr, status=status.HTTP_201_CREATED)
#     else:
#         return Response(arr, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@never_cache
def run_fraud_detection_inference(request):
    input_dict = {
        "step": int(request.POST.get('step')),
        "type": str(request.POST.get('type')),
        "amount": float(request.POST.get('amount')),
        "nameOrig": str(request.POST.get('nameOrig')),
        "oldbalanceOrig": float(request.POST.get('oldbalanceOrig')),
        "newbalanceOrig": float(request.POST.get('newbalanceOrig')),
        "nameDest": str(request.POST.get('nameDest')),
        "oldbalanceDest": float(request.POST.get('oldbalanceDest')),
        "newbalanceDest": float(request.POST.get('newbalanceDest'))
    }

    output = RunFraudDetectionInference(input_dict).run()
    return Response({"isFraud": output})
