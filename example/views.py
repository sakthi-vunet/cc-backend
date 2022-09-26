import json
from django.http import JsonResponse
from . import db_labels
from . import db_inserthosts
from . import db_updatehosts
from django.http import QueryDict
from . import db_versioninfo
from . import services_start_stop
from . import db_settings
from . import container_logs
from . import hostsnew
from . import servicesdbdocker
from . import containersdbdocker



def get_containers():
    
    out_json=containersdbdocker.get_containers_dbdocker()
    json_obj=json.loads(out_json)
    return json_obj


def get_containers_id(id):
    result=[]
    getall=get_containers()
    for keyval in getall:
        if id == keyval['_id']:
            result.append(keyval)
    return result


def index_containers(request):
    if request.method=="GET":
        if request.GET.get("_id") is None:
            return JsonResponse(get_containers(),safe=False)
        else:
            return JsonResponse(get_containers_id(request.GET.get("_id")),safe=False)
    
    elif request.method=="PUT":
        temp=json.loads(request.body.decode('utf-8'))
        print(temp['name'],temp['action'])
        return JsonResponse(json.loads(request.body.decode('utf-8')))

def index_logs_containers(request):
    if request.method=="GET":
        return JsonResponse(container_logs.get_container_logs(request.GET.get("_id")),safe=False)

def get_services():
    out_json=servicesdbdocker.get_service_data()
    json_obj=json.loads(out_json)
    return json_obj



def get_services_id(id):
    result=[]
    getall=get_services()
    print("Id from function",id)
    for keyval in getall:
        if int(id)== keyval['_id']:
            result.append(keyval)
    return result


def index_services(request):
    if request.method=="GET":
        if request.GET.get("_id") is None:
            return JsonResponse(get_services(),safe=False)
        else:
            
            return JsonResponse(get_services_id(request.GET.get("_id")),safe=False)
    
    elif request.method=="PUT":
        temp=json.loads(request.body.decode('utf-8'))
        print(temp['name'],temp['action'])
        response=services_start_stop.service_actions(temp['name'],temp['action'])
        return JsonResponse(json.loads(response))
    
    elif request.method=="POST":
        temp=json.loads(request.body.decode('utf-8'))
        return JsonResponse(temp)


def get_hosts():
    out_json=hostsnew.get_hosts()
    json_obj=json.loads(out_json)
    return json_obj


def get_hosts_id(id):
    result=[]
    getall=get_hosts()
    for keyval in getall:
        if id == keyval["name"]:
            result.append(keyval)
    return result


def index_hosts(request):
    if request.method=="GET":
        if request.GET.get("name") is None:
            return JsonResponse(get_hosts(),safe=False)
        else:
            return JsonResponse(get_hosts_id(request.GET.get("name")),safe=False)

    elif request.method=="POST":
        print('BODY', request.body)
        host_item= json.loads(request.body.decode('utf-8'))
        db_inserthosts.insert_hosts(host_item)
        return JsonResponse(json.loads(request.body.decode('utf-8')))
    
    elif request.method=="PUT":
        print('Body',request.body)
        host_item= json.loads(request.body.decode('utf-8'))
        db_updatehosts.update_hosts(host_item)
        return JsonResponse(json.loads(request.body.decode('utf-8')))



def get_labels():
    result=db_labels.getfromdb_labels()
    result=result.to_dict()
    result=result[0]
    return result
 


def index_labels(request):
    if request.method=="GET":
        return JsonResponse(get_labels(),safe=False)


def index_settings(request):
    if request.method=="GET":
        return JsonResponse(db_settings.getfromdb_settings(),safe=False)

def get_status():
    with open('/home/sakthi/Downloads/cc-backend/jsondata/status.json','r') as fp:
        out_json = json.load(fp)
    return out_json

def index_status(request):
    if request.method=="GET":
        return JsonResponse(get_status(),safe=False)

def index_version_info(request):
    if request.method=="GET":
        return JsonResponse(db_versioninfo.getfromdb_versioninfo(),safe=False)


