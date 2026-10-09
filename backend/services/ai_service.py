import os
from groq import Groq


def generate_climate_recommendations(
    city: str,
    weather: dict,
    climate_risk: dict
):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing from the environment."
        )

    client = Groq(api_key=api_key)

    prompt = f"""
You are ClimateOS, a climate intelligence assistant.

Analyze the supplied weather data and calculated risk results.

Location: {city}
Weather data: {weather}
Calculated climate risks: {climate_risk}

Rules:
1. Use only the supplied data.
2. Do not invent measurements, forecasts, or statistics.
3. Explain the detected risks in simple English.
4. Give 3 practical, affordable climate-related actions.
5. Distinguish current weather conditions from long-term climate change.
6. Do not claim that one weather observation proves climate change.
7. If data is missing, clearly mention it.
8. For emergencies, advise users to follow official local authorities.

Return these sections:
- Weather Summary
- Risk Explanation
- Recommended Actions
- Data Limitations
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You provide careful, evidence-based climate "
                    "information. Never invent data."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=700
    )

    return response.choices[0].message.content