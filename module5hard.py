class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        self.hash_password = hash(password)


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname:
                if i.password == password and i.hash_password == hash(password):
                    self.current_user = nickname

    def register(self, nickname, password, age):
        if User(nickname, password, age) in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User(nickname, password, age))
            UrTube.log_in(self, nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for el in args:
            if el not in self.videos:
                self.videos.append(el)

    def get_videos(self, word):
        correct_videos = []
        for el in self.videos:
            if word.lower() in str(el).lower():
                correct_videos.append(el.title)
        return correct_videos

    def watch_video(self, title):
        from time import sleep
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for el in self.videos:
                if title == el.title:
                    if el.adult_mode == True:
                        for i in self.users:
                            if i.nickname == self.current_user:
                                if i.age < 18:
                                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                                else:
                                    for i in range(el.time_now + 1, el.duration + 1):
                                        sleep(1)
                                        print(i, end =' ')
                                    print('Конец видео')
                                    break
                    else:
                        for i in range(el.time_now + 1, el.duration + 1):
                            sleep(1)
                            print(i, end=' ')
                        print('Конец видео')
                        break


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


