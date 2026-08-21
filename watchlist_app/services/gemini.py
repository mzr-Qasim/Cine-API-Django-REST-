from google import genai
import json
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_movie_review(name, description):

    
    prompt = f"""
    Analyze this movie.

    Movie name: {name}

    Movie description:
    {description}

    Return the result in this exact JSON structure:

    {{
        "rating": 0,
        "short_review": "",
        "strengths": [],
        "weaknesses": []
    }}

    Rules:
    - rating must be a number between 0 and 10
    - short_review must be a concise paragraph
    - strengths must contain 3 to 5 items
    - weaknesses must contain 2 to 4 items
    - return ONLY valid JSON
    - do not use Markdown
    - do not use ```json
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )


    return json.loads(response.text)


