import time
import os
class Cronometro:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    def get_elapsed_time(self):
        if self.running:
            return time.time() - self.start_time
        return self.elapsed_time

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        elapsed = self.get_elapsed_time()
        minutes, seconds = divmod(elapsed, 60)
        hours, minutes = divmod(minutes, 60)
        print(f"Cronômetro: {int(hours):02}:{int(minutes):02}:{int(seconds):02}")

if __name__ == "__main__":
    cronometro = Cronometro()
    while True:
        cronometro.display()
        print("Comandos: [s]tart, s[t]op, [r]eset, [q]uit")
        command = input("Digite um comando: ").strip().lower()
        if command == 's':
            cronometro.start()
        elif command == 't':
            cronometro.stop()
        elif command == 'r':
            cronometro.reset()
        elif command == 'q':
            break
        time.sleep(0.1)

