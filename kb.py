# acSlacker, Copyright (c) 2015 Jeremy English <jhe@jeremyenglish.org>
#
# Permission to use, copy, modify, distribute, and sell this software and its
# documentation for any purpose is hereby granted without fee, provided that
# the above copyright notice appear in all copies and that both that
# copyright notice and this permission notice appear in supporting
# documentation.  No representations are made about the suitability of this
# software for any purpose.  It is provided "as is" without express or
# implied warranty.
 
import json
import urllib
import urllib2
from handler import Handler

class Kb(Handler):
    def run(self):
        max_results = 10
        baseUrl = 'https://support.sparkpay.com'
        path = '/api/v2/help_center/articles/search.json'
        params = {'query': self.text()}
        url = "%s%s?%s" % (baseUrl, path, urllib.urlencode(params))
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        results = json.loads(the_page)
        data_sent = False

        if results.has_key("results"):
            for e in results["results"][:max_results]:
                if e.has_key("title") and e.has_key("html_url"):
                    data_sent = True
                    self.write('<%s|%s>\n' % (e["html_url"], e["title"])) 

        if not data_sent:
            self.write("Nothing")
        


