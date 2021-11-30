
# celery_squirrel.py
 
import time
from utils import check_website
from data import WEBSITE_LIST
from celery import Celery
from celery.result import ResultSet
 
app = Celery('celery_squirrel',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')
 
@app.task
def check_website_task(address):
    return check_website(address)
 
if __name__ == "__main__":
    start_time = time.time()
 
    
    rs = ResultSet([check_website_task.delay(address) for address in WEBSITE_LIST])
     
    
    rs.get()
 
    end_time = time.time()
 
    print("CelerySquirrel:", end_time - start_time)
    
