from utils.jsonmg import JsonDatabase
from controllers.rep_controller import ReplayController

def run_app():
    print("#####osu!Analytics######")
    db = JsonDatabase()
    controller = ReplayController()
    last_path = db.get_last_path()
    
    print("Ingresa el Directorio de Replays:")
    if last_path:
        print(f"-> /// presiona Enter para usar la ultima ruta usada: {last_path}")
    req_directory = input("> ").strip()
    
    # Resolucion de ruta
    if req_directory == "" and last_path != "":
        req_directory = last_path
        
    # Ejecucion
    if req_directory != "":
        db.save_last_path(req_directory)
        controller.process_directory(req_directory)
    else:
        print("Operacion cancelada. Es necesario especificar una ruta.")

if __name__ == "__main__":
    run_app()