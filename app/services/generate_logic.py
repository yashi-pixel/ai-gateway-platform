from app.providers.gemini_provider import Geminiprovider

class Generateservice():
    def __init__(self):
        self.provider = Geminiprovider()
    async def m_services(self, prompt:str):
        #return f"This is your response for : {prompt}"
        return self.provider.generate(prompt)