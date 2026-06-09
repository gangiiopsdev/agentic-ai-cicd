from fastapi import FastAPI
import subprocess
import shlex

class SafePingException(Exception):
    pass

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call with input validation
    try:
        args = ['ping', *shlex.split(host)]
        subprocess.run(args, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')
        return False
    except shlex.Error as e:
        raise SafePingException('Invalid input for ping command') from e

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}