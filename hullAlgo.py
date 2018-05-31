class convexHull:
    def __init__(self):
        self.pointCollection = []
        self.Hull = []
    def addPoint(self,tup):
        self.pointCollection.append(tup)        
    def findSide(self,p1,p2,p3):
        x1 = p1[0]
        x2 = p2[0]
        x3 = p3[0]
        y1 = p1[1]
        y2 = p2[1]
        y3 = p3[1]
        hasil = ((y2-y1)*x3) - ((x2-x1)*y3) + (x2*y1) - (x1*y2)
        if hasil>0:
            return 1
        elif hasil<0:
            return -1
        else:
            return 0
    def jarakTitikGaris(self,p1,p2,p3):
        x1 = p1[0]
        x2 = p2[0]
        x3 = p3[0]
        y1 = p1[1]
        y2 = p2[1]
        y3 = p3[1]
        hasil = ((y2-y1)*x3) - ((x2-x1)*y3) + (x2*y1) - (x1*y2)
        return abs(hasil)
    def __quickHull(self,sideNow,p1,p2):
        n  = len(self.pointCollection)
        idxMax = -1
        maxJarak = 0
        #mencari titik terjauh dari garis dengan side yang sama
        for idx in range(0,n):
            panjang = self.jarakTitikGaris(p1,p2,self.pointCollection[idx])
            if self.findSide(p1,p2,self.pointCollection[idx]) ==sideNow and panjang>maxJarak:
                idxMax = idx
                maxJarak = panjang
        if idxMax ==-1: #basecase ya kalo sudah gak ada lagi titik dengan side yang sama
            self.Hull.append((p1,p2))
            return 0
        else: # lakukan qucikhull lagi 
            self.__quickHull(-1*self.findSide(self.pointCollection[idxMax],p1,p2),self.pointCollection[idxMax],p1)
            self.__quickHull(-1*self.findSide(self.pointCollection[idxMax],p2,p1),self.pointCollection[idxMax],p2)
            return 0

    def mulaiHull(self):
        #Cari max x i dan min x i
        n  = len(self.pointCollection)
        if n<2:
            return -1
        
        #mencari titik paling atas dan paling bawah
        idxMax = 0
        idxMin = 0
        for i in range(1,n):
            if self.pointCollection[i][1]> self.pointCollection[idxMax][1]:
                idxMax = i
            if self.pointCollection[i][1]< self.pointCollection[idxMin][1]:
                idxMin = i

        #mulai dnc hullnya
        self.__quickHull(-1,self.pointCollection[idxMin],self.pointCollection[idxMax])
        self.__quickHull(1,self.pointCollection[idxMin],self.pointCollection[idxMax])