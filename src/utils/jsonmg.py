import os
import json

class JsonDatabase:
    
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.data_folder = os.path.join(base_dir, "data")
        self.replays_folder = os.path.join(self.data_folder, "replays")
        
        self.config_path = os.path.join(self.data_folder, "config.json")
        self.db_path = os.path.join(self.replays_folder, "replayData.json")

    def get_last_path(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                try:
                    return json.load(f).get("last_path", "")
                except json.JSONDecodeError:
                    return ""
        return ""

    def save_last_path(self, path):
        os.makedirs(self.data_folder, exist_ok=True)
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump({"last_path": path}, f)

    def load_database(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    print("Base de datos vacia o corrupta. Se inicializara una nueva.")
                    return {}
        return {}

    def save_database(self, data_dict):
        os.makedirs(self.replays_folder, exist_ok=True)
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(data_dict, f, indent=4, ensure_ascii=False)