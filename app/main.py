from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Safe implementation using subprocess.Popen
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8')

app = FastAPI()

@app.get('/')</code>
<div class="hljs-pre"><pre class="hljs"><code>@app.get('/ping')
def ping(host: str):
    stdout, stderr = execute_ping(host)
    return {'status': 'completed', 'stdout': stdout, 'stderr': stderr}</code></pre></div>