import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

load_dotenv(Path(__file__).resolve().with_name(".env"))

GOOGLE_API_KEY = (
    os.getenv("GOOGLE_API_KEY")
    or os.getenv("GEMMA_API_KEY")
    or os.getenv("GEMMA_API")
)

client = None

if GOOGLE_API_KEY:
    try:
        client = genai.Client(api_key=GOOGLE_API_KEY)
    except Exception as exc:
        print(f"[LearnoryX] Gemma client initialization failed: {exc}")
        client = None


def _normalize_model_name(name: str) -> str:
    if not name:
        return "gemma-4-31b-it"
    return str(name).strip().split("/")[-1]


def get_supported_gemma_model() -> str:
    preferred = [
        "gemma-4-31b-it",
        "gemma-4-26b-a4b-it",
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        "gemini-2.5-pro",
    ]

    if client is None:
        return preferred[0]

    try:
        model_list = client.models.list()
        available = []

        if hasattr(model_list, "items"):
            available = [
                _normalize_model_name(getattr(item, "name", str(item)))
                for item in model_list.items
            ]
        elif isinstance(model_list, list):
            available = [
                _normalize_model_name(getattr(item, "name", str(item)))
                for item in model_list
            ]
        elif isinstance(model_list, dict):
            available = [
                _normalize_model_name(str(item))
                for item in model_list.get("models", [])
            ]

        available_text = " ".join(available).lower()

        for candidate in preferred:
            if candidate.lower() in available_text:
                return candidate

    except Exception as exc:
        print(f"[LearnoryX] Could not inspect Gemma models: {exc}")

    return preferred[0]


async def ask_gemma(prompt: str) -> str:
    if client is None:
        raise RuntimeError("GOOGLE_API_KEY is missing from environment")

    preferred_models = []
    preferred_models.append(get_supported_gemma_model())

    for candidate in [
        "gemma-4-31b-it",
        "gemma-4-26b-a4b-it",
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        "gemini-2.5-pro",
    ]:
        if candidate not in preferred_models:
            preferred_models.append(candidate)

    last_error = None

    for model_name in preferred_models:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            if hasattr(response, "text") and response.text:
                return str(response.text).strip()

            if isinstance(response, dict):
                text = response.get("text") or response.get("candidates")
                if text:
                    return str(text).strip()
                return str(response).strip()

            return str(response).strip()

        except Exception as exc:
            last_error = exc
            print(f"[LearnoryX] Model {model_name} failed: {exc}")

    raise RuntimeError(f"Gemma request failed: {last_error}") from last_error