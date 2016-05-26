import os
from django.conf import settings

from django.db.models.fields.files import FieldFile
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

if settings.hasattr(MEDIA_TRASH):
	def move2trash(field):
		old_path = field.path
		new_path = settings.MEDIA_TRASH + field.name

		trash_dir = os.path.dirname(new_path)

		try:
			os.makedirs(trash_dir, mode=0o777)
		except:
			pass

		os.rename(old_path, new_path)

	@receiver(pre_delete)
	def on_delete(sender, instance, *args, **kwargs):
		for field_name, _ in instance.__dict__.iteritems():
			field = getattr(instance, field_name)
			if issubclass(field.__class__, FieldFile):
				move2trash(previos_file)


	@receiver(pre_save)
	def on_change(sender, instance, *args, **kwargs):
		try:
			previos = sender.objects.get(id=instance.id)

			for field_name, _ in instance.__dict__.iteritems():
				field = getattr(instance, field_name)
				if issubclass(field.__class__, FieldFile):
					previos_file = getattr(previos, field_name)
					if previos_file != field:
						print 'move!'
						move2trash(previos_file)
		except:
			pass