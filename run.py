from app import create_app,db,celery
app = create_app('default')
app.app_context().push()

from app.index.models import *
@app.shell_context_processor
def shell_context_processor():
    return {"db":db}