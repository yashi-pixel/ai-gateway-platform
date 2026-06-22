from app.providers.gemini_provider import Geminiprovider

class Generateservice():
    def __init__(self):
        self.provider = Geminiprovider()
    async def m_services(self, prompt:str) -> str:
        return self.provider.generate(prompt)