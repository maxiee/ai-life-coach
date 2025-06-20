from smolagents import LiteLLMModel
import os


def main():

    model = LiteLLMModel(
        model_id=os.getenv("AI_LIFE_COACH_MODEL"),
        tempurature=0.7,
        api_key=os.getenv("AI_LIFE_COACH_API_KEY"),
    )
