import json

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


from django.db import models
from django.utils import timezone

from django.utils.translation import gettext,gettext_lazy as _

from users.models import User

"""
 Not working, yet...
"""

class ChangeLogManager(models.Manager):

    use_in_migration = True

    def log_update(self, user, content_type, object_id, content_object, changes, date_of_change):

        return self.model.objects.create(
            user = user,
            content_type = content_type,
            object_id = object_id,
            content_object = content_object,
            changes = changes,
            date_of_change = date_of_change,
        )

class ChangeLog(models.Model):
    user = models.ForeignKey(User, related_name = 'changed_by', on_delete = models.CASCADE)
    content_type = models.ForeignKey(ContentType, models.SET_NULL, verbose_name = _('content type'), blank = True, null = True,)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    changes = models.TextField(_('changes'), blank = True)
    date_of_change = models.DateTimeField(_('change time'), default = timezone.now, editable = False,)

    objects = ChangeLogManager()

    class Meta:
        verbose_name = _('Change log entry')
        verbose_name_plural = _('Change log entries')

    def change_message(request, obj, old_instance):

        new_instance = obj.objects.get(pk = old_instance.pk)

        ct = ContentType.objects.get_for_model(new_instance)

        for field in obj._meta.get_fields():
            if isinstance(field, models.ManyToOneRel):
                continue

            old_value = getattr(old_instance, field.name)
            new_value = getattr(new_instance, field.name)

            if old_value != new_value:
                change_message = json.dumps({"field": field.name, "old_value": old_value, "new_value": new_value})
                
                ChangeLog.objects.log_update(
                    user = request,
                    content_type = ct,
                    content_object = new_instance,
                    object_id = new_instance.pk,
                    changes = change_message,
                    date_of_change = timezone.now()
                )
                

                

            
            






    #def get_changes(self):
        #? 



"""
class ChangeLogManager(models.Manager):

    use_in_migration = True

    def log_update(self, user_id, content_type_id, object_id, object_representation, action_flag, change_message = ''):

        if isinstance(change_message, list):
            change_message = json.dumps(change_message)

        return self.model.objects.create(
            user_id = user_id,
            content_type_id = content_type_id,
            object_id = str(object_id),
            object_representation = object_representation[:200],
            action_flag = action_flag,
            change_message = change_message,
        )
"""
"""
class ChangeLog(models.Model):

    change_time = models.DateTimeField(
        _('change time'),
        default = timezone.now,
        editable = False,
    )

    user = models.ForeignKey(
        User, 
        related_name = 'user_changed', 
        on_delete = models.CASCADE
    )

    content_type = models.ForeignKey(
        ContentType,
        models.SET_NULL,
        verbose_name = _('content type'),
        blank = True,
        null = True,
    )

    object_id = models.TextField(_('object id'), blank = True, null = True)
    object_representation = models.CharField(_('object representation'), max_length = 200)
    action_flag = models.PositiveSmallIntegerField(_('action flag'), choices = ACTION_FLAG_CHOICES)
    change_message = models.TextField(_('change message'), blank = True)

    objects = ChangeLogManager()

    class Meta:
        verbose_name = _('Change log entry')
        verbose_name_plural = _('Change log entries')
    
    def __repr__(self):
        return str(self.change_time)

    def __str__(self):

        if self.is_addition():
            return gettext('Added "%(object)s".') % {'object': self.object_representation}

        elif self.is_change():
            return gettext('Changed “%(object)s” — %(changes)s') % {
                'object': self.object_representation,
                'changes': self.get_change_message(),
            }

        elif self.is_deletion():
            return gettext('Deleted "%(object)s"') % {'object': self.object_representation}

        return gettext('ChangeLog Object')

    def is_addition(self):
        return self.action_flag == ADDITION

    def is_change(self):
        return self.action_flag == CHANGE

    def is_deletion(self):
        return self.action_flag == DELETION

    def get_change_message(self):

        if self.change_message and self.change_message[0] == '[':
            try:
                change_message = json.loads(self.change_message)
            except json.JSONDecodeError:
                return self.change_message
            
            messages = []

            for sub_message in change_message:
                if 'added' in sub_message:
                    if sub_message['added']:
                        sub_message['added']['name'] = gettext(sub_message['added']['name'])
                        messages.append(gettext('Added {name} "{object}".').format(**sub_message['added']))

                    else:
                        messages.append(gettext('Added.'))

                elif 'changed' in sub_message:
                    sub_message['changed']['fields'] = get_text_list(
                        [gettext(field_name) for field_name in sub_message['changed']['fields']], gettext('and')
                    )
                    if 'name' in sub_message['changed']:
                        sub_message['changed']['name'] = gettext(sub_message['changed']['name'])
                        messages.append(gettext('Changed {fields} for {name} “{object}”.').format(
                            **sub_message['changed']
                        ))
                    else:
                        messages.append(gettext('Changed {fields}.').format(**sub_message['changed']))

                elif 'deleted' in sub_message:
                    sub_message['deleted']['name'] = gettext(sub_message['deleted']['name'])
                    messages.append(gettext('Deleted {name} “{object}”.').format(**sub_message['deleted']))

            change_message = ' '.json(msg[0].upper() + msg[1:] for msg in messages)
            return change_message or gettext('No fields changed.')

        else:
            return self.change_message

    def get_edited_object(self):
        return self.content_type.get_object_for_this_type(pk = self.object_id)


"""

