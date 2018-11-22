from . import index_bp
from .views import Index
index_bp.add_url_rule('/',view_func=Index.as_view('index'))

# url_for 的时候怎么用？
# url_for('index.index') index 可以类比为就是这个函数的名字