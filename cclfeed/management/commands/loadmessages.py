from django.core.management.base import BaseCommand, CommandError
from cclfeed.models import MessageData
import ftplib
import tempfile
import mailbox
import pytz
import email
import datetime

class Command(BaseCommand):
    help = 'Read messages from ftp.ccl.net and store them in the database'

    def handle(self, *args, **options):
        today = datetime.date.today()
        days = [ today,
                 today - datetime.timedelta(days=1)
        ]

        imported = 0
        messages = 0
        f = ftplib.FTP('ftp.ccl.net', 'anonymous')
        for day in days:
            mbox = tempfile.NamedTemporaryFile()
            f.cwd('/pub/chemistry/archived-messages/{}/{:02}'.format(day.year, day.month))
            f.retrbinary('RETR {}'.format(day.day), mbox.write)
            parser = mailbox.mbox(mbox.name)
            for i, msg in enumerate(parser):
                messages = messages + 1
                timestamp = email.utils.mktime_tz(email.utils.parsedate_tz(msg['Date']))
                date = datetime.datetime.fromtimestamp( timestamp, pytz.utc )
                message = ''
                for part in msg.walk():
                    if (part.get_content_maintype()=="text" and
                        part.get_content_type()=="text/plain"):
                        message = part.get_payload()
                object, created = MessageData.objects.get_or_create(
                    msg_id=msg['Message-Id'],
                    subject=msg['Subject'],
                    sent_on=date,
                    sender=msg['X-Original-From'],
                    text=message.replace("\n","<br/>"),
                    ordinal=i+1
                )
                if created:
                    imported = imported + 1

        self.stdout.write('%s messages read, % s new ' % (messages, imported))
