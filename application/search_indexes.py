
from django.utils import timezone
from haystack import indexes
#from models.my_model import MyModel

"""
class MyModelIndex(indexes.SearchIndex, indexes.Indexable):

	text = indexes.CharField(document = True, use_template = True, template_name = 'index/mymodel.txt')
	name = indexes.CharField(model_attr = 'name')
	#date = indexes.DateTimeField(model_attr = 'date')

	def get_model(self):
		return MyModel

	def index_queryset(self, using = None):
		return self.get_model().objects.filter(date__lte = timezone.now())
"""


