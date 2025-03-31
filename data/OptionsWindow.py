import pygame

class OptionsWindow:
    def open_options_window(self):
        # Cria a tela de seleção do tipo de Busca
        options_window = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Options Menu")

        options = ["Busca Largura", "Busca Profundidade", "Busca A*"]
        selected_option = None

        running = True
        while running:
            options_window.fill((200, 200, 200))

            font = pygame.font.Font(None, 36)
            for i, option in enumerate(options):
                text_surface = font.render(option, True, (0, 0, 0))
                options_window.blit(text_surface, (50, 50 + i * 50))

            # Verifica o que clicou
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    option_index = (my - 50) // 50  # Verifica qual opção de Busca escolheu
                    if 0 <= option_index < len(options):
                        selected_option = options[option_index]
                        running = False

            pygame.display.update()

        # Volta para a tela main
        pygame.display.set_mode((800, 800))
        return selected_option




