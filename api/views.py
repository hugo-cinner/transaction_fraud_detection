from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import never_cache
from .serializers import InputSerializer
from .models import Transaction
from .utils import *


@api_view(['GET'])
@never_cache
def test_api(request):
    return Response({'response': "You are successfully connected to the Transaction Fraud Detection API"})



@api_view(['POST'])
@never_cache
def run_fraud_detection_inference(request):
    step = int(request.POST.get('step'))
    type = str(request.POST.get('type'))
    amount = float(request.POST.get('amount'))
    nameOrig = str(request.POST.get('nameOrig'))
    oldbalanceOrig = float(request.POST.get('oldbalanceOrig'))
    newbalanceOrig = float(request.POST.get('newbalanceOrig'))
    nameDest = str(request.POST.get('nameDest'))
    oldbalanceDest = float(request.POST.get('oldbalanceDest'))
    newbalanceDest = float(request.POST.get('newbalanceDest'))

    input_dict = {
        "step": step,
        "type": type,
        "amount": amount,
        "nameOrig": nameOrig,
        "oldbalanceOrig": oldbalanceOrig,
        "newbalanceOrig": newbalanceOrig,
        "nameDest": nameDest,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }

    # get all similar records
    pass_records = Transaction.objects.filter(step=str(step), type=type, nameOrig=nameOrig, nameDest=nameDest,
                                              amount=str(amount))
    if len(pass_records) > 3:
        output = True
    else:
        output = RunFraudDetectionInference(input_dict).run()

    input_dict['isFraud'] = output

    record_serializer = InputSerializer(data=input_dict)

    if record_serializer.is_valid():
        record_serializer.save()

    # check limit records
    LIMIT = 2000
    all_records = Transaction.objects.all()
    if len(all_records) >= LIMIT:
        Transaction.objects.filter(uuid__in=list(Transaction.objects.values_list('uuid', flat=True)[:500])).delete()



    return Response({"isFraud": output})
