from django.db.models.fields.files import FieldFile


def file_type(filename):
	filename = filename.split('.')
	filetype = filename[len(filename) - 1].lower()
	return filetype

def upload_to(instance, filename):
	puth = ''
	# content_object
	# parent
	# fk

	puth += instance._meta.app_label + '/'
	puth += instance._meta.model_name + '/'

	# Check for many fields
	file_fields = []
	for field_name, _ in instance.__dict__.iteritems():
		field = getattr(instance, field_name)
		if issubclass(field.__class__, FieldFile):
			file_fields.append(field_name)
		if field == filename:
			current_field_name = field_name

	# Prefix by field name
	if len(file_fields) > 1:
		puth += current_field_name + '_'

	# Name
	if hasattr(instance, 'slug'):
		name = instance.slug
	else:
		name = '%s' % instance.id

	# Ext
	puth += name + '.'
	puth += file_type(filename)

	return puth
