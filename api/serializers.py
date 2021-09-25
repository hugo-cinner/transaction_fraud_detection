from rest_framework import serializers
from .models import Transaction


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('uuid', 'step', 'type', 'amount', 'nameOrig', 'oldbalanceOrig', 'newbalanceOrig',
                  'nameDest', 'oldbalanceDest', 'newbalanceDest', 'isFraud')
