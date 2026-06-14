from fastapi import FastAPI
import subprocess
import shlex
git clone https://github.com/owasp/python-bandit.git
python bandit -r app/main.py --confidence MEDIUM