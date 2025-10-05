# Use Conda environment: piano
import pygame

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Create window
screen = pygame.display.set_mode((600, 250))
pygame.display.set_caption("Python Piano")

# Font for displaying text
font = pygame.font.SysFont("Arial", 28, bold=True)
small_font = pygame.font.SysFont("Arial", 20)

# Text surfaces
title_text = font.render("Welcome to Keyboard Piano!", True, (255, 255, 255))
hint_text = small_font.render("Press keys to play notes. Press ESC to quit.", True, (200, 200, 200))

# Get rectangles for positioning
title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 20))
hint_rect = hint_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 20))


# Map keys to note sounds
key_to_note = {
    # C3 - B3 -> keyboard q - u, 2 - 7
    pygame.K_q: "sounds/C3.wav",
    pygame.K_2: "sounds/C3#.wav",
    pygame.K_w: "sounds/D3.wav",
    pygame.K_3: "sounds/D3#.wav",
    pygame.K_e: "sounds/E3.wav",
    pygame.K_r: "sounds/F3.wav",
    pygame.K_5: "sounds/F3#.wav",
    pygame.K_t: "sounds/G3.wav",
    pygame.K_6: "sounds/G3#.wav",
    pygame.K_y: "sounds/A3.wav",
    pygame.K_7: "sounds/A3#.wav",
    pygame.K_u: "sounds/B3.wav",

    # C4 - B4 -> keyboard i - ], z - x; 9 - =, a - s
    pygame.K_i: "sounds/C4.wav",
    pygame.K_9: "sounds/C4#.wav",
    pygame.K_o: "sounds/D4.wav",
    pygame.K_0: "sounds/D4#.wav",
    pygame.K_p: "sounds/E4.wav",
    pygame.K_LEFTBRACKET: "sounds/F4.wav",
    pygame.K_EQUALS: "sounds/F4#.wav",
    pygame.K_RIGHTBRACKET: "sounds/G4.wav",
    pygame.K_a: "sounds/G4#.wav",
    pygame.K_z: "sounds/A4.wav",
    pygame.K_s: "sounds/A4#.wav",
    pygame.K_x: "sounds/B4.wav",
    
    # C5 - B5 -> keyboard c - ., f - l
    pygame.K_c: "sounds/C5.wav",
    pygame.K_f: "sounds/C5#.wav",
    pygame.K_v: "sounds/D5.wav",
    pygame.K_g: "sounds/D5#.wav",
    pygame.K_b: "sounds/E5.wav",
    pygame.K_n: "sounds/F5.wav",
    pygame.K_j: "sounds/F5#.wav",
    pygame.K_m: "sounds/G5.wav",
    pygame.K_k: "sounds/G5#.wav",
    pygame.K_COMMA: "sounds/A5.wav",
    pygame.K_l: "sounds/A5#.wav",
    pygame.K_PERIOD: "sounds/B5.wav",

    # C6 -> keyboard /
    pygame.K_SLASH: "sounds/C6.wav",
}

# Load sounds
sounds = {key: pygame.mixer.Sound(note_file) for key, note_file in key_to_note.items()}

# Track which keys are playing
playing_channels = {}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press ESC to quit
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        # Press key → play note (only once, no looping)
        elif event.type == pygame.KEYDOWN:
            if event.key in sounds and event.key not in playing_channels:
                channel = sounds[event.key].play()  # play once, full length
                playing_channels[event.key] = channel

        # Release key → fade out if still playing
        elif event.type == pygame.KEYUP:
            if event.key in playing_channels:
                channel = playing_channels[event.key]
                if channel.get_busy():  # if sound still playing
                    channel.fadeout(300)  # fade out smoothly
                del playing_channels[event.key]
    
    # Draw background and text
    screen.fill((30, 30, 30))
    screen.blit(title_text, title_rect)
    screen.blit(hint_text, hint_rect)
    pygame.display.flip()

pygame.quit()
