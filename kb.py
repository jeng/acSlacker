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
import StringIO
from lxml import etree
from handler import Handler

class Kb(Handler):
    def run(self):
        baseUrl = 'http://support.americommerce.com'
        path = '/hc/en-us/search'
        params = {'utf8': '%E2%9C%93', 
                  'query': self.text(), 
                  'commit':'Search', 
                  'format':'json'}
        url = "%s%s?%s" % (baseUrl, path, urllib.urlencode(params))
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        results = json.loads(the_page)
        if results.has_key("html"):
            doc = results["html"]
            parser = etree.HTMLParser()
            html = etree.parse(StringIO.StringIO(doc), parser)

            anchors = [(x.text, [y for y in x.items() if y[0] == 'href'][0:]) 
                       for x in html.iter() if x.tag == 'a']

            wellformed = [(title, baseUrl+attr[0][1]) 
                          for title, attr in anchors 
                          if len(attr) > 0 and len(attr[0]) == 2]

            for post, location in wellformed:
                self.write('<%s|%s>\n' % (location, post)) 
        else:
            self.write("Nothing")


