from rest_framework import serializers

from .models import Wallet, Transaction
from semillas_backend.users.serializers import UserSerializer


class CreateWalletSerializer(serializers.ModelSerializer):
    """ Usage:
    """
    class Meta:
        model = Wallet
        fields = ('uuid', 'owner', 'balance', 'last_updated', 'transactions')

class TransactionSerializer(CreateWalletSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'value', 'running_balance', 'created_at')

class WalletSerializer(CreateWalletSerializer):
    """ Usage:
        from rest_framework.renderers import JSONRenderer
        from semillas_backend.users.serializers import UserSerializer

        JSONRenderer().render(UserSerializer(user_instance).data)
    """
    transactions = TransactionSerializer(many=True)
    owner = UserSerializer()