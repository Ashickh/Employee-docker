# schema.py

import graphene
from graphene_django.types import DjangoObjectType
from .models import Employee

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee

class CreateEmployee(graphene.Mutation):
    class Arguments:
        emp_id = graphene.String(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        designation = graphene.String(required=True)

    employee = graphene.Field(EmployeeType)

    def mutate(self, info, emp_id, name, email, designation):
        employee = Employee.objects.create(emp_id=emp_id, name=name, email=email, designation=designation)
        return CreateEmployee(employee=employee)

class Query(graphene.ObjectType):
    employees = graphene.List(EmployeeType)

    def resolve_employees(self, info):
        return Employee.objects.all()

class Mutation(graphene.ObjectType):
    create_employee = CreateEmployee.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
