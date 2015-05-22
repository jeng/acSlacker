acSlacker
=========

A google app engine program for implementing [slack
commands](https://api.slack.com/slash-commands)

To add a new command create an object that inherits Handler. Then add it to the
POOL dictionary in the CommandPool.  That's all you have to do.  

I've included a couple of examples.  Echo just dumps all of the parameters.  Kb
hits a json endpoint, parses the results and then uses Slack's formatting for
the links.

To make sure someone doesn't hijack your commands, the yaml file should contain
your tokens. The `SLACK_TOKEN` environment variable needs to be a comma
separated string in the format `<command>:<token>`.  A single command can have multiple tokens.  Just separate each one with a colon.

