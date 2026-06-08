from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using Popen
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'stdout': output.decode(), 'stderr': error.decode() if error else None}

def safe_ping2(host):
    # Safe implementation using check_output
    import shlex
    args = shlex.split(f'ping {host}')
    try:
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'stdout': output.decode(), 'stderr': None}
    except subprocess.CalledProcessError as e:
        return {'stdout': None, 'stderr': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}