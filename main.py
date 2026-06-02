from pygame import *
import sys

# --- INICIALIZAÇÃO DO PYGAME ----
init()
screen = display.set_mode((1280, 720))
display.set_caption("Tutorial")
clock = time.Clock()

#mapa = image.load("Atividade_12/Cenario/masmorra.png")
#mapa = transform.scale(mapa, (1280, 720))  # Redimensiona o mapa para preencher a tela
mapa_2 = image.load("Atividade_12/cenario/masmorra.png")
pos_x = 0
pos_y = 0

# Variáveis para animação da vela tipo A
curr_frame_vela = 0
anim_timer_vela = 0
vela = []
for i in range(4):
    vela.append(image.load(f"Atividade_12/cenario/candleA_0{i+1}.png"))

# Variáveis para animação da vela tipo B
curr_frame_vela_b = 0
anim_timer_vela_b = 0
vela_b = []
for i in range(4):
    vela_b.append(image.load(f"Atividade_12/cenario/candleB_0{i+1}.png"))

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



    screen.fill((0, 0, 0))  # Limpa a tela com cinza
    
    # Renderização da vela animada
    screen.blit(vela[curr_frame_vela], (200,200))
    screen.blit(vela_b[curr_frame_vela_b], (400,200))

    # Renderiza o mapa (cenário)
    screen.blit(mapa_2, (-55, -40),(0,0,290,190) )  # Desenha o cenário na posição 
    screen.blit(mapa_2, (150, -40),(0,0,290,190) )  # Desenha o cenário na posição 
    screen.blit(mapa_2, (350, -40),(0,0,290,190) )  # Desenha o cenário na posição
    screen.blit(mapa_2, (550, -40),(0,0,290,190) )  # Desenha o cenário na posição
    screen.blit(mapa_2, (750, -40),(0,0,290,190) )  # Desenha o cenário na posição
    screen.blit(mapa_2, (950, -40),(0,0,290,190) )  # Desenha o cenário na posição
    screen.blit(mapa_2, (1150, -40),(0,0,290,190) )  # Desenha o cenário na posição
    






    display.update()
