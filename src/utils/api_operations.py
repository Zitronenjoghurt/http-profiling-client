from src.config import Config

CONFIG = Config.get_instance()

def generate_url(endpoint_path: list[str], **kwargs) -> str:
    endpoint = "/".join(endpoint_path)
    arguments = "&".join([f"{key}={value}" for key, value in kwargs.items()])
    if len(kwargs) > 0:
        return f"https://{CONFIG.HOSTNAME}/{endpoint}?{arguments}"
    return f"https://{CONFIG.HOSTNAME}/{endpoint}"

def generate_path_with_params(endpoint_path: list[str], **kwargs) -> str:
    endpoint = "/".join(endpoint_path)
    arguments = "&".join([f"{key}={value}" for key, value in kwargs.items()])
    if len(kwargs) > 0:
        return f"/{endpoint}?{arguments}"
    return f"/{endpoint}"