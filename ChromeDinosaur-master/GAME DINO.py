import pygame
import os

pygame.init()

#Konstanta global
LAYAR_TINGGI = 600
LAYAR_LEBAR = 1100
LAYAR = pygame.display.set_mode((LAYAR_LEBAR,LAYAR_TINGGI))

LARI = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
        pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]

LOMPAT = [pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))]

NUNDUK = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

KAKTUS_KECIL = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

KAKTUS_BESAR = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BURUNG = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
          pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

AWAN = [pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))]

BG = [pygame.image.load(os.path.join("Assets/Other", "Track.png"))]

class Dinosaurus:
    POSISI_X = 80
    POSISI_Y = 310
    POSISI_Y_NUNDUK = 340

    def __init__(self):
        self.nunduk_gmbr = NUNDUK
        self.lari_gmbr = LARI
        self.lompat_gmbr = LOMPAT

        self.dino_nunduk = False
        self.dino_lari = True
        self.dino_lompat = False

        self.index_langkah = 0
        self.gambar = self.lari_gmbr[0]
        self.kotak_dino = self.gambar.get_rect()
        self.kotak_dino.x = self.POSISI_X
        self.kotak_dino.y = self.POSISI_Y

    def update(self, userInput):
        if self.dino_nunduk:
            self.nunduk()
        if self.dino_lari:
            self.lari()
        if self.dino_lompat:
            self.lompat()

        if self.index_langkah >= 10:
            self.index_langkah = 0
        
        if userInput[pygame.K_UP] and not self.dino_lompat:
            self.dino_nunduk = False
            self.dino_lari = False
            self.dino_lompat = True
        elif userInput[pygame.K_DOWN] and not self.dino_lompat:
            self.dino_nunduk = True
            self.dino_lari = False
            self.dino_lompat = False
        elif not (self.dino_lompat or userInput[pygame.K_DOWN]):
            self.dino_nunduk = False
            self.dino_lari = True
            self.dino_lompat = False
        
    def nunduk(self):
        self.gambar = self.nunduk_gmbr[self.index_langkah // 5]
        self.kotak_dino = self.gambar.get_rect()
        self.kotak_dino.x = self.POSISI_X
        self.kotak_dino.y = self.POSISI_Y_NUNDUK
        self.index_langkah += 1

    def lari(self):
        self.gambar = self.lari_gmbr[self.index_langkah // 5]
        self.kotak_dino = self.gambar.get_rect()
        self.kotak_dino.x = self.POSISI_X
        self.kotak_dino.y = self.POSISI_Y
        self.index_langkah += 1

    def lompat(self):
        pass

    def draw(self, LAYAR):
        LAYAR.blit(self.gambar, (self.kotak_dino.x, self.kotak_dino.y))

#asdsasd
def main():
    lari = True
    waktu = pygame.time.Clock()
    pemain = Dinosaurus()

    while lari:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lari = False
        
        LAYAR.fill((255,255,255))
        userInput = pygame.key.get_pressed()
    
        pemain.draw (LAYAR)
        pemain.update (userInput)

        waktu.tick(30)
        pygame.display.update()
    

main()