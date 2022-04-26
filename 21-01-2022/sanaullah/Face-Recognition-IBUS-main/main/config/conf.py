import os
import sys
def get_edge_device_config():
    conf = {
			"detector": "mtcnn",
            "save_data_in_edge_device": True,
			"save_path": os.getcwd(),
			"in_camera_id": 0,
			"out_camera_id": 1,
			"camera_resolution": (640, 480), #(1280, 720),
			"web_server_address": "http://20.212.16.129/api/perform-attendances",
			"headers": {
					'Accept': 'application/json',
					'Authorization': 'Bearer CPXQWLgEnfIEseMnLSTvw1FyjmlhrfSTvLaDT842',
					'Content-Type': 'application/json'
			}
	}
    return conf 
