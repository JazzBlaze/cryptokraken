python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install -U pip
python -m pip install -r requirements.txt
$env:FLASK_APP = "main"
Start-Process "http://127.0.0.1:5000/"
flask run
