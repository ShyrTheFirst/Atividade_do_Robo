import pygame, sys

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode([largura_tela, altura_tela])
pygame.display.set_caption("Salve o Robô")
frames = pygame.time.Clock()
preto_fundo = (0,0,0)
branco_personagem = (255,255,255)
verde_ganhou = (120,218,122)
vermelho_perdeu = (193,30,30)
preto_obstaculo = (10,10,10)


class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'personagem.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.speed = 2
        self.dir = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def entrada(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.dir.y = -1              
        elif keys[pygame.K_DOWN]:
            self.dir.y = 1
        else:
            self.dir.y = 0

        if keys[pygame.K_RIGHT]:
            self.dir.x = 1               

        elif keys[pygame.K_LEFT]:
            self.dir.x = -1
        else:
            self.dir.x = 0

    def update(self):
        self.entrada()
        self.pos.x += self.dir.x * self.speed
        self.rect.x = round(self.pos.x)
        self.pos.y += self.dir.y * self.speed
        self.rect.y = round(self.pos.y)
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > largura_tela - 49:
            self.rect.x = largura_tela - 50
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > altura_tela - 49:
            self.rect.y = altura_tela - 50
            

obstaculo = pygame.Rect(20,20,50,50)
    
      
personagem = Jogador()
grupo_personagem = pygame.sprite.Group()
grupo_personagem.add(personagem)
playing = True

while playing:
    tela.fill(preto_fundo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    grupo_personagem.draw(tela)
    personagem.update()
    pygame.draw.rect(tela,branco_personagem, obstaculo)
    pygame.display.update()


        

    frames.tick(60)
    
