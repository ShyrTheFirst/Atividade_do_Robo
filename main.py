import pygame, sys

####################INICIALIZACAO##########################################
pygame.init()
largura_tela = 500
altura_tela = 500
tela = pygame.display.set_mode([largura_tela, altura_tela])
pygame.display.set_caption("Salve o Robô")
frames = pygame.time.Clock()

####################CORES##################################################
preto_fundo = (0,0,0)
branco_personagem = (255,255,255)
verde_ganhou = (120,218,122)
vermelho_perdeu = (193,30,30)
preto_obstaculo = (10,10,10)

####################GRUPOS#################################################
grupo_personagem = pygame.sprite.Group()
grupo_controles = pygame.sprite.Group()
grupo_obstaculos = pygame.sprite.Group()

####################IMAGENS################################################
start_grid = pygame.image.load(r'start.png').convert_alpha()
grid = pygame.image.load(r'grid.png').convert_alpha()
fim_jogo = pygame.image.load(r'fim.png').convert_alpha()
nao = pygame.image.load(r'nao.png').convert_alpha()
sim = pygame.image.load(r'sim.png').convert_alpha()
reinicio = pygame.image.load(r'reinicio.png').convert_alpha()

#######################VARIAVEIS########################
start = True
playing = False
posmouse = pygame.mouse.get_pos()

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'personagem.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.old_rect = self.rect.copy()
        self.rect.x = 75
        self.rect.y = 50
        self.dir = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.obstaculos = grupo_obstaculos
        self.direita = direita
        self.esquerda = esquerda
        self.cima = cima
        self.baixo = baixo
            

    def colisao(self,direcao):
            collision_sprites = pygame.sprite.spritecollide(self,self.obstaculos,False)
            if collision_sprites:
                if direcao == 'horizontal':
                    for sprite in collision_sprites:
                        # colisão na direita
                        if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:                                                       
                            self.rect.right = sprite.rect.left
                            self.pos.x = self.rect.x

                        # colisão na esquerda
                        if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:                           
                            self.rect.left = sprite.rect.right
                            self.pos.x = self.rect.x

                if direcao == 'vertical':
                    for sprite in collision_sprites:
                        # colisão em baixo
                        if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                            self.rect.bottom = sprite.rect.top
                            self.pos.y = self.rect.y

                        # colisão em cima
                        if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:                            
                            self.rect.top = sprite.rect.bottom
                            self.pos.y = self.rect.y

    def update(self):
        self.old_rect = self.rect.copy()
        #self.colisao('horizontal')
        #self.colisao('vertical')



class Obstaculo(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load(r'obstaculo.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.old_rect = self.rect.copy()
        self.rect.x, self.rect.y = pos
        self.old_rect = self.rect.copy()

################CONTROLES###########################################################
class Direita(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'direita.png').convert_alpha() # -> +x
        self.rect = self.image.get_rect()
        self.rect.x = 275
        self.rect.y = 425

class Esquerda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'esquerda.png').convert_alpha() #<- -x
        self.rect = self.image.get_rect()
        self.rect.x = 175
        self.rect.y = 425

class Cima(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'cima.png').convert_alpha() #-y
        self.rect = self.image.get_rect()
        self.rect.x = 225
        self.rect.y = 400

class Baixo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'baixo.png').convert_alpha() #+y
        self.rect = self.image.get_rect()
        self.rect.x = 225
        self.rect.y = 450
            
    
      
#############criando controles################
direita = Direita()
esquerda = Esquerda()
cima = Cima()
baixo = Baixo()
grupo_controles.add(direita)
grupo_controles.add(esquerda)
grupo_controles.add(cima)
grupo_controles.add(baixo)

############criando personagem#################
personagem = Jogador()
grupo_personagem.add(personagem)

############criando obstaculos#################
pos_obstaculos = [(75,150),(75,350),(125,100),(125,250),(175,150),(175,200),(175,300),(225,150),(275,100),(275,150),(275,200),(275,300),(275,350),(325,200),(425,100),(425,300)]
for i in range(len(pos_obstaculos)):
    obstaculo = Obstaculo(pos_obstaculos[i])
    grupo_obstaculos.add(obstaculo)
#obstaculo = Obstaculo(75,150)
#grupo_obstaculos.add(obstaculo)

while start:
    tela.blit(grid,(75,50))
    tela.blit(start_grid,(0,0))
    grupo_personagem.draw(tela)
    grupo_obstaculos.draw(tela)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = False
            playing = True
        elif event.type == pygame.KEYDOWN:
            start = False
            playing = True

while playing:
    tela.fill(preto_fundo)

    #######permite que o jogo feche ao clicar no X########
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu_jogo = True
                while menu_jogo:
                    tela.blit(reinicio,(0,0))
                    tela.blit(nao,(300,300))
                    tela.blit(sim,(150,300))
                    nao_rect = pygame.Rect(300,300,50,50)
                    sim_rect = pygame.Rect(150,300,50,50)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            posmouse = pygame.mouse.get_pos()
                            if nao_rect.collidepoint(posmouse):
                                menu_jogo = False
                            if sim_rect.collidepoint(posmouse):
                                restart = True
                                personagem.rect.x = 75
                                personagem.rect.y = 50
                                tela.fill(preto_fundo)
                                pygame.display.update()
                                while restart:
                                    tela.blit(grid,(75,50))
                                    tela.blit(start_grid,(0,0))
                                    grupo_personagem.draw(tela)
                                    grupo_obstaculos.draw(tela)
                                    pygame.display.update()
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            restart = False
                                        elif event.type == pygame.KEYDOWN:
                                            restart = False

                                
                                menu_jogo = False
                            
                    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            posmouse = pygame.mouse.get_pos()
            if personagem.cima.rect.collidepoint(posmouse):
                personagem.rect.y += -50
            elif personagem.baixo.rect.collidepoint(posmouse):
                personagem.rect.y += 50
            elif personagem.esquerda.rect.collidepoint(posmouse):
                personagem.rect.x += -50
            elif personagem.direita.rect.collidepoint(posmouse):
                personagem.rect.x += 50

            if personagem.rect.x < 75:
                personagem.rect.x = 75
            elif personagem.rect.x > largura_tela - 125:
                personagem.rect.x = largura_tela - 125
            if personagem.rect.y < 50:
                personagem.rect.y = 50
            elif personagem.rect.y > altura_tela - 150:
                personagem.rect.y = altura_tela - 150
            elif personagem.rect.x == 125 and personagem.rect.y == 150:
                try_again = True
                while try_again:
                    tela.blit(fim_jogo,(0,0))
                    tela.blit(nao,(300,300))
                    tela.blit(sim,(150,300))
                    nao_rect = pygame.Rect(300,300,50,50)
                    sim_rect = pygame.Rect(150,300,50,50)
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            posmouse = pygame.mouse.get_pos()
                            if nao_rect.collidepoint(posmouse):
                                pygame.quit()
                                sys.exit()
                            if sim_rect.collidepoint(posmouse):
                                personagem.rect.x = 75
                                personagem.rect.y = 50
                                tela.fill(preto_fundo)
                                pygame.display.update()
                                try_again = False
                    pygame.display.update()
                
            personagem.colisao('horizontal')
            personagem.colisao('vertical')
                
        else:
            posmouse = (0,0)


    #######desenhando os sprites#######
    grupo_personagem.draw(tela)
    grupo_controles.draw(tela)
    grupo_obstaculos.draw(tela)
    personagem.update()

    ############atualizando a tela#################
    pygame.display.update()


        

    frames.tick(60)




