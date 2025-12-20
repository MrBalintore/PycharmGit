
import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np
import pygame
import sys

# --- Tic-Tac-Toe Environment ---
class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 = X, -1 = O
        return self.get_state()

    def get_state(self):
        return torch.tensor(self.board.flatten(), dtype=torch.float32)

    def available_actions(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def step(self, action):
        i, j = action
        if self.board[i, j] != 0:
            return self.get_state(), -10, True  # invalid move
        self.board[i, j] = self.current_player

        if self.check_winner(self.current_player):
            return self.get_state(), 1, True
        elif len(self.available_actions()) == 0:
            return self.get_state(), 0, True  # draw

        self.current_player *= -1
        return self.get_state(), 0, False

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i, :] == player):
                return True
            if all(self.board[:, i] == player):
                return True
        if all(np.diag(self.board) == player):
            return True
        if all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

# --- Neural Network ---
class QNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(9, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 9)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

# --- Training Loop ---
def train_agent(episodes=2000):
    env = TicTacToe()
    model = QNetwork()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()

    gamma = 0.9
    epsilon = 1.0
    epsilon_decay = 0.999
    epsilon_min = 0.1

    for ep in range(episodes):
        state = env.reset()
        done = False

        while not done:
            if random.random() < epsilon:
                action = random.choice(env.available_actions())
                action_idx = action[0] * 3 + action[1]
            else:
                q_values = model(state)
                mask = torch.tensor([i * 3 + j for i, j in env.available_actions()])
                action_idx = mask[torch.argmax(q_values[mask]).item()].item()
                action = (action_idx // 3, action_idx % 3)

            next_state, reward, done = env.step(action)

            with torch.no_grad():
                target = reward + gamma * (0 if done else torch.max(model(next_state)))

            pred = model(state)[action_idx]
            loss = criterion(pred, torch.tensor(target))

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            state = next_state

        if epsilon > epsilon_min:
            epsilon *= epsilon_decay

        if ep % 500 == 0:
            print(f"Episode {ep}, Epsilon: {epsilon:.3f}")

    return model

# --- GUI using pygame ---
def play_gui(model):
    pygame.init()
    size = 300
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption('Tic-Tac-Toe')
    clock = pygame.time.Clock()

    env = TicTacToe()
    state = env.reset()

    font = pygame.font.SysFont(None, 100)

    def draw_board():
        screen.fill((255, 255, 255))
        for i in range(1, 3):
            pygame.draw.line(screen, (0, 0, 0), (0, i * 100), (300, i * 100), 5)
            pygame.draw.line(screen, (0, 0, 0), (i * 100, 0), (i * 100, 300), 5)
        for i in range(3):
            for j in range(3):
                if env.board[i, j] == 1:
                    text = font.render('X', True, (255, 0, 0))
                    screen.blit(text, (j * 100 + 25, i * 100 + 10))
                elif env.board[i, j] == -1:
                    text = font.render('O', True, (0, 0, 255))
                    screen.blit(text, (j * 100 + 25, i * 100 + 10))

    running = True
    while running:
        draw_board()
        pygame.display.flip()

        if env.current_player == -1:
            with torch.no_grad():
                q_values = model(state)
                mask = torch.tensor([i * 3 + j for i, j in env.available_actions()])
                action_idx = mask[torch.argmax(q_values[mask]).item()].item()
                action = (action_idx // 3, action_idx % 3)
                state, reward, done = env.step(action)

                if done:
                    draw_board()
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    env.reset()
                    state = env.get_state()
                    continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and env.current_player == 1:
                x, y = pygame.mouse.get_pos()
                action = (y // 100, x // 100)
                state, reward, done = env.step(action)
                if done:
                    draw_board()
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    env.reset()
                    state = env.get_state()

        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    print("Training agent...")
    trained_model = train_agent(2000)
    play_gui(trained_model)