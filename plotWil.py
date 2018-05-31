import matplotlib.pyplot as plt
class memPlotHull:
    
    def __init__(self):
        self.notHull = []
        self.pairHull = []    
    def addPairHull(self,pair):
        #pair as tuple (x,y)
        self.pairHull.append(pair)
    def addNotHull(self,titik):
        #titik as tuple of tuple(x,y)
        self.notHull.append(titik)
    def showHull(self):
        nNh = len(self.notHull)
        nPh = len(self.pairHull)
        #masukan titik  not hull
        for i in range(0,nNh):
            plt.plot(self.notHull[i][0],self.notHull[i][1],'ro')
        #buat garis
        for i in range(0,nPh):
            p1 = self.pairHull[i][0]
            p2 = self.pairHull[i][1]
            plt.plot([p1[0],p2[0]],[p1[1],p2[1]],'r-')
            plt.plot([p1[0],p2[0]],[p1[1],p2[1]],'bo')
        plt.grid(True)
        plt.show()