import datetime
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now

from cclfeed.models import MessageData

DEFAULT_DAYS = 15

class Command(BaseCommand):
    help = 'Delete the older messages from the database'
    option_list = BaseCommand.option_list + (
        make_option('-d', '--days',
                    dest='days',
                    type='int',
                    default=DEFAULT_DAYS,
                    help=('Remove al messages older than ' + 
                          'the specified number ' + 
                          'of days (def. {0})').format(DEFAULT_DAYS),
                    ),
        )

    def handle(self, *args, **options):
        oldest = now() - datetime.timedelta(days=options['days'])
        MessageData.objects.filter(sent_on__lt=oldest).delete()
