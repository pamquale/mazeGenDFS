import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

UP, DOWN, LEFT, RIGHT = 'up', 'down', 'left', 'right'


class MazeGame:
    def __init__(self):
        self.exit_y = None
        self.exit_x = None
        self.player_y = None
        self.player_x = None
        self.grid = None
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.reset_game()

    def generate_maze(self):
        stack = [(0, 0)]
        self.grid[0][0] = 0

        while stack:
            x, y = stack[-1]
            neighbors = self.get_unvisited_neighbors(x, y)

            if neighbors:
                next_x, next_y = random.choice(neighbors)
                self.remove_wall_between(x, y, next_x, next_y)
                self.grid[next_x][next_y] = 0
                stack.append((next_x, next_y))
            else:
                stack.pop()

        self.ensure_path_to_exit()

    def get_unvisited_neighbors(self, x, y):
        neighbors = []
        if x > 1 and self.grid[x - 2][y] == 1:
            neighbors.append((x - 2, y))
        if x < GRID_HEIGHT - 2 and self.grid[x + 2][y] == 1:
            neighbors.append((x + 2, y))
        if y > 1 and self.grid[x][y - 2] == 1:
            neighbors.append((x, y - 2))
        if y < GRID_WIDTH - 2 and self.grid[x][y + 2] == 1:
            neighbors.append((x, y + 2))
        return neighbors

    def remove_wall_between(self, x1, y1, x2, y2):
        self.grid[(x1 + x2) // 2][(y1 + y2) // 2] = 0

    def ensure_path_to_exit(self):
        from collections import deque

        queue = deque([(0, 0)])
        visited = {0, 0}

        while queue:
            x, y = queue.popleft()

            if (x, y) == (GRID_WIDTH - 1, GRID_HEIGHT - 1):
                return

            for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_HEIGHT and 0 <= ny < GRID_WIDTH and self.grid[nx][ny] == 0 and (
                nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        self.create_direct_path()

    def create_direct_path(self):
        x, y = 0, 0
        while (x, y) != (GRID_HEIGHT - 1, GRID_WIDTH - 1):
            if x < GRID_HEIGHT - 1:
                x += 1
            if y < GRID_WIDTH - 1:
                y += 1
            self.grid[x][y] = 0

    def draw_grid(self):
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if self.grid[row][col] == 1:
                    pygame.draw.rect(self.screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, GREEN, (self.exit_x * CELL_SIZE, self.exit_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_player(self):
        pygame.draw.circle(self.screen, RED,
                           (self.player_x * CELL_SIZE + CELL_SIZE // 2, self.player_y * CELL_SIZE + CELL_SIZE // 2),
                           CELL_SIZE // 3)

    def move_player(self, direction):
        if direction == UP and self.player_y > 0 and self.grid[self.player_y - 1][self.player_x] == 0:
            self.player_y -= 1
        elif direction == DOWN and self.player_y < GRID_HEIGHT - 1 and self.grid[self.player_y + 1][self.player_x] == 0:
            self.player_y += 1
        elif direction == LEFT and self.player_x > 0 and self.grid[self.player_y][self.player_x - 1] == 0:
            self.player_x -= 1
        elif direction == RIGHT and self.player_x < GRID_WIDTH - 1 and self.grid[self.player_y][self.player_x + 1] == 0:
            self.player_x += 1
        self.check_win()

    def check_win(self):
        if self.player_x == self.exit_x and self.player_y == self.exit_y:
            self.display_win_screen()

    def display_win_screen(self):
        win_text = self.font.render("You Won! Press R to Restart", True, RED)
        self.screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
        pygame.display.flip()
        self.wait_for_restart()

    def wait_for_restart(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                        self.reset_game()

    def reset_game(self):
        self.grid = [[1] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.player_x = 0
        self.player_y = 0
        self.exit_x = GRID_WIDTH - 1
        self.exit_y = GRID_HEIGHT - 1
        self.generate_maze()
        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move_player(UP)
                    elif event.key == pygame.K_DOWN:
                        self.move_player(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.move_player(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.move_player(RIGHT)

            self.screen.fill(WHITE)
            self.draw_grid()
            self.draw_player()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    game = MazeGame()
    game.run()
