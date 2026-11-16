# bot/utils/logger.py
from datetime import datetime
from rich.console import Console
from rich.theme import Theme

class Logger:
    def __init__(self):
        self.console = Console(theme=Theme({
            "info": "blue",
            "step": "cyan",
            "warning": "yellow",
            "error": "red",
            "success": "green",
            "debug": "#B7B7B7",
            "timestamp": "#B7B7B7",
            "message": "white"
        }))
    
    def log(self, level, message, **kwargs):
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        level_styles = {
            "INFO": "info",
            "STEP": "step",
            "WARNING": "warning", 
            "ERROR": "error",
            "SUCCESS": "success",
            "DEBUG": "debug"
        }
        
        level_clean = level.upper().rstrip(':')
        style = level_styles.get(level_clean, "info")
        
        self.console.print(
            f"[timestamp][{timestamp}][/timestamp] "
            f"[{style}][{level_clean}][/{style}] "
            f"[message]{message}[/message]",
            **kwargs
        )
    
    def info(self, message):
        self.log("INFO", f"ℹ {message}")

    def step(self, message):
        self.log("STEP", f"→ {message}")
        
    def warning(self, message):
        self.log("WARNING", f"! {message}")
        
    def error(self, message):
        self.log("ERROR", f"✗ {message}")
        
    def success(self, message):
        self.log("SUCCESS", f"✓ {message}")

    def debug(self, message):
        self.log("DEBUG", f"{message}")

# Глобальный логгер
logger = Logger()