from google.genai import Client
from app.core.settings import settings

class Geminiprovider:
    def __init__(self):
        self.client = Client(api_key=settings.GEMINI_API_KEY)
        self.model = settings.GEMINI_MODEL
        #print(dir(self.client))

    def generate(self, prompt: str):
        response = self.client.models.generate_content(model=self.model, contents=prompt)
        return response.text


