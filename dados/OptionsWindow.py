import pygame

class OptionsWindow:
    def open_options_window(self):
        # Create a new Pygame window
        options_window = pygame.display.set_mode((400, 300))  # Set size for the new window
        pygame.display.set_caption("Options Menu")

        options = ["Busca Largura", "Busca Profundidade", "Busca A*"]
        selected_option = None

        running = True
        while running:
            options_window.fill((200, 200, 200))  # Fill the background with a light gray color

            # Draw options
            font = pygame.font.Font(None, 36)
            for i, option in enumerate(options):
                text_surface = font.render(option, True, (0, 0, 0))
                options_window.blit(text_surface, (50, 50 + i * 50))

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    option_index = (my - 50) // 50  # Determine which option was clicked
                    if 0 <= option_index < len(options):
                        selected_option = options[option_index]
                        running = False  # Close the options window after selection

            pygame.display.update()

        # Return to the main game window
        pygame.display.set_mode((800, 800))  # Reset to the main game window size
        return selected_option




