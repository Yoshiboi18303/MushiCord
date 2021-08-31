import os
loginToken = os.environ['TOKEN']
from event_handler import ready_bot

ready_bot('MushiCord', loginToken, True)