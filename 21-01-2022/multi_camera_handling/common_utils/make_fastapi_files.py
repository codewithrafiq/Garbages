import os
import subprocess





def make_camara(name,port):
        try:
            os.makedirs(f'./all_camaras/{name}')
        except:
            pass
        try:
            file = open(f'./all_camaras/{name}/{name}.py', 'w')
            file.close()
        except:
            pass

        file = open(f'./all_camaras/{name}/{name}.py', 'w')
        
        file.write("from logging import debug\n")
        file.write("from fastapi import FastAPI,APIRouter\n")
        file.write("import uvicorn\n")
        file.write("import cv2\n")
        file.write("\n")
        file.write("\n")
        file.write("app = FastAPI()\n")
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("@app.get('/')\n")
        file.write("def read_frame():\n")
        file.write("\treturn {\"message\": \"Hello, World!\"}\n")
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("if __name__ == '__main__':\n")
        file.write(f"\tuvicorn.run(app, host='0.0.0.0', port={port},debug=True)\n")
        
        file.close()



def run_camara(name):
    # subprocess.call(f'start /wait python ./all_camaras/{name}/{name}.py', shell=True)
    MY_COMMAND = f'python ./all_camaras/{name}/{name}.py'
    os.system(f"gnome-terminal -e 'bash -c \"{MY_COMMAND}\" '")



