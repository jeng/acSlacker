# acSlacker, Copyright (c) 2015 Jeremy English <jhe@jeremyenglish.org>
#
# Permission to use, copy, modify, distribute, and sell this software and its
# documentation for any purpose is hereby granted without fee, provided that
# the above copyright notice appear in all copies and that both that
# copyright notice and this permission notice appear in supporting
# documentation.  No representations are made about the suitability of this
# software for any purpose.  It is provided "as is" without express or
# implied warranty.
 
from handler import Handler

class Echo(Handler):
    def run(self):
        d = [self.team_id,
             self.team_domain,
             self.channel_id,
             self.channel_name,
             self.user_id,
             self.user_name,
             self.command,
             self.text]
        self.write("\n".join(["%s: %s" % (x.__name__, x()) for x in d]))

