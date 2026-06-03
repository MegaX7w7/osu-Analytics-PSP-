import os
import json
from osrparse import Replay

def calc_acc(h300, h100, h50, misses):
    total_hits = h300 + h100 + h50 + misses
    if total_hits == 0:
        return 0.0
    accuracy = (h300 * 300 + h100 * 100 + h50 * 50) / (total_hits * 300)
    return accuracy * 100

def get_last_path(config_file="config.json"):
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data.get("last_path", "")
            except json.JSONDecodeError:
                return ""
    return ""

def save_last_path(path, config_file="config.json"):
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump({"last_path": path}, f)

def save_replay_data(req_directory, replayData="replayData.json"):
    if not os.path.isdir(req_directory):
        print(f"El directorio {req_directory} no existe o su ruta es incorrecta.")
        return

    # Se inicializa como diccionario {} en lugar de lista [] para agrupar por Hash
    data_save = {}
    if os.path.exists(replayData):
        with open(replayData, "r", encoding="utf-8") as database_temp:
            try:
                data_save = json.load(database_temp)
            except json.JSONDecodeError:
                print("Los registros se encuentran vacios. Se crearan registros nuevos.")
                data_save = {}

    processed_count = 0

    for file_name in os.listdir(req_directory):
        if file_name.endswith(".osr"):
            full_path = os.path.join(req_directory, file_name)
            print(f"Procesando: {file_name}...")

            try:
                #Data Extraction (parsea los datos de la replay)
                replay = Replay.from_path(full_path)
                
                #ACC Calc (calc_acc)
                acc = calc_acc(
                    replay.count_300,
                    replay.count_100,
                    replay.count_50, 
                    replay.count_miss
                )
                
                #Naming and format: (Usuario, modo de juego, mapa, stats)
                replay_format = {
                    "Modo de juego:": replay.mode.name,
                    "Usuario:": replay.username,
                    "Stats": {
                        "300": replay.count_300,
                        "100": replay.count_100,
                        "50": replay.count_50,
                        "misses": replay.count_miss,
                        "Max Combo": replay.max_combo,
                        "Precision:": round(acc, 2),
                        "FC": replay.perfect
                    }
                }
                
                map_hash = replay.beatmap_hash
                
                #Se hace la insercion de los datos agrupando por beatmap_hash
                if map_hash not in data_save:
                    data_save[map_hash] = []
                    
                data_save[map_hash].append(replay_format)
                processed_count += 1

            except Exception as e:
                print(f"[Error de archivo] No se pudo leer el archivo {file_name} , comprueba la ruta y tipo de archivo (.osr)")
                print(f"tech:{e}")
                
    if processed_count > 0:
        #Save data en el json
        with open(replayData, "w", encoding="UTF-8") as database_temp:
            json.dump(data_save, database_temp, indent=4, ensure_ascii=False)
        print(f"Data saved. {processed_count} replays procesadas.")
    else:
        print("No se procesaron replays nuevas.")

if __name__ == "__main__":
    last_path = get_last_path()
    
    print("Ruta del directorio de replays:")
    if last_path:
        print(f"-> Presiona Enter para usar la ultima ruta: {last_path}")
        
    req_directory = input("> ").strip()
    
    if req_directory == "" and last_path != "":
        req_directory = last_path
        
    if req_directory != "":
        save_last_path(req_directory)
        save_replay_data(req_directory)
    else:
        print("Operacion cancelada. No se ingreso ruta.")