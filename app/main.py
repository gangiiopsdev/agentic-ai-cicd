from fastapi import FastAPI
import subprocess
def ping_host(host):
    try:
        git = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = git.communicate()
        return {'status': 'completed', 'stdout': output.decode('utf-8'), 'stderr': error.decode('utf-8')}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()
app.get('/ping/{host}')
(app, ping_host)