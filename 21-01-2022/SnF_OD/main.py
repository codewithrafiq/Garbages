from logging import debug
from fastapi import FastAPI,APIRouter,Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,StreamingResponse
import single_cv2_for_single_camera
from single_threaded_streaming import SingleThreadedStreamingYolov3, gen_frames
from multithreaded_streaming import threadBoth
from multithreaded_streaming_edit import single_threaded_for_single_camera



app = FastAPI()
router = APIRouter()
templates = Jinja2Templates(directory="templates")



@router.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})





@router.get('/video_fead1', response_class=HTMLResponse)
def video_fead1(request: Request):
    rtsp = "rtsp://admin:abc12345@119.148.38.194:554/Streaming/Channels/0301"
    frams = single_cv2_for_single_camera.camera_1(rtsp)
    return  StreamingResponse(frams, media_type='multipart/x-mixed-replace; boundary=frame')

@router.get('/video_fead2', response_class=HTMLResponse)
def video_fead2(request: Request):
    rtsp = "rtsp://admin:abc12345@119.148.38.194:554/Streaming/Channels/1401"
    frams = single_cv2_for_single_camera.camera_2(rtsp)
    return  StreamingResponse(frams, media_type='multipart/x-mixed-replace; boundary=frame')
 
 
@router.get('/video_fead3', response_class=HTMLResponse)
def video_fead3(request: Request):
    rtsp = "rtsp://admin:abc12345@119.148.38.194:554/Streaming/Channels/0201"
    frams = single_cv2_for_single_camera.camera_3(rtsp)
    return  StreamingResponse(frams, media_type='multipart/x-mixed-replace; boundary=frame')
 


app.include_router(router)
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000,debug=True)