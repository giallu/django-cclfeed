from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from cclfeed.models import MessageData

class LatestMessagesFeed(Feed):
    title = "CCL"
    link = "http://www.ccl.net/"
    description = "RSS Feed of the world's greatest computational chemistry"
    "mailing list, chemistry@ccl.net (the CCL list)",

    def items(self):
        return MessageData.objects.order_by('-sent_on')[:5]

    def item_title(self, item):
        return item.subject

    def item_description(self, item):
        return item.text

    # item_link is only needed if item has no get_absolute_url method.
    def item_link(self, item):
        baseurl = 'http://www.ccl.net/cgi-bin/ccl/message-new?'
        return baseurl + '{}+{:02}+{:02}+{:03}'.format(
            item.sent_on.year,
            item.sent_on.month,
            item.sent_on.day,
            item.ordinal
        )