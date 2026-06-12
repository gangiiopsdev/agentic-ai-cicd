from fastapi import FastAPI
import re
import shlex

class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Validate the host to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host): raise ValueError('Invalid host name')
        safe_host = shlex.quote(host)
        output = subprocess.run(['ping', '-c', '4', safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)