from fastapi import FastAPI
cimport os

global hosts_to_ping
hosts_to_ping = ['host1', 'host2'] # Replace with actual list of hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in hosts_to_ping:
        raise Exception('Invalid host')
    result = subprocess.call(['ping', os.path.basename(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'result': result}