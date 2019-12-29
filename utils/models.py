import json

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext,gettext_lazy as _

from users.models import User

# Manager for changelogs
class ChangeLogManager(models.Manager):

    use_in_migration = True

    # constructor for creating a logging instance
    def log_update(self, user, content_type, object_id, content_object, changes, date_of_change):

        return self.model.objects.create(
            user = user,
            content_type = content_type,
            object_id = object_id,
            content_object = content_object,
            changes = changes,
            date_of_change = date_of_change,
        )

# changelog model
class ChangeLog(models.Model):
    user = models.ForeignKey(User, related_name = 'changed_by', on_delete = models.CASCADE)
    content_type = models.ForeignKey(ContentType, models.SET_NULL, verbose_name = _('content type'), blank = True, null = True,)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    changes = models.TextField(_('changes'), blank = True)
    date_of_change = models.DateTimeField(_('change time'), default = timezone.now, editable = False,)

    # add the changelog model to the ChangeLogManager
    objects = ChangeLogManager()

    class Meta:
        verbose_name = _('Change log entry')
        verbose_name_plural = _('Change log entries')

    # method for creating change message
    def change_message(request, obj, old_instance):

        # get the new version of the instance by querying the object
        new_instance = obj.objects.get(pk = old_instance.pk)

        # get content type for object
        ct = ContentType.objects.get_for_model(new_instance)

        # loop for checking fields on the old instance and compare it to the new one
        for field in obj._meta.get_fields():

            # filter out reverse relations to prevent typerror 
            if isinstance(field, models.ManyToOneRel):
                continue
            
            # get the value of old and new fields
            old_value = getattr(old_instance, field.name)
            new_value = getattr(new_instance, field.name)

            # check if old does not match new
            if old_value != new_value:

                # format changemessage as JSON 
                change_message = json.dumps({"field": field.name, "old_value": old_value, "new_value": new_value})
                
                # use constructor created in manager to create a new model instance
                ChangeLog.objects.log_update(
                    user = request,
                    content_type = ct,
                    content_object = new_instance,
                    object_id = new_instance.pk,
                    changes = change_message,
                    date_of_change = timezone.now()
                )

    # property to parse and returns the changed JSON
    @cached_property
    # cached property is useful as it stops parsing the changes on every access
    def changes_dict(self):
        return json.loads(self.changes)