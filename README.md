# SETUP
1. Run `python -m venv .` in the root directory NOT IN `/src` FOLDER. 
You should have the following folder structure after running the above, if not re-clone the repo.
. <- root directory, name is preferably `VoiceAssistant/` but can be anything.  
├── Include  
├── Lib  
├── Scripts  
├── src/  
│   └── main.py  
├── .gitignore  
├── pyvenv.cfg  
├── README.md  
└── requirements.txt  
2. Run `. Scripts/activate` in the root directory. (if this fails re-clone repo and try again)
3. Run `pip install -r requirements.txt` (technically the only thing that needs to be ran but you should use the venv stuff above to avoid conflicts.)
## Adding libraries
ALWAYS run `pip freeze > requirements.txt` if you ever use `pip install`.
# Starting the script
Run `python src/main.py` (make sure venv is activated with `. Scripts/activate`)
# Goal
Make an AI voice assistant with multi input/output relative to the input location.
# Future Goals 
include task specific requests acting as different "personalities" to change speed, voice, and style of reply according to the task, as well as visual inputs/outputs for varied tasks.