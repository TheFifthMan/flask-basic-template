from . import index_bp
from .views import Index,TaskStatus
index_bp.add_url_rule('/',view_func=Index.as_view('index'))
index_bp.add_url_rule('/status/<task_id>',view_func=TaskStatus.as_view('task_status'),methods=['GET'])

# url_for 的时候怎么用？
# url_for('index.index') index 可以类比为就是这个函数的名字