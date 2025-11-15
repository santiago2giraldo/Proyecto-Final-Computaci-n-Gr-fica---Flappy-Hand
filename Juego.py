import pygame
import random

# ---------------------------
# CONFIGURACIÓN
# ---------------------------
W, H = 900, 600
GRAVEDAD = 2000.0
RESTITUCION = 0.6
ROZAMIENTO_AIRE = 0.5

pygame.init()
screen = pygame.display.set_mode((W, H))
clock  = pygame.time.Clock()
pygame.display.set_caption("Gravedad Pygame")
font = pygame.font.SysFont(None, 40)
font_small = pygame.font.SysFont(None, 24)

# ---------------------------
# FUNCIONES DEL JUEGO
# ---------------------------
def aplicar_gravedad_y_rozamiento(jugador, dt):
    drag = ROZAMIENTO_AIRE ** dt
    jugador["vy"] += GRAVEDAD * dt
    jugador["vx"] *= drag
    jugador["vy"] *= drag


# ---------------------------
# MENÚ PRINCIPAL
# ---------------------------
def menu_principal():
    while True:
        screen.fill((20, 20, 20))

        mx, my = pygame.mouse.get_pos()

        # Botones
        botones = [
            ("Jugar", (W//2, 200)),
            ("Instrucciones", (W//2, 280)),
            ("Salir", (W//2, 360)),
        ]

        for texto, (x, y) in botones:
            render = font.render(texto, True, (255, 255, 255))
            rect = render.get_rect(center=(x, y))

            # Efecto hover
            color_fondo = (80, 80, 80) if rect.collidepoint(mx, my) else (50, 50, 50)
            pygame.draw.rect(screen, color_fondo, rect.inflate(40, 20), border_radius=10)

            screen.blit(render, rect)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if e.type == pygame.MOUSEBUTTONDOWN:
                for texto, (x, y) in botones:
                    render = font.render(texto, True, (255, 255, 255))
                    rect = render.get_rect(center=(x, y))

                    if rect.inflate(40, 20).collidepoint(mx, my):
                        if texto == "Jugar":
                            return  # Sale del menú y ejecuta el juego
                        if texto == "Instrucciones":
                            instrucciones()
                        if texto == "Salir":
                            pygame.quit()
                            raise SystemExit

        pygame.display.flip()
        clock.tick(60)


# ---------------------------
# PANTALLA DE INSTRUCCIONES
# ---------------------------
def instrucciones():
    while True:
        screen.fill((10, 10, 30))

        lines = [
            "INSTRUCCIONES:",
            "- Este juego simula gravedad, rozamiento y rebotes.",
            "- El jugador cae acelerado por la gravedad.",
            "- Rebota al tocar el piso.",
            "",
            "Haz clic para volver al menú..."
        ]

        y = 150
        for line in lines:
            render = font_small.render(line, True, (255, 255, 255))
            screen.blit(render, (50, y))
            y += 40

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if e.type == pygame.MOUSEBUTTONDOWN:
                return  # vuelve al menú

        pygame.display.flip()
        clock.tick(60)


# ---------------------------
# LOOP DEL JUEGO PRINCIPAL
# ---------------------------
def jugar():
    # Un ejemplo de jugador (puedes reemplazarlo por tu código)
    jugador = {"x": W//2, "y": 50, "vx": 0, "vy": 0}

    while True:
        dt = clock.tick(120) / 1000.0

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        aplicar_gravedad_y_rozamiento(jugador, dt)

        # Simulación de piso:
        if jugador["y"] > H - 50:
            jugador["y"] = H - 50
            jugador["vy"] = -jugador["vy"] * RESTITUCION

        jugador["x"] += jugador["vx"] * dt
        jugador["y"] += jugador["vy"] * dt

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (0, 255, 0), (int(jugador["x"]), int(jugador["y"])), 20)

        pygame.display.flip()


# ---------------------------
# PROGRAMA: iniciar menú
# ---------------------------
menu_principal()
jugar()


