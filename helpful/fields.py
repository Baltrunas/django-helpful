from django.db.models.fields.files import FieldFile


def get_ext(filename):
	filename = filename.split('.')
	filetype = filename[len(filename) - 1].lower()
	if filetype == 'jpeg':
		filetype = 'jpg'
	return filetype

def get_unique(instance):
	if instance.id:
		instance_id = instance.id
	else:
		Model = instance.__class__
		if Model.objects.all():
			last = Model.objects.all().order_by('-id')[0]
			instance_id = last.id + 1
		else:
			instance_id = 1

	if hasattr(instance, 'slug'):
		if instance._meta.get_field('slug').unique:
			return instance.slug
		else:
			return '%s-%s' % (instance_id, instance.slug)
	else:
		return '%s' % instance_id


def get_field(instance, filename):
	file_fields = []
	for field_name, _ in instance.__dict__.items():
		field = getattr(instance, field_name)
		if issubclass(field.__class__, FieldFile):
			file_fields.append(field_name)
		if field == filename:
			return field_name


def upload_to(instance, filename):
	puth = ''

	if hasattr(instance, 'dependent_from'):
		dependent_from = instance.dependent_from()
		puth += dependent_from._meta.app_label + '/'
		puth += dependent_from._meta.model_name + '/'
		puth += get_unique(dependent_from) + '/'

		# instance._meta.app_label
		puth += instance._meta.model_name + '/'

		puth += get_unique(instance) + '/'
		puth += get_field(instance, filename) + '.'
	else:
		puth += instance._meta.app_label + '/'
		puth += instance._meta.model_name + '/'
		puth += get_unique(instance) + '/'
		puth += get_field(instance, filename) + '.'

	puth += get_ext(filename)
	return puth
