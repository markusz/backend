from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TokenSerializer, AccountingSerializer
from .models import Token, Accounting
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


class CreateView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = TokenSerializer

    def get_queryset(self):
        queryset = Token.objects.all()
        status = self.request.query_params.get('active', None)
        if status is not None:
            if status == 'true':
                status = True
            else:
                status = False
            queryset = queryset.filter(is_active=status)
        return queryset


class DetailsView(APIView):
    """This class handles the http GET and PATCH requests."""

    # queryset = Token.objects.all()
    # serializer_class = TokenSerializer
    def get_object(self, pk):
        return Token.objects.get(pk=pk)

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = TokenSerializer(obj)
        return Response(serializer.data)

    def patch(self, request, pk):
        update_object = self.get_object(pk)
        serializer = TokenSerializer(update_object, data=request.data,
                                     partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedeemView(APIView):
    def get_object(self, pk):
        return Token.objects.get(pk=pk)

    def patch(self, request, pk):
        update_object = self.get_object(pk)
        # if update_object.is_active:
        request.data['is_active'] = False
        serializer = TokenSerializer(update_object, data=request.data,
                                 partial=True)
        if serializer.is_valid():
            self.update_balance(update_object)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
            # import pdb
            # pdb.set_trace()
            # return Response(JsonResponse(data={'res':'double spend'}), status=status.HTTP_402_PAYMENT_REQUIRED)

    def update_balance(self, update_object):
        try:
            accounting_obj = Accounting.objects.get(
                media_type=update_object.media_type)
        except ObjectDoesNotExist:
            accounting_obj = Accounting(media_type=update_object.media_type,
                                        limits=update_object.duration)
        else:
            test = accounting_obj.limits + update_object.duration
            test = max([0, test])
            accounting_obj.limits = test
        accounting_obj.save()
        return True


class BalanceView(generics.ListAPIView):
    queryset = Accounting.objects.all()
    serializer_class = AccountingSerializer


class BudgetView(APIView):
    def post(self, request):
        source_type = self.request.query_params.get('type', 'YT')
        accounting_obj = Accounting.objects.get(media_type=source_type)
        accounting_obj.limits += request.data['duration']
        accounting_obj.save()
        serializer = AccountingSerializer(accounting_obj)
        return Response(serializer.data)


class HeartbeatView(APIView):
    def get(self, request):
        source_type = request.query_params.get('type', 'YT')
        accounting_obj = Accounting.objects.get(media_type=source_type)
        accounting_obj.limits -= 2
        accounting_obj.save()
        serializer = AccountingSerializer(accounting_obj)
        return Response(serializer.data)
