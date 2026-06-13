from fastapi import FastAPI
import subprocess
import ipaddress
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host or not isinstance(host, str) or '@' in host:
        return {'status': 'Invalid input'}
    try:
        # Validate IP address
        ipaddress.ip_address(host)
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except ValueError:
        return {'status': 'failed', 'error': 'Invalid IP address'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}