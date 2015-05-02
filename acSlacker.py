# acSlacker, Copyright (c) 2015 Jeremy English <jhe@jeremyenglish.org>
#
# Permission to use, copy, modify, distribute, and sell this software and its
# documentation for any purpose is hereby granted without fee, provided that
# the above copyright notice appear in all copies and that both that
# copyright notice and this permission notice appear in supporting
# documentation.  No representations are made about the suitability of this
# software for any purpose.  It is provided "as is" without express or
# implied warranty.

import os
import webapp2
from handler import Handler
from commandPool import CommandPool

class Slacker(Handler):

    def post(self):

        tokens = dict([tuple(x.strip().split(":")) 
                 for x in os.environ["SLACK_TOKEN"].split(",")])

        cmd = self.command()
        if tokens.has_key(cmd) and self.token() == tokens[cmd]:
            command_pool = CommandPool(self.request, self.response)
            command_pool.run()
        else:
            self.write("Sorry")

app = webapp2.WSGIApplication([('/slacker', Slacker)],
        debug=os.environ["DEBUGGING"])

