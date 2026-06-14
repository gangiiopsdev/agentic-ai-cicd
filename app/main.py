from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in '.,_:- ') 
app = FastAPI()
@app.get('/ping')
def ping(host: str):  
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', '-c', '1'] + sanitized_host.split(), check=True, shell=False)  
    return {'status': 'completed'}