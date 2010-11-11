class HANOI():

    def __init__(self, n, src_Tow):
        self.kule = { 1 : [], 2 : [], 3 : [] }
        while n :
            self.kule[src_Tow].append(n)
            n -= 1
        print "Kaynak Kule(%d) ' un durumu : %s" %(src_Tow, self.kule[src_Tow])

    def hatali(self, src_n, dest_n):
        if src_n == dest_n:
            print "Lutfen kaynak kule ile hedef kule icin farkli deger giriniz :) \n"+\
                    "!! siz Kaynak kule : %d = hedef kule : %d degeri girdiniz !! :))" %(src_n, dest_n)
            return False
        return True

    def hanoitow(self, n, src_Tow, dest_Tow):
        if n == 1:
            self.kule[dest_Tow].append(self.kule[src_Tow].pop())
            print "Disk(%d) =>> kule(%d) den kule(%d) tasindi :)" \
                    % (self.kule[dest_Tow][len(self.kule[dest_Tow])-1],src_Tow, dest_Tow)
            print "Kule(%d) 'un durumu : %s" %(dest_Tow, self.kule[dest_Tow])
            return
            
        temp_Tow = 6 - src_Tow - dest_Tow 
        self.hanoitow(n-1, src_Tow, temp_Tow)
        self.kule[dest_Tow].append(self.kule[src_Tow].pop())
        print "Disk(%d) =>> kule(%d) den kule(%d) tasindi :)" \
                % (self.kule[dest_Tow][len(self.kule[dest_Tow])-1], src_Tow,dest_Tow)
        print "Hedef Kule(%d) 'un durumu : %s" %(dest_Tow, self.kule[dest_Tow])
        
        self.hanoitow(n-1, temp_Tow, dest_Tow)
        return
        
    def gor(self, dest_tow):
        print "Hedef Kule(%d) 'un durumu : %s" %(dest_tow, self.kule[dest_tow])
        
disc_n = input("Disk sayisi giriniz =>>  ")
source_tow = input("Kaynak kule numarasini <1-3> arasi deger giriniz =>> ")
destination_tow = input("Hedef kule numarasini <1-3> arasi deger giriniz =>> ")

hanoi = HANOI(disc_n, source_tow)
if hanoi.hatali(source_tow, destination_tow) :
    hanoi.gor(destination_tow)
    hanoi.hanoitow(disc_n, source_tow, destination_tow)
    hanoi.gor(destination_tow)
