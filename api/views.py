from rest_framework import filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.serializers import ValidationError

from user.models import CustomUser
from CRM.models import Client, Lead, Contract, Event, EventStatus
from api.permissions import (ContractPermissions, EventPermissions,
                             LeadsPermissions, ClientsPermissions,
                             EventStatusPermissions)
from api.serializers import (UserSerializer, ClientSerializer,
                             LeadSerializer, ContractSerializer,
                             EventSerializer, EventStatusSerializer)


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class ClientViewSet(ModelViewSet):

    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated, ClientsPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['last_name', 'email']
    search_fields = ['last_name', 'email']

    def create(self, request, project_pk=None, *args, **kwargs):
        data = request.data
        client = Client.objects.create(first_name=data['first_name'],
                                       last_name=data['last_name'],
                                       email=data['email'],
                                       phone=data['phone'],
                                       mobile=data['mobile'],
                                       company_name=data['company_name'],
                                       sales_contact=request.user)

        client.save()
        serializer = ClientSerializer(client)
        return Response(serializer.data)


class LeadViewSet(ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.filter(converted_to_client=False)
    permission_classes = [IsAuthenticated, LeadsPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['last_name', 'email']
    search_fields = ['last_name', 'email']

    def create(self, request, *args, **kwargs):
        data = request.data
        lead = Lead.objects.create(first_name=data['first_name'],
                                   last_name=data['last_name'],
                                   email=data['email'],
                                   phone=data['phone'],
                                   mobile=data['mobile'],
                                   company_name=data['company_name'],
                                   sales_contact=request.user)

        lead.save()
        serializer = LeadSerializer(lead)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        lead = Lead.objects.get(pk=pk)
        lead.converted_to_client = True
        lead.save()
        client = Client.objects.create(
                first_name=lead.first_name,
                last_name=lead.last_name,
                email=lead.email,
                phone=lead.phone,
                mobile=lead.mobile,
                company_name=lead.company_name,
                date_created=lead.date_created,
                date_updated=lead.date_updated,
                sales_contact=lead.sales_contact
        )
        client.save()
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    @action(description="Convertir en client", detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def convert_to_client(self, request, pk):
        user = request.user
        lead = Lead.objects.get(pk=pk)
        if user == lead.sales_contact or user.role == "Gestion":
            lead.converted_to_client = True
            lead.save()
            client = Client.objects.create(
                    first_name=lead.first_name,
                    last_name=lead.last_name,
                    email=lead.email,
                    phone=lead.phone,
                    mobile=lead.mobile,
                    company_name=lead.company_name,
                    date_created=lead.date_created,
                    date_updated=lead.date_updated,
                    sales_contact=lead.sales_contact
            )
            client.save()
            return Response()
        else:
            return Response("You do not have the required authorizations for this operation")


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    permission_classes = [IsAuthenticated, ContractPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['client__last_name', 'client__email', 'date_created', 'amount']
    search_fields = ['client__last_name', 'client__email', 'date_created', 'amount']

    def retrieve(self, request, pk, *args, **kwargs):
        contract = Contract.objects.get(pk=pk)
        serializer = ContractSerializer(contract)
        return Response(serializer.data)

    @action(description="Valider le contrat", detail=True, methods=['get'],)
    def validate_a_contract(self, request, pk):
        contract = Contract.objects.get(pk=pk)
        contract.status = True
        contract.save()
        return Response()


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated, EventPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['client__last_name', 'client__email', 'event_date']
    search_fields = ['client__last_name', 'client__email', 'event_date']

    def perform_create(self, serializer):
        if serializer.validated_data['contract'] is None:
            raise ValidationError("Le champ contrat ne peut pas être vide.")
        super().perform_create(serializer)


class EventStatusViewSet(ModelViewSet):
    serializer_class = EventStatusSerializer
    queryset = EventStatus.objects.all()
    permission_classes = [IsAuthenticated, EventStatusPermissions]
