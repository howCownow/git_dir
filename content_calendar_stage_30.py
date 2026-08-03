# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: ContentCalendar
class Profile:
    def __init__(self, login, name, email):
        self.login = login
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"Profile({self.login}, {self.name})"

profiles = []
current_profile = None

def add_profile(login, name, email):
    global current_profile
    profiles.append(Profile(login, name, email))
    if not current_profile:
        current_profile = profiles[-1]
    return current_profile

def switch_profile(login):
    for p in profiles:
        if p.login == login:
            global current_profile
            current_profile = p
            return True
    return False

def get_current():
    return current_profile

def list_profiles():
    return [p.name for p in profiles]
