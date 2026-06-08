from pygame import *
import sys

# --- INICIALIZAÇÃO DO PYGAME ----
init()
screen = display.set_mode((1280, 720))
display.set_caption("Tutorial")
clock = time.Clock()

#mapa = image.load("Atividade_12/Cenario/masmorra.png")
#mapa = transform.scale(mapa, (1280, 720))  # Redimensiona o mapa para preencher a tela
mapa_2 = image.load("Cenario/masmorra.png")
pos_x = 0
pos_y = 0

mapa_3 = image.load("sprites_separados/sprite_4.png")
mapa_4 = image.load("spritesheet.png")
mapa_5 = image.load("sprites_separados/sprite_24.png")
mapa_6 = image.load("imagens_masmorra/parede_2.png")
mapa_7 = image.load("imagens_masmorra/porta.png")
mapa_8 = image.load("imagens_masmorra/teto.png")
mapa_9 = image.load("imagens_masmorra/parede_esquerda.png")

# Variáveis para animação do personagem
curr_frame = 0
anim_timer = 0
zant = image.load("swordsman_lvl3/with_shadow/swordsman_lvl3_walk_with_shadow.png")
zant_x, zant_y = 600, 500  # CORRIGIDO: Posição inicial dentro do mapa
vel_zant_x = 6  # AJUSTADO: Aumentado de 4 para movimento mais rápido
zant_olhando_direita = True
zant_olhando_cima = True
vel_zant_y = 6  # AJUSTADO: Aumentado de 4 para movimento mais rápido


# Variáveis para animação da vela tipo A
curr_frame_vela = 0
anim_timer_vela = 0
vela = []
for i in range(4):
    vela.append(image.load(f"Cenario/candleA_0{i+1}.png"))

# Variáveis para animação da vela tipo B
curr_frame_vela_b = 0
anim_timer_vela_b = 0
vela_b = []
for i in range(4):
    vela_b.append(image.load(f"Cenario/candleB_0{i+1}.png"))

# Variáveis dos espinhos
curr_frame_spike = 0
anim_timer_spike = 0
spike = []
#for i in range(5):
    #spike.append(image.load(f"Atividade_12/Cenario/spike_0{i+1}.png"))

mapa_joguinho = [
    "XXXXXXXXXXXXXX",
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXXXXXXXXXXX", 
  "XXXXBXXXXXXXXX", 
  "GGGGGGGAAGGGGG", 
  "TTTTTTTPPTTTTT", 
  "TTTTTTTPPTTTTT",]

# --- FUNÇÃO DE COLISÃO ---
def verificar_colisao(zant_x, zant_y, paredes_rects):
    """
    Verifica se o personagem colidiu com alguma parede.
    Retorna True se houver colisão, False caso contrário.
    """
    zant_rect = Rect(zant_x, zant_y, 64, 64)  # Rect do personagem (64x64)
    
    for parede_rect in paredes_rects:
        if zant_rect.colliderect(parede_rect):
            return True
    return False

# --- LOOP PRINCIPAL ---
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    
    clock.tick(60)  # Controla a taxa de atualização para 60 FPS
    dt = clock.get_time()

    anim_timer_vela += dt
    anim_timer_sec = anim_timer_vela / 1000

    if anim_timer_sec >= 0.25:  # Tempo para mudar o frame da vela
        curr_frame_vela = curr_frame_vela + 1 # ou curr_frame_vela += 1
        if curr_frame_vela >= len(vela)-1:
            curr_frame_vela = 0
        anim_timer_vela = 0

    # Animação da vela tipo B
    anim_timer_vela_b += dt
    anim_timer_sec_b = anim_timer_vela_b / 1000

    if anim_timer_sec_b >= 0.25: # Tempo para mudar o frame da vela
        curr_frame_vela_b += 1
        if curr_frame_vela_b >= len(vela_b):
            curr_frame_vela_b = 0
        anim_timer_vela_b = 0

    # Animação dos espinhos
    anim_timer_spike += dt
    anim_timer_sec_spike = anim_timer_spike / 1000

    #if anim_timer_sec_spike >= 0.25:
    #    curr_frame_spike += 1
    #    if curr_frame_spike >= len(spike):
    #        curr_frame_spike = 0
    #    anim_timer_spike = 0
    
    
    old_pos_x = pos_x
    old_pos_y = pos_y

    keys = key.get_pressed()
    if keys[K_LEFT]:
        pos_x -= 200 * dt / 1000  # Move para a esquerda
    if keys[K_RIGHT]:
        pos_x += 200 * dt / 1000  # Move para a direita
    if keys[K_UP]:
        pos_y -= 200 * dt / 1000  # Move para cima
    if keys[K_DOWN]:
        pos_y += 200 * dt / 1000  # Move para baixo

    # --- LOGICA DE MOVIMENTAÇÃO ---

    # 1. Inicializa as velocidades como 0 a cada frame (para ele parar se soltar as teclas)
    velocidade_atual_zant_x = 0
    velocidade_atual_zant_y = 0
    zant_andando = False

    # 2. Verifica o Eixo X (Horizontal)
    if keys[K_d]: # Direita
        velocidade_atual_zant_x = vel_zant_x
        zant_olhando_direita = True
        zant_andando = True
    elif keys[K_a]: # Esquerda
        velocidade_atual_zant_x = -vel_zant_x
        zant_olhando_direita = False
        zant_andando = True

    # 3. Verifica o Eixo Y (Vertical)
    if keys[K_w]: # Cima (No Pygame, para cima é NEGATIVO)
        velocidade_atual_zant_y = -vel_zant_y
        zant_andando = True
    elif keys[K_s]: # Baixo (No Pygame, para baixo é POSITIVO)
        velocidade_atual_zant_y = vel_zant_y
        zant_andando = True

    # --- RENDERIZAÇÃO (PARA CRIAR LISTA DE RECTS) ---
    # Primeiro, vamos criar a lista de coordenadas e paredes que será usada
    
    coordenadas = [
    # Parte inferior (y=600, 610)
    (600,600), (610,600),
    (600,610), (610,610),
    
    # Coluna direita (x=610, y=620-690)
    (610,620), (610,630), (610,640), (610,650),
    (610,660), (610,670), (610,680), (610,690),
    
    # Linha horizontal superior (y=590)
    (610,590), (620,590), (630,590), (640,590),
    
    # Linha y=580
    (600,580), (610,580), (620,580), (630,580),
    (590,580),
    
    # Linha y=570
    (590,570), (600,570), (610,570), (620,570),
    (630,570), (640,570),
    
    # Linha y=560 (a mais longa)
    (640,560), (650,560), (660,560), (670,560),
    (680,560), (690,560), (700,560), (710,560),
    (720,560), (730,560), (740,560), (750,560),
    (760,560), (770,560), (780,560), (790,560),
    (800,560), (810,560), (820,560), (830,560),
    (840,560), (850,560), (860,560), (870,560),
    (880,560), (890,560), (900,560),
    (590,560), (600,560), (610,560), (620,560),
    (630,560),
    
    # Linha y=550
    (590,550), (600,550), (610,550), (620,550),
    (630,550), (640,550), (650,550), (660,550),
    (670,550), (680,550), (690,550), (700,550),
    (710,550), (720,550), (730,550), (740,550),
    (750,550), (760,550), (770,550), (780,550),
    (790,550), (800,550), (810,550), (820,550),
    (830,550), (840,550), (850,550), (860,550),
    (870,550), (880,550), (890,550), (900,550),
    ]

    # Pontos específicos
    pontos_especiais = [
    (630, 600), (630, 610),
    (630, 650), (630, 660)
    ]

    # Teto da parte de cima 1
    teto_cima_1 = [
    (700, 200, 100),
    (740, 200, 100),
    (780, 200, 100),
    (820, 55, 100),   # Guina
    (915, 200, 100),
    (955, 200, 100),
    (995, 200, 100),
    (1035, 200, 100),
    (1055, 70, 100),
    ]

    # --- CRIANDO LISTA DE RECTS PARA COLISÃO ---
    paredes_rects = []

    # Paredes Lado Direito
    paredes_rects.append(Rect(610, 600, 47, 150))
    paredes_rects.append(Rect(610, 550, 47, 150))

    # Coluna x=590 (parede grande)
    for y in range(540, 690, 10):
        paredes_rects.append(Rect(590, y, 20, 32))

    # Coluna x=870 (parede média)
    for y in range(400, 480, 10):
        paredes_rects.append(Rect(870, y, 20, 32))

    # Coluna x=700 (paredes irregulares)
    for y in [290, 300, 310, 320, 330, 340, 350, 360, 370, 375]:
        paredes_rects.append(Rect(700, y, 20, 32))

    # Coluna x=440 (pequenas paredes)
    for y in [200, 210]:
        paredes_rects.append(Rect(390, y, 20, 32))

    # Teto parte de baixo
    for x in range(650, 870, 40):
        paredes_rects.append(Rect(x, 590, 20, 32))

    # Teto parte de cima 2
    for x in range(405, 665, 40):
        paredes_rects.append(Rect(x, 360, 20, 32))

    # Teto da parte de cima 1
    for x, y, w in teto_cima_1:
        paredes_rects.append(Rect(x, 470, 20, 32))

    # Outras blits individuais
    paredes_rects.append(Rect(447, 250, 20, 32))
    paredes_rects.append(Rect(548, 250, 20, 32))
    paredes_rects.append(Rect(680, 490, 20, 32))
    paredes_rects.append(Rect(590, 490, 20, 32))
    paredes_rects.append(Rect(915, 350, 20, 32))
    paredes_rects.append(Rect(745, 350, 20, 32))

    # Plataformas (coordenadas list)
    for x, y in coordenadas:
        paredes_rects.append(Rect(x, y, 20, 32))

    # Pontos especiais
    for x, y in pontos_especiais:
        paredes_rects.append(Rect(x, y, 20, 32))

    # Pontes
    for x in range(910, 1110, 10):
        for y in range(400, 450, 10):
            paredes_rects.append(Rect(x, y, 20, 32))

    for x in range(700, 870, 10):
        for y in range(400, 450, 10):
            paredes_rects.append(Rect(x, y, 20, 32))

    for x in range(700, 740, 10):
        for y in range(300, 390, 10):
            paredes_rects.append(Rect(x, y, 20, 32))

    for x in range(400, 700, 10):
        for y in range(300, 340, 10):
            paredes_rects.append(Rect(x, y, 20, 32))

    for x in range(400, 440, 10):
        for y in range(180, 300, 10):
            paredes_rects.append(Rect(x, y, 20, 32))

    for x in range(590, 910, 10):
        paredes_rects.append(Rect(x, 540, 20, 32))

    # Linha horizontal de cima (Y=530 até Y=400)
    for y in range(400, 540, 10):
        for x in range(870, 910, 10):
            paredes_rects.append(Rect(x, y, 20, 32))

    # --- 4. ATUALIZA A POSIÇÃO DO PERSONAGEM (COM COLISÃO) ---
    nova_zant_x = zant_x + velocidade_atual_zant_x
    nova_zant_y = zant_y + velocidade_atual_zant_y
    
    # Verifica colisão antes de atualizar a posição
    if not verificar_colisao(nova_zant_x, zant_y, paredes_rects):
        zant_x = nova_zant_x  # Permite movimento horizontal
    
    if not verificar_colisao(zant_x, nova_zant_y, paredes_rects):
        zant_y = nova_zant_y  # Permite movimento vertical

    # 5. ANIMA O PERSONAGEM
    if zant_andando:
        anim_timer += dt
        if anim_timer >= 100:  # Muda frame a cada 100ms
            curr_frame += 1
            if curr_frame >= 6:  # A animação tem 6 frames
                curr_frame = 0
            anim_timer = 0
    else:
        curr_frame = 0
    
         
        
        
    #for i in range(len(mapa_joguinho)):
     #   for j in range(len(mapa_joguinho[i])):
      #      if mapa_joguinho[i][j] == "X":
       #         screen.blit(mapa_2, (j*64, i*64),(0,0,64,64) )  # Desenha o cenário na posição 
        #    elif mapa_joguinho[i][j] == "G":
         #       screen.blit(mapa_2, (j*64, i*64),(64,0,64,64) )  # Desenha o cenário na posição 
          #  elif mapa_joguinho[i][j] == "T":
           #     screen.blit(mapa_2, (j*64, i*64),(128,0,64,64) )  # Desenha o cenário na posição 
            #elif mapa_joguinho[i][j] == "B":
             #   screen.blit(mapa_2, (j*64, i*64),(192,0,64,64) )  # Desenha o cenário na posição 
           # elif mapa_joguinho[i][j] == "A":
            #    screen.blit(mapa_2, (j*64, i*64),(256,0,64,64) )  # Desenha o cenário na posição 
          #  elif mapa_joguinho[i][j] == "P":
           #     screen.blit(mapa_2, (j*64, i*64),(320,0,64,64) )  # Desenha o cenário na posição



    #screen.fill((255, 255, 255))  # Limpa a tela com cinza
    screen.fill((0,0,0))
    # Renderização da vela animada
    screen.blit(vela[curr_frame_vela], (200,200))
    #screen.blit(vela_b[curr_frame_vela_b], (400,180))

    # Renderização dos espinhos animados
    #screen.blit(spike[curr_frame_spike], (600,200))

    # Renderiza o mapa (cenário)
    screen.blit(mapa_2, (-55, -40),(0,0,290,190) )  # Desenha o cenário na posição 
    screen.blit(mapa_2, (150, -40),(0,0,290,190) )  # Desenha o cenário na posição 
    screen.blit(mapa_2, (350, -40),(0,0,290,190) )  # Desenha o cenário na posição
    screen.blit(mapa_2, (550, -40),(0,0,290,190) )  # Desenha o cenário na posição
    screen.blit(mapa_2, (750, -40),(0,0,290,190) )  # Desenha o cenário na posição
    screen.blit(mapa_2, (950, -40),(0,0,290,190) )  # Desenha o cenário na posição
    screen.blit(mapa_2, (1150, -40),(0,0,290,190) )  # Desenha o cenário na posição
    
    # Desenhar todas as coordenadas
    for x, y in coordenadas:
        screen.blit(mapa_3, (x, y), (0, 200, 20, 32))
    
    rect = (0, 200, 20, 32)
    # Linha horizontal de cima (Y=530 até Y=400)
    for y in range(400, 540, 10):
        for x in range(870, 910, 10):
            screen.blit(mapa_3, (x, y), rect)

    # Ponte pro Lado Direito
    # Versão otimizada com loops
    for x in range(910, 1110, 10):  # x: 910, 920, 930, ... 1100
        for y in range(400, 450, 10):  # y: 400, 410, 420, 430, 440
            screen.blit(mapa_3, (x, y), (0, 200, 20, 32))
    # Ponte para o Lado Esquerdo
    for x in range(700, 870, 10):  # x: 700, 710, 720, ... 860
        for y in range(400, 450, 10):  # y: 400, 410, 420, 430, 440
            screen.blit(mapa_3, (x, y), (0, 200, 20, 32))
    
    # Ponte para cima no Lado Esquerdo
    for x in range(700, 740, 10):  # x: 700, 710, 720, 730
        for y in range(300, 390, 10):  # y: 300, 310, 320, ... 380
            screen.blit(mapa_3, (x, y), (0, 200, 20, 32))
    # Ponte para o Lado Esquerdo
    for x in range(400, 700, 10):  # x: 400, 410, 420, ... 690
        for y in range(300, 340, 10):  # y: 300, 310, 320, 330
            screen.blit(mapa_3, (x, y), (0, 200, 20, 32))
    # Ponte para cima
    for x in range(400, 440, 10):  # x: 400, 410, 420, 430
        for y in range(180, 300, 10):  # y: 180, 190, 200, ... 290
            screen.blit(mapa_3, (x, y), (0, 200, 20, 32))

    # Blit especial no final
    screen.blit(vela_b[curr_frame_vela_b], (430, 300))


    # Para Baixo
    # Coluna esquerda (x=590, y=600 até 690)
    for y in range(600, 700, 10):
        screen.blit(mapa_3, (590, y), (0, 200, 20, 32))

    for x, y in pontos_especiais:
        screen.blit(mapa_3, (x, y), (0, 200, 20, 32))

    # Blit especial
    screen.blit(vela_b[curr_frame_vela_b], (600, 570))

    # Coluna x=600 (y=620 até 690)
    for y in range(620, 700, 10):
        screen.blit(mapa_3, (600, y), (0, 200, 20, 32))

    # Coluna x=620 (y=600 até 690)
    for y in range(600, 700, 10):
        screen.blit(mapa_3, (620, y), (0, 200, 20, 32))

    # Pontos específicos (y=590)
    for x in [590, 600]:
        screen.blit(mapa_3, (x, 590), (0, 200, 20, 32))

    # Linha longa (y=540, x=590 até 900)
    for x in range(590, 910, 10):
        screen.blit(mapa_3, (x, 540), (0, 200, 20, 32))
                                   



    # Paredes Lado Direito
    # Blits iniciais (mapa_4)
    screen.blit(mapa_4, (610, 600), (0, 0, 47, 150))
    screen.blit(mapa_4, (610, 550), (0, 0, 47, 150))

    # Paredes Lado Esquerdo
    # Coluna x=590 (parede grande)
    for y in range(540, 690, 10):
        screen.blit(mapa_5, (590, y), (0, 100, 100, 200))

    # Coluna x=870 (parede média)
    for y in range(400, 480, 10):
        screen.blit(mapa_5, (870, y), (0, 50, 100, 100))

    # Coluna x=700 (paredes irregulares)
    for y in [290, 300, 310, 320, 330, 340, 350, 360, 370, 375]:
        screen.blit(mapa_5, (700, y), (0, 50, 100, 100))

    # Coluna x=440 (pequenas paredes)
    for y in [200, 210]:
        screen.blit(mapa_9, (390, y), (0, 50, 100, 100))




    # Paredes Lado de Cima
    # Teto parte de baixo
    for x in range(650, 870, 40):
        screen.blit(mapa_8, (x, 590), (0, 0, 200, 100))

    # Teto parte de cima 2
    for x in range(405, 665, 40):
        screen.blit(mapa_8, (x, 360), (0, 0, 200, 100))

    # Teto da parte de cima 1
    for x, w, h in teto_cima_1:
        screen.blit(mapa_8, (x, 470), (0, 0, w, h))

    # Outras blits individuais (que não repetem padrão)
    screen.blit(mapa_7, (385, 115), (0, 0, 200, 100))
    screen.blit(mapa_6, (447, 250), (0, 0, 200, 100))
    screen.blit(mapa_6, (548, 250), (0, 0, 200, 79))
    screen.blit(mapa_6, (680, 490), (0, 0, 200, 79))
    screen.blit(mapa_6, (590, 490), (0, 0, 200, 79))
    screen.blit(mapa_6, (915, 350), (0, 0, 200, 100))
    screen.blit(mapa_6, (745, 350), (0, 0, 180, 100))
    



    # Personagem
    zant_surface = Surface((64,64), SRCALPHA)
    zant_surface.blit(zant, (0,0), (64*(curr_frame % 6), (curr_frame // 6)*64, 64, 64))

    if not zant_olhando_direita:
        zant_surface = transform.flip(zant_surface, True, False)
    
    screen.blit(zant_surface, (zant_x, zant_y))

    

    display.update()
