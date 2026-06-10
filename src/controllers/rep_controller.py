import os
import re
from osrparse import Replay
from models.rep_format import ReplayRecord
from utils.jsonmg import JsonDatabase

class ReplayController:
    
    def __init__(self):
        self.db = JsonDatabase()
        self.regex_pattern = re.compile(r"^(.+?) playing (.+) \[([^\]]+)\] \(([\d-]+_[\d-]+)\)(?: \(\d+\))?\.osr$")
    

    def process_directory(self, directory_path):
        if not os.path.isdir(directory_path):
            print(f"[Error] El directorio {directory_path} no es válido.")
            return

        data_save = self.db.load_database()
        processed_count = 0
        ignored_count = 0

        for file_name in os.listdir(directory_path):
            if file_name.endswith(".osr"):
                full_path = os.path.join(directory_path, file_name)
                coincidence = self.regex_pattern.match(file_name)

                if not coincidence:
                    print(f"[Aviso] {file_name} ignorado. Formato de nombre no estándar.")
                    continue

                try:
                    date_time = coincidence.group(4)
                    date, time = date_time.split("_")
                    time_form = time.replace("-", ":")
                    user = coincidence.group(1)

                    replay = Replay.from_path(full_path)
                    
                    record = ReplayRecord(
                        mode_name=replay.mode.name,
                        username=user,
                        beatmap_hash=replay.beatmap_hash,
                        count_300=replay.count_300,
                        count_100=replay.count_100,
                        count_50=replay.count_50,
                        count_miss=replay.count_miss,
                        max_combo=replay.max_combo,
                        perfect=replay.perfect
                    )

                    map_hash = record.beatmap_hash
                    
                    if map_hash not in data_save:
                        data_save[map_hash] = []

                    is_duplicate = False
                    for exist_replay in data_save[map_hash]:
                        if (exist_replay.get("date") == date and 
                            exist_replay.get("time") == time_form and 
                            exist_replay.get("user") == user):
                            is_duplicate = True
                            break

                    if is_duplicate:
                        ignored_count += 1
                        continue

                    new_dict = record.to_dict()
                    new_dict["date"] = date
                    new_dict["time"] = time_form
                    new_dict["Mapa_Info"] = coincidence.group(2).strip()
                    new_dict["Dificultad"] = coincidence.group(3)

                    data_save[map_hash].append(new_dict)
                    processed_count += 1
                    print(f"[Éxito] {file_name} procesado.")

                except Exception as e:
                    print(f"[Fallo] No se pudo procesar {file_name}. Detalle: {e}")

        if processed_count > 0:
            self.db.save_database(data_save)
            print(f"\nResumen: {processed_count} agregadas | {ignored_count} duplicados ignorados.")
        else:
            print(f"\nSin cambios. Se encontraron {ignored_count} archivos duplicados.")