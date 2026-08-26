from google import genai
import json
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_movie_review(name, description):

    
    prompt = f"""
Analyze this movie or TV series based only on the information provided.

Title: {name}

Description:
{description}

Return the result in this exact JSON structure:

{{
    "ai_rating": 0,
    "overview": "",
    "strengths": [],
    "weaknesses": [],
    "recommended_for": []
}}

Rules:
- ai_rating must be a number between 0 and 10
- overview must be informative and moderately detailed, around 80 to 120 words
- Do not invent specific facts, actors, scenes, awards, or events that are not supported by the provided description
- strengths must contain 3 to 5 items
- weaknesses must contain 2 to 4 items
- recommended_for must contain 2 to 4 types of viewers
- return ONLY valid JSON
- do not use Markdown
- do not use ```json
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )


    return json.loads(response.text)


