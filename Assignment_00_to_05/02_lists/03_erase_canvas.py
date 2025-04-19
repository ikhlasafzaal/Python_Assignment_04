import pygame  # Pygame library ko import karte hain

# Pygame ko initialize karte hain
pygame.init()

# Set up the display window
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Eraser Tool on Canvas")  # Window ka title set karte hain

# Colors ko define karte hain
BLUE = (0, 0, 255)  # Blue color for the grid cells
WHITE = (255, 255, 255)  # White color for erasing
ERASER_COLOR = (200, 200, 200)  # Light color for the eraser rectangle

# Grid ka setup
cell_size = 40  # Har cell ka size 40 pixels hoga
rows = screen_height // cell_size  # Screen mein rows ka number
cols = screen_width // cell_size  # Screen mein columns ka number

# Grid banate hain (sabhi cells ko initially blue karte hain)
grid = [[BLUE for _ in range(cols)] for _ in range(rows)]

# Eraser ka size aur position set karte hain
eraser_width = 80  # Eraser ka width 80 pixels
eraser_height = 80  # Eraser ka height 80 pixels
eraser_x = 100  # Eraser ki initial X position
eraser_y = 100  # Eraser ki initial Y position

# Main game loop chalate hain
running = True
while running:
    # Events ko handle karte hain (jaise window ko close karna)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouse ki position ko get karte hain aur eraser ko uske according move karte hain
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser_x = mouse_x - eraser_width // 2  # Eraser ko mouse ke center pe adjust karte hain
    eraser_y = mouse_y - eraser_height // 2  # Eraser ko y-axis pe adjust karte hain

    # Screen ko white se fill karte hain (purani drawing ko clean karte hain)
    screen.fill(WHITE)

    # Grid ko draw karte hain
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, grid[row][col], (col * cell_size, row * cell_size, cell_size, cell_size))

    # Eraser ko draw karte hain (grey rectangle)
    pygame.draw.rect(screen, ERASER_COLOR, (eraser_x, eraser_y, eraser_width, eraser_height))

    # Eraser ke touch mein aaye hue cells ko white karte hain
    start_col = max(0, eraser_x // cell_size)  # Eraser ke start column ko calculate karte hain
    end_col = min(cols, (eraser_x + eraser_width) // cell_size)  # Eraser ke end column ko calculate karte hain
    start_row = max(0, eraser_y // cell_size)  # Eraser ke start row ko calculate karte hain
    end_row = min(rows, (eraser_y + eraser_height) // cell_size)  # Eraser ke end row ko calculate karte hain

    # Jahan jahan eraser gaya hai, wahan cells ko white kar dete hain
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            grid[row][col] = WHITE  # Eraser ke upar jo cells hain unko white kar dete hain

    # Screen ko update karte hain
    pygame.display.flip()

# Pygame ko close karte hain
pygame.quit()
