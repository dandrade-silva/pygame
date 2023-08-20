class Bouncer(pygame.sprite.Sprite): 
    def __init__(self, startpos): 
        pygame.sprite.Sprite.__init__(self) 
        #direcao: 1=direita, -1=esquerda 
        self.direction = 1 
        #carrega a imagem e a posiciona na tela 
        self.image, self.rect = load_image("images/raichu.png") 
        self.rect.centerx = startpos[0] 
        self.rect.centery = startpos[1] 
        
    
    def update(self): 
        #multiplicamos x por 3 pro bouncer mover-se #um pouco mais rápido! 
        self.rect.move_ip((self.direction*3,0)) 
        #se o bouncer atingir os limites da tela, #invertemos a sua direcao 
        if self.rect.left < 0: 
            self.direction = 1 
        elif self.rect.right > width: 
            self.direction = -1

Read more: http://www.linhadecodigo.com.br/artigo/503/introducao-ao-pygame.aspx#ixzz8Ay4SzmEC