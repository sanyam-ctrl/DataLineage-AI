from google import genai
from dotenv import load_dotenv
import os

from app.schemas.ai_itinerary import AIItineraryResponse

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(prompt: str) -> str:
    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=prompt,
    )

    return interaction.output_text


def generate_structured_itinerary(
    prompt: str
) -> AIItineraryResponse:

    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=prompt,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": AIItineraryResponse.model_json_schema(),
        },
    )

    return AIItineraryResponse.model_validate_json(
        interaction.output_text
    )