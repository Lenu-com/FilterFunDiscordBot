from typing import Final, List


class Image:
    IMAGE_EXTENSIONS: Final[List[str]] = ['.jpg', '.png', '.jpeg']
    
    
    def __init__(self, value: str) -> None:
        if not value:
            raise ValueError('value is invalid')
        if not self.is_image(value):
            raise ValueError('value is not image')
        self.__image_name = value
            
    
    def is_image(self, value: str) -> bool:
        for extension in self.IMAGE_EXTENSIONS:
            if value.endswith(extension):
                return True
        return False
