class DrumKit:

    def __init__(self):
        self.top_hat = True
        self.snare = True

    def play_snare(self):
        print("bang bang ba-bang")
    def play_tophat(self):
        print("ding ding di-ding")

class DrumKitTest:
    d = DrumKit()
    d.play_snare()
    d.play_tophat()
    d.snare = False
    if d.snare == True:
        d.play_snare()

if __name__ == "__main__":
    DrumKitTest()
