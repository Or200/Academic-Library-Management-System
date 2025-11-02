from datetime import datetime

class Logger:

    @staticmethod
    def log_action(action_type: str, details: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open ("log.log", "a")  as f:
            f.write (f"[{timestamp}] [{action_type}] {details} \n")
