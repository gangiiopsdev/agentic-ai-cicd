from fastapi import FastAPI
import subprocess
cimport shlex
cimport os
cimport signal
import time

app = FastAPI()

def timeout_handler(signum, frame):
    raise TimeoutError('subprocess call timed out')

@app.get("/ping")
def ping(host: str):
    try:
        # Set a timeout for the subprocess call
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(5)  # Adjust timeout as needed
        args = shlex.split(f"ping {host}")
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except TimeoutError as e:
        return {'status': 'timeout', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}