import httpx
from redis import Redis
from src.config import settings

class AIClient:
    def __init__(self, redis: Redis):
        self.redis = redis
        self.endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

    async def generate(self, prompt: str) -> str:
        # Vérifie le cache Redis
        if cached := self.redis.get(f"ai:{hash(prompt)}"):
            return cached.decode()

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.endpoint}?key={settings.GOOGLE_AI_KEY}",
                json={"contents": [{"parts": [{"text": prompt}]}]}
            )
            response.raise_for_status()
            result = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            self.redis.setex(f"ai:{hash(prompt)}", 3600, result)  # Cache 1h
            return result
