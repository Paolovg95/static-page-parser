class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, obj):
        if self.text == obj.text and self.text_type == obj.text_type and self.url == obj.url:
            return True
        return False

    def __repr__(self):
        TEXT = self.text
        TEXT_TYPE = self.text_type
        URL = self.url
        return f"{TEXT}, {TEXT_TYPE}, {URL}"
