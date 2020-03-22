class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.memory_taken = 0
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        memory_left = self.memory - self.memory_taken

        if not self.is_on:
            return f'Turn on your phone to install {app}'

        if memory_left < app_memory:
            return f'Not enough memory to install {app}'

        self.apps.append(app)
        self.memory_taken += app_memory
        return f'Installing {app}'

    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.memory - self.memory_taken
        return f'Total apps: {total_apps_count}. Memory left: {self.memory_left}'
