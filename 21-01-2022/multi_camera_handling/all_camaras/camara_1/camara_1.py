from logging import debug
from fastapi import FastAPI,APIRouter
import uvicorn
import cv2


app = FastAPI()



@app.get('/')
def read_frame():
	return {"message": "Hello, World!"}



if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=8888,debug=True)
