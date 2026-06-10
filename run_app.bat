
echo Iniciando Osu!Analytics
call .venv\Scripts\activate.bat
echo "Running..."
echo "running localhost:5000"
start http://localhost:5000
echo "Server Start."
python src\app.py
pause