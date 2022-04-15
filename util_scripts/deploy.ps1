python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install -U pip
python -m pip install -r requirements.txt
$env:FLASK_APP = "main"
flask run