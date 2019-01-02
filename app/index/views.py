from flask.views import MethodView
from app import celery
from flask import jsonify
import requests,time
@celery.task
def test_task(arg1,arg2):
    time.sleep(100)
    r = requests.get('https://www.baidu.com')
    with open('baidu.html','w')as f:
        f.write(r.text)
    

class Index(MethodView):
    def get(self):
        task = test_task.delay(100,100)
        return jsonify({"taskid":task.id,"task_state":task.state})


class TaskStatus(MethodView):
    def get(self,task_id):
        task= test_task.AsyncResult(task_id)
        if task.state == "PENDING":
            response = {
                'state':task.state,
                'current':0,
                'total':1,
                'status':"Pending..."
            }
        elif task.state != "FAILURE":
            response = {
                'state': task.state,
                'info':task.info
            }
        
        else:
            # something went wrong in the background job
            response = {
                'state': task.state,
                'current': 1,
                'total': 1,
                'status': str(task.info),  # this is the exception raised
            }
        return jsonify(response)  

