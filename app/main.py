from fastapi import FastAPI
import subprocess
import shlex

global_count = 0

app = FastAPI()

def safe_ping(host):
    global global_count
    # Safe implementation using shlex.quote to escape arguments and logging
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    print(f'Ping executed {global_count} times: {result.stdout}')
    global_count += 1

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}