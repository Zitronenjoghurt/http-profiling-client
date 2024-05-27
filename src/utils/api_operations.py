from src.config import Config

CONFIG = Config.get_instance()

def generate_url(endpoint_path: list[str], **kwargs) -> str:
        endpoint = "/".join(endpoint_path)
        arguments = "&".join([f"{key}={value}" for key, value in kwargs.items()])
        if len(kwargs) > 0:
            return f"{CONFIG.URL}/{endpoint}?{arguments}"
        return f"{CONFIG.URL}/{endpoint}"