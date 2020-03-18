class Drumkit():
    def __init__ (self):
        self.top_hat = True
        self.snare = True

    def play_snare (self):
        print("bang bang ba-bang")


    def play_tophat(self):
        print("ding ding di-ding")


class DrumkitTest:
    if __name__ == "__main__":
        d = Drumkit()
    if d.snare == True:
        d.play_snare()
    d.snare = False
    d.play_tophat()
    d.play_snare()

DrumkitTest()

