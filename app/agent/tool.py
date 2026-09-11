import logging

from langchain_core.tools import tool
from config import client


logger = logging.getLogger(__name__)


@tool
def create_activity(message: str):
    """Receive natural language input from the user."""

    logger.info("create_activity tool called")
    logger.debug("User message received: %s", message)

    system_prompt = """
    You are an activity extraction assistant.

    Convert the user's natural language into activity data.

    Required fields:
    - title
    - category
    - duration
    - start_time
    - end_time
    - activity_date

    Return ONLY valid JSON.
    """

    logger.debug("System prompt prepared")
    logger.info("Sending request to Groq")

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0
        )

        logger.info("Groq response received successfully")

        result = response.choices[0].message.content

        logger.debug("AI response: %s", result)

        return result

    except Exception:
        logger.exception("Error while calling Groq API")
        raise