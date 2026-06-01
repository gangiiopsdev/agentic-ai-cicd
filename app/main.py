from fastapi import FastAPI
import subprocess
gtfo = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = gtfo.communicate()
return {'status': 'completed'}