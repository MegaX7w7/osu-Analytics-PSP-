class ReplayRecord:
#Formating for replay log
    def __init__(self, mode_name, username, beatmap_hash, count_300, count_100, count_50, count_miss, max_combo, perfect):
        self.mode_name = mode_name
        self.username = username
        self.beatmap_hash = beatmap_hash
        self.count_300 = count_300
        self.count_100 = count_100
        self.count_50 = count_50
        self.count_miss = count_miss
        self.max_combo = max_combo
        self.perfect = perfect
        
        self.accuracy = self._calc_acc()

    def _calc_acc(self):
        total_hits = self.count_300 + self.count_100 + self.count_50 + self.count_miss
        if total_hits == 0:
            return 0.0
        acc = (self.count_300 * 300 + self.count_100 * 100 + self.count_50 * 50) / (total_hits * 300)
        return round(acc * 100, 2)

    def to_dict(self):
        return {
            "Jugador": self.username,
            "Hash": self.beatmap_hash,
            "Stats": {
                "300": self.count_300,
                "100": self.count_100,
                "50": self.count_50,
                "Misses": self.count_miss,
                "Max_Combo": self.max_combo,
                "Precision": self.accuracy,
                "FC": self.perfect
            }
        }