from pygame import *
import sys

# --- INICIALIZAÇÃO DO PYGAME ----
init()
screen = display.set_mode((1280, 720))
display.set_caption("Tutorial")
clock = time.Clock()

#mapa = image.load("Atividade_12/Cenario/masmorra.png")
#mapa = transform.scale(mapa, (1280, 720))  # Redimensiona o mapa para preencher a tela
mapa_2 = image.load("cenario/masmorra.png")
pos_x = 0
pos_y = 0

mapa_3 = image.load("sprites_separados/sprite_4.png")
mapa_4 = image.load("spritesheet.png")

# Variáveis para animação da vela tipo A
curr_frame_vela = 0
anim_timer_vela = 0
vela = []
for i in range(4):
    vela.append(image.load(f"cenario/candleA_0{i+1}.png"))

# Variáveis para animação da vela tipo B
curr_frame_vela_b = 0
anim_timer_vela_b = 0
vela_b = []
for i in range(4):
    vela_b.append(image.load(f"cenario/candleB_0{i+1}.png"))

# Variáveis dos espinhos
curr_frame_spike = 0
anim_timer_spike = 0
spike = []
#for i in range(5):
    #spike.append(image.load(f"cenario/spike_0{i+1}.png"))

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
    screen.blit(vela_b[curr_frame_vela_b], (400,200))

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
    
    # Lado Direito
    screen.blit(mapa_3, (600,600),(0,200,20,32))
    screen.blit(mapa_3, (610,600),(0,200,20,32))
    screen.blit(mapa_3, (600,610),(0,200,20,32))
    screen.blit(mapa_3, (610,610),(0,200,20,32))
    screen.blit(mapa_3, (610,620),(0,200,20,32))
    screen.blit(mapa_3, (610,630),(0,200,20,32))
    screen.blit(mapa_3, (610,640),(0,200,20,32))
    screen.blit(mapa_3, (610,650),(0,200,20,32))
    screen.blit(mapa_3, (610,660),(0,200,20,32))
    screen.blit(mapa_3, (610,670),(0,200,20,32))
    screen.blit(mapa_3, (610,680),(0,200,20,32))
    screen.blit(mapa_3, (610,690),(0,200,20,32))
    screen.blit(mapa_3, ( 610,590), (0,200,20,32))
    screen.blit(mapa_3, ( 620,590), (0,200,20,32))
    screen.blit(mapa_3, ( 630,590), (0,200,20,32))
    screen.blit(mapa_3, ( 640,590), (0,200,20,32))
    screen.blit(mapa_3, ( 630,580), (0,200,20,32))
    screen.blit(mapa_3, ( 620,580), (0,200,20,32))
    screen.blit(mapa_3, ( 610,580), (0,200,20,32))
    screen.blit(mapa_3, ( 600,580), (0,200,20,32))
    screen.blit(mapa_3, ( 590,580), (0,200,20,32))
    screen.blit(mapa_3, ( 590,570), (0,200,20,32))
    screen.blit(mapa_3, ( 600,570), (0,200,20,32))
    screen.blit(mapa_3, ( 610,570), (0,200,20,32))
    screen.blit(mapa_3, ( 620,570), (0,200,20,32))
    screen.blit(mapa_3, ( 630,570), (0,200,20,32))
    screen.blit(mapa_3, ( 640,570), (0,200,20,32))
    screen.blit(mapa_3, ( 640,560), (0,200,20,32))
    screen.blit(mapa_3, ( 650,560), (0,200,20,32))
    screen.blit(mapa_3, ( 660,560), (0,200,20,32))
    screen.blit(mapa_3, ( 670,560), (0,200,20,32))
    screen.blit(mapa_3, ( 680,560), (0,200,20,32))
    screen.blit(mapa_3, ( 690,560), (0,200,20,32))
    screen.blit(mapa_3, ( 700,560), (0,200,20,32))
    screen.blit(mapa_3, ( 710,560), (0,200,20,32))
    screen.blit(mapa_3, ( 720,560), (0,200,20,32))
    screen.blit(mapa_3, ( 730,560), (0,200,20,32))
    screen.blit(mapa_3, ( 740,560), (0,200,20,32))
    screen.blit(mapa_3, ( 750,560), (0,200,20,32))
    screen.blit(mapa_3, ( 760,560), (0,200,20,32))
    screen.blit(mapa_3, ( 770,560), (0,200,20,32))
    screen.blit(mapa_3, ( 780,560), (0,200,20,32))
    screen.blit(mapa_3, ( 790,560), (0,200,20,32))
    screen.blit(mapa_3, ( 800,560), (0,200,20,32))
    screen.blit(mapa_3, ( 810,560), (0,200,20,32))
    screen.blit(mapa_3, ( 820,560), (0,200,20,32))
    screen.blit(mapa_3, ( 830,560), (0,200,20,32))
    screen.blit(mapa_3, ( 840,560), (0,200,20,32))
    screen.blit(mapa_3, ( 850,560), (0,200,20,32))
    screen.blit(mapa_3, ( 860,560), (0,200,20,32))
    screen.blit(mapa_3, ( 870,560), (0,200,20,32))
    screen.blit(mapa_3, ( 880,560), (0,200,20,32))
    screen.blit(mapa_3, ( 890,560), (0,200,20,32))
    screen.blit(mapa_3, ( 900,560), (0,200,20,32))
    screen.blit(mapa_3, ( 900,550), (0,200,20,32))
    screen.blit(mapa_3, ( 890,550), (0,200,20,32))
    screen.blit(mapa_3, ( 880,550), (0,200,20,32))
    screen.blit(mapa_3, ( 870,550), (0,200,20,32))
    screen.blit(mapa_3, ( 860,550), (0,200,20,32))
    screen.blit(mapa_3, ( 850,550), (0,200,20,32))
    screen.blit(mapa_3, ( 840,550), (0,200,20,32))
    screen.blit(mapa_3, ( 830,550), (0,200,20,32))
    screen.blit(mapa_3, ( 820,550), (0,200,20,32))
    screen.blit(mapa_3, ( 810,550), (0,200,20,32))
    screen.blit(mapa_3, ( 800,550), (0,200,20,32))
    screen.blit(mapa_3, ( 790,550), (0,200,20,32))
    screen.blit(mapa_3, ( 780,550), (0,200,20,32))
    screen.blit(mapa_3, ( 770,550), (0,200,20,32))
    screen.blit(mapa_3, ( 760,550), (0,200,20,32))
    screen.blit(mapa_3, ( 750,550), (0,200,20,32))
    screen.blit(mapa_3, ( 740,550), (0,200,20,32))
    screen.blit(mapa_3, ( 730,550), (0,200,20,32))
    screen.blit(mapa_3, ( 720,550), (0,200,20,32))
    screen.blit(mapa_3, ( 710,550), (0,200,20,32))
    screen.blit(mapa_3, ( 700,550), (0,200,20,32))
    screen.blit(mapa_3, ( 690,550), (0,200,20,32))
    screen.blit(mapa_3, ( 680,550), (0,200,20,32))
    screen.blit(mapa_3, ( 670,550), (0,200,20,32))
    screen.blit(mapa_3, ( 660,550), (0,200,20,32))    
    screen.blit(mapa_3, ( 650,550), (0,200,20,32))
    screen.blit(mapa_3, ( 640,550), (0,200,20,32))
    screen.blit(mapa_3, ( 630,550), (0,200,20,32))
    screen.blit(mapa_3, ( 620,550), (0,200,20,32))
    screen.blit(mapa_3, ( 610,550), (0,200,20,32))
    screen.blit(mapa_3, ( 600,550), (0,200,20,32))
    screen.blit(mapa_3, ( 590,550), (0,200,20,32))
    screen.blit(mapa_3, ( 590,560), (0,200,20,32))
    screen.blit(mapa_3, ( 600,560), (0,200,20,32))
    screen.blit(mapa_3, ( 610,560), (0,200,20,32))
    screen.blit(mapa_3, ( 620,560), (0,200,20,32))
    screen.blit(mapa_3, ( 630,560), (0,200,20,32))
    screen.blit(mapa_3, ( 640,560), (0,200,20,32))


    # Para Baixo
    screen.blit(mapa_3, ( 590,600), (0,200,20,32))
    screen.blit(mapa_3, ( 590,610), (0,200,20,32))
    screen.blit(mapa_3, ( 590,620), (0,200,20,32))
    screen.blit(mapa_3, ( 590,630), (0,200,20,32))
    screen.blit(mapa_3, ( 590,640), (0,200,20,32))
    screen.blit(mapa_3, ( 590,650), (0,200,20,32))
    screen.blit(mapa_3, ( 590,660), (0,200,20,32))
    screen.blit(mapa_3, ( 590,670), (0,200,20,32))
    screen.blit(mapa_3, ( 590,680), (0,200,20,32))
    screen.blit(mapa_3, ( 590,690), (0,200,20,32))
    screen.blit(mapa_3, (630,600),(0,200,20,32))
    screen.blit(mapa_3, (630,610),(0,200,20,32))
    screen.blit(mapa_3, (630,650),(0,200,20,32))
    screen.blit(mapa_3, (630,660),(0,200,20,32))
    

    # Lado Esquerdo
    screen.blit(mapa_3, (600,620),(0,200,20,32))
    screen.blit(mapa_3, (600,630),(0,200,20,32))
    screen.blit(mapa_3, (600,640),(0,200,20,32))
    screen.blit(mapa_3, (600,650),(0,200,20,32))
    screen.blit(mapa_3, (600,660),(0,200,20,32))
    screen.blit(mapa_3, (600,670),(0,200,20,32))
    screen.blit(mapa_3, (600,680),(0,200,20,32))
    screen.blit(mapa_3, (600,690),(0,200,20,32))

    screen.blit(mapa_3, (620,600),(0,200,20,32))
    screen.blit(mapa_3, (620,610),(0,200,20,32))
    screen.blit(mapa_3, (620,620),(0,200,20,32))
    screen.blit(mapa_3, (620,630),(0,200,20,32))
    screen.blit(mapa_3, (620,640),(0,200,20,32))
    screen.blit(mapa_3, (620,650),(0,200,20,32))
    screen.blit(mapa_3, (620,660),(0,200,20,32))
    screen.blit(mapa_3, (620,670),(0,200,20,32))
    screen.blit(mapa_3, (620,680),(0,200,20,32))
    screen.blit(mapa_3, (620,690),(0,200,20,32))
    screen.blit(mapa_3, (600,590),(0,200,20,32))
    screen.blit(mapa_3, (590,590),(0,200,20,32))
    
    # Paredes Lado Direito
    screen.blit(mapa_4,(610,600),(0,0,47,150))
    screen.blit(mapa_4,(610,550),(0,0,47,150))

    # Paredes Lado Esquerdo
    screen.blit(mapa_4,(390,600),(0,0,100,200))
    

    # Ponte para Cima - OTIMIZADO COM LOOPS
    rect = (0, 200, 20, 32)
    # Linha horizontal de cima (Y=530 até Y=400)
    for y in range(400, 540, 10):
        for x in range(870, 910, 10):
            screen.blit(mapa_3, (x, y), rect)




    screen.blit(mapa_3,(110,200),(0,200,20,32))




    display.update()
