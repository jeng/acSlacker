# acSlacker, Copyright (c) 2015 Jeremy English <jhe@jeremyenglish.org>
#
# Permission to use, copy, modify, distribute, and sell this software and its
# documentation for any purpose is hereby granted without fee, provided that
# the above copyright notice appear in all copies and that both that
# copyright notice and this permission notice appear in supporting
# documentation.  No representations are made about the suitability of this
# software for any purpose.  It is provided "as is" without express or
# implied warranty.

import sys
import re
import os
import json
import datetime
import logging
import webapp2

class Handler(webapp2.RequestHandler):

    def token(self):
        return self.request.get("token")

    def team_id(self):
        return self.request.get("team_id")

    def team_domain(self):
        return self.request.get("team_domain")

    def channel_id(self):
        return self.request.get("channel_id")

    def channel_name(self):
        return self.request.get("channel_name")

    def user_id(self):
        return self.request.get("user_id")

    def user_name(self):
        return self.request.get("user_name")

    def command(self):
        return self.request.get("command")

    def text(self):
        return self.request.get("text")

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def info(self, s):
        logging.info("%s : %s" % (self.__class__, s))
 
    def json_content(self):
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'

    def json_write(self, data):
        self.write(json.dumps(data))

    def set_response(self, response):
        self.response = response


