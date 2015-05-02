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
from echo import Echo
from kb import Kb

# List new command classes here
POOL = {
    '/echo': Echo, 
    '/kb'  : Kb
}


class CommandPool(Handler):

    def run(self):

        self.pool = POOL
        cmd = self.command()

        if self.pool.has_key(cmd):
            runner = self.pool[cmd](self.request, self.response)
            try:
                runner.run()
            except:
                self.write(":( failed")
        else:
            self.write("didn't find the command")

