from osrparse import Replay


rep_file = "Megaaazzz playing succducc - me & u (Alonevpk) [thiinggs] (2026-04-25_19-27).osr"


replay = Replay.from_path(rep_file)

print("Replay Data:")
print(f"Modo de juego: {replay.mode}")
print(f"Versión del juego: {replay.game_version}")
print(f"Jugador: {replay.username}")
print(f"Hash del mapa: {replay.beatmap_hash}")
print("--- MÉTRICAS ---")
print(f"300s: {replay.count_300}")
print(f"100s: {replay.count_100}")
print(f"50s: {replay.count_50}")
print(f"Misses: {replay.count_miss}")
print(f"Max Combo: {replay.max_combo}")
print(f"Perfect (FC): {replay.perfect}")
print(f"Mods: {replay.mods}")