class punto():
    def __init__(self, x0=0.0, y0=0.0):
        self.x=x0
        self.y=y0
    def imprimir(self):
        print("[%.2f, %.2f]")%(self.x, self.y)
