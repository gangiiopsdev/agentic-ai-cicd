from fastapi import FastAPI
import subprocess
import shlex

global blacklist = ['ping']

app = FastAPI()

def check_blacklist(command):
    for word in blacklist:
        if word in command:
            raise Exception(f'Command contains blacklisted keyword: {word}')

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    check_blacklist(' '.join(shlex.split(' '.join(command))))
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}