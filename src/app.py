import os
from flask import Flask, jsonify, send_from_directory
from utils.jsonmg import JsonDatabase
from controllers.rep_controller import ReplayController

app = Flask(__name__, static_folder='../view', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/replays', methods=['GET'])
def get_replays():
    db = JsonDatabase()
    data = db.load_database()
    return jsonify(data)

@app.route('/api/scan-default', methods=['POST'])
def scan_default_folder():
    controller = ReplayController()
    
    user_profile = os.environ.get('USERPROFILE')
    osu_replays_path = os.path.join(user_profile, "AppData", "Roaming", "osu", "exports") if user_profile else ""
    
    #(fallback) para el profesor
    base_dir = os.path.dirname(os.path.dirname(__file__))
    fallback_path = os.path.join(base_dir, "data", "exReplays")
    

    if os.path.exists(osu_replays_path) and len(os.listdir(osu_replays_path)) > 0:
        target_folder = osu_replays_path
        origen = "osu! Local"
    else:
        target_folder = fallback_path
        origen = "Carpeta exReplays"
        os.makedirs(fallback_path, exist_ok=True)

    try:
        controller.process_directory(target_folder)
        return jsonify({
            "status": "success",
            "message": f"Escaneo completado desde {origen}.",
            "path": target_folder
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    
    print("osu! Analytics...")
    app.run(debug=True, port=5000)