from Game2048 import Game2048
from Joc import Joc

if __name__ == "__main__":
    app = Joc()
    app.bind_all('<Key>', app.moves)
    app.wm_title("2048")
    app.minsize(430, 470)
    app.mainloop()
    # start = Game2048()
