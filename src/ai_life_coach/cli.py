import os
import sys

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AI_LIFE_COACH_KEY", ""), base_url="https://api.siliconflow.cn/v1"
)

model_Qwen3_30B_A3B = "Qwen/Qwen3-30B-A3B"


def chat(messages, model=model_Qwen3_30B_A3B):
    """与AI模型进行对话

    Args:
        messages: 对话消息列表
        model: 使用的AI模型

    Returns:
        AI模型的回复
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=2048,
        temperature=0.7,
    )
    return response.choices[0].message.content


def main():
    """主函数，处理命令行输入"""
    input_str = input("> ")
    messages = [{"role": "user", "content": input_str}]
    try:
        response = chat(messages)
        print(response)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
