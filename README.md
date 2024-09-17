# SETUP
1. Run `python -m venv .` in the root directory NOT IN `/src` FOLDER. 
2. Run `. Scripts/activate` in the root directory. (if this fails re-clone repo and try again)
3. Run `pip install -r requirements.txt` (technically the only thing that needs to be ran but you should use the venv stuff above.)
## Adding libraries
ALWAYS run `pip freeze > requirements.txt` if you ever use `pip install`.
# Goal
Make an AI voice assistant with multi input/output relative to the input location.
# Future Goals 
include task specific requests acting as different "personalities" to change speed, voice, and style of reply according to the task, as well as visual inputs/outputs for varied tasks.