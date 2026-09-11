# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: ContentCalendar
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    FG_BLACK = "\033[30m"
    FG_WHITE = "\033[37m"

    @staticmethod
    def enabled():
        return getattr(__import__("content_calendar"), "_COLORS_ENABLED", True)

    @staticmethod
    def disable():
        import content_calendar
        content_calendar._COLORS_ENABLED = False

    @staticmethod
    def enable():
        import content_calendar
        content_calendar._COLORS_ENABLED = True

    @staticmethod
    def active():
        import content_calendar
        return content_calendar._COLORS_ENABLED
