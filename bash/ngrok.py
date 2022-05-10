# This program can install ngrok in linux

import os
import time

url = input('Enter ngrok download link :')

# Commands
cmd1 = 'wget '+url+' -O ngrok.tgz'
cmd2 = 'sudo tar xvzf ./ngrok.tgz -C /usr/local/bin'

# Start commands
os.system(cmd1)
os.system(cmd2)
