# How to run this

## Requirments
checked this configuaration on Rasberry PI and Jetson Nano
- Python>=3.8
- opencv-python >= 4.5.4.60

### Configuartion Details

```python
"save_data_in_edge_device": True,         # do you want to store the image data in edge device?
"save_path": os.getcwd(),                 # path where data will be saved. Default data will saved in code directory           
"in_camera_id": 0,                        # enter camera Id 
"out_camera_id": 1,                       # exit camera Id 
"camera_resolution": (640, 480),          # camera resolution for capture images. for 720p: (1280, 720) 
"web_server_address": "http://20.212.16.129/api/perform-attendances",
"headers": {
		'Accept': 'application/json',
		'Authorization': 'Bearer CPXQWLgEnfIEseMnLSTvw1FyjmlhrfSTvLaDT842', # Monitor Token for the company
		'Content-Type': 'application/json'
}
```

Note: Token for Authorization is basically generated token for monitor by super-admin


## Auto Start Python Script on Boot
Steps is given below,
- Make a Launcher Sript
- Make It Executable
- Add Logs Directory


#### Step 1: Make a Launcher Sript
Let's create the shell script!
This bash file needs for startup running so that it will run automatically if it restarted.

create bash file in terminal
```bash
touch RUN.sh
```


Then, edit with following commands in RUN.sh
```bash
cd /
cd /home/intisar/Hasan/Deploy-edge-device   # path where the code exist
sudo python3 Main.py 
cd /
```

Note: in base file, opencv may not find while the python file running in bash. So, we need to append 
opencv path to program.

Find out the opencv path,
```bash
python3
>>> import cv2
>>> cv2.data
```

Add this path in "Main.py" file
```python
import sys
sys.path.append('/home/intisar/.local/lib/python3.6/site-packages')
```
#### Step 2: Make It Executable
We need to make the launcher script an executable, which we do with this command,
```bash
chmod 755 RUN.sh
```

Now test it, by typing in:
```bash
sh RUN.sh
```

#### Step 3: Add Logs Directory
we need to make a directory for the any errors in crontab to go.

Create a logs directory:
```
mkdir logs
```
for example,
```
/home/intisar/Hasan/Deploy-edge-device/logs
```

#### Step 4: Add to Your Crontab
crontab is a background (daemon) process that lets you execute scripts at specific times. It's essential to Python and Raspberry Pi/Jetson Nano. The details are confusing, as is often the case with Linux. Once I got the hang of the format, I've found it to be incredibly easy to use.
Type in:
```bash
sudo crontab -e
```
This will brings up a crontab window.

Now, enter the line:
```bash
@reboot sh /home/intisar/Hasan/Deploy-edge-device/RUN.sh >/home/intisar/Hasan/Deploy-edge-device/logs/cronlog 2>&1
```




