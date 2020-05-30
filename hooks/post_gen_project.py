#!/usr/bin/env python

import re
import os
import sys


msgs = [s for s in re.split('[\s,]+', '{{ cookiecutter.generated_msgs }}') if s != '']
srvs = [s for s in re.split('[\s,]+', '{{ cookiecutter.generated_srvs }}') if s != '']
actions = [s for s in re.split('[\s,]+', '{{ cookiecutter.generated_actions }}') if s != '']

os.mkdir('msg')
for msg in msgs:
    fname = msg.partition('.')[0].strip() + '.msg'
    fh = open(os.path.join('msg', fname), 'w')
    fh.close()
os.mkdir('srv')
for srv in srvs:
    fname = srv.partition('.')[0].strip() + '.srv'
    fh = open(os.path.join('srv', fname), 'w')
    fh.close()
os.mkdir('action')
for action in actions:
    fname = action.partition('.')[0].strip() + '.action'
    fh = open(os.path.join('action', action), 'w')
    fh.close()
