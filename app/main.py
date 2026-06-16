from fastapi import FastAPI
import subprocess
genesis = '''#!/bin/sh\nif [ "$@" != "" ]; then\
    ping $@\
fi'''\nwith open('ping.sh', 'w') as f:\n    f.write(genesis)\nsubprocess.call(['sh', './ping.sh', '{host}'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    subprocess.call(['sh', './ping.sh', host])
    return {'status': 'completed'}