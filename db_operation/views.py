from django.http import JsonResponse
from django.shortcuts import render, redirect
import csv
import pandas as pd
from db_operation.models import *


def home(request):
    try:
        data = Customer.objects.all()
        context = {'table_data': data}
        return render(request, "home.html", context)
    except Exception as e:
        print(e)

def csv_operation(request):
    try:
        if request.method == 'POST':
            csv_data = request.FILES['csv_file']
            csv_data = csv.reader(csv_data.read().decode('utf-8').splitlines())
            csv_data_df = pd.DataFrame(csv_data)
            new_header = csv_data_df.iloc[0]
            csv_data_df = csv_data_df[1:]
            csv_data_df.columns = new_header
            csv_data_df.rename(columns={'Customer ID' : 'customer_id' , 'Name' : 'name' , 'Last name' : 'last_name' , 'Email' : 'email' ,'Mobile' : 'mobile_number' ,'Address' : 'address' } ,inplace = True)
            dtypes_dict = {'customer_id': 'int', 'name': 'str', 'last_name': 'str', 'email': 'str' ,'mobile_number' : 'str' , 'address' : 'str'}
            csv_data_df = csv_data_df.astype(dtypes_dict)
            csv_data_df = csv_data_df.to_dict(orient='records')
            try :
                Customer.objects.bulk_create([Customer(**row) for row in csv_data_df])
            except Exception as e:
                print(e)
            return redirect('home')
    except Exception as e:
        print(e)


def delete_record(request,id):
    try:
        user = Customer.objects.get(pk=id)
        user.delete()
        return redirect('home')
    except Exception as e:
        print(e)