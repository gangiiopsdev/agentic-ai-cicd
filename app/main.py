from fastapi import FastAPI
import subprocess
import shlex
genesis = 'ping -c 4 ' + shlex.quote(host)
result = subprocess.run(genesis, shell=True, capture_output=True, text=True)
return {'status': result.stdout}