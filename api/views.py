from rest_framework.response import Response
from rest_framework.decorators import api_view
from employee.models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET'])
def overview(request):
    api_details = {
        '/get': "Get all the Employees",
        '/get/<int:id>': "Get one Employee",
        '/add': "Add an employee",
        '/update/<int:id>': "Update an Employee",
        '/delete/<int:id>': "Delete an Employee"
    }
    return Response(api_details)

@api_view(['GET'])
def getData(request):
    data = Employee.objects.all()
    serializedData = EmployeeSerializer(data, many=True)
    return Response(serializedData.data)

@api_view(['GET'])
def getEmployee(request, pk):
    try:
        employee = Employee.objects.get(id=pk)
    
        employeeSerialized = EmployeeSerializer(employee)
        return Response(employeeSerialized.data)
    except:
        return Response({"msg": f"No user found with id: {pk}"})
@api_view(['POST'])
def addEmployee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateEmployee(request, pk):
    emp = Employee.objects.get(id=pk)
    
    serializer = EmployeeSerializer(instance=emp, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteEmployee(requet, pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()
    
    return Response({"msg": "Employee deleted with ID: " + str(pk)})