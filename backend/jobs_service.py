import os
import httpx
from dotenv import load_dotenv

load_dotenv()


BA_JOBS_API_KEY = os.getenv("BA_JOBS_API_KEY")
BA_JOBS_API_URL = os.getenv("BA_JOBS_API_URL")


async def search_germany_jobs(
    keyword: str,
    location: str = "Germany",
    page: int = 1,
    size: int = 20
):
    if not BA_JOBS_API_KEY:
        raise RuntimeError("BA_JOBS_API_KEY is missing")

    if not BA_JOBS_API_URL:
        raise RuntimeError("BA_JOBS_API_URL is missing")

    url = f"{BA_JOBS_API_URL.rstrip('/')}/pc/v6/jobs"

    headers = {
        "X-API-Key": BA_JOBS_API_KEY,
        "Accept": "application/json"
    }

    params = {
        "was": keyword,
        "wo": location,
        "page": page,
        "size": size
    }

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(
                url,
                headers=headers,
                params=params
            )
            response.raise_for_status()
            return response.json()
    except httpx.TimeoutException as exc:
        print(f"[LearnoryX] Germany jobs request timed out: {exc}")
        return {"stellenangebote": []}
    except httpx.HTTPStatusError as exc:
        print(f"[LearnoryX] Germany jobs HTTP error: {exc}")
        return {"stellenangebote": []}
    except Exception as exc:
        print(f"[LearnoryX] Germany jobs service error: {exc}")
        return {"stellenangebote": []}