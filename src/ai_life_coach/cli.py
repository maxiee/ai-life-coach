from smolagents import OpenAIServerModel, CodeAgent
import os


def main():

    model = OpenAIServerModel(
        api_base="https://api.siliconflow.cn/v1",
        model_id=os.getenv("AI_LIFE_COACH_MODEL", ""),
        api_key=os.getenv("AI_LIFE_COACH_KEY"),
    )

    agent = CodeAgent(tools=[], model=model)

    result = agent.run("计算从0到10之和")
    print(result)
