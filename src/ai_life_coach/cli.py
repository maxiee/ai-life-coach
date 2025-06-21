from smolagents import OpenAIServerModel, CodeAgent, tool
import os
import sys


@tool
def get_user_input(prompt: str = "> ") -> str:
    """获取用户输入

    Args:
        prompt: 显示给用户的提示符

    Returns:
        用户输入的字符串，如果用户中断则返回 'exit'
    """
    try:
        user_input = input(prompt).strip()
        return user_input
    except (KeyboardInterrupt, EOFError):
        return "exit"


@tool
def display_message(message: str) -> str:
    """显示消息给用户

    Args:
        message: 要显示给用户的消息内容

    Returns:
        确认消息已显示的字符串
    """
    print(message)
    return "消息已显示"


@tool
def should_continue_conversation(user_message: str) -> bool:
    """判断是否应该继续对话，如果用户想要退出则返回False

    Args:
        user_message: 用户输入的消息内容

    Returns:
        如果应该继续对话返回True，如果用户想退出返回False
    """
    exit_keywords = ["exit", "quit", "bye", "退出", "再见", "结束", "停止"]
    return user_message.lower() not in exit_keywords


def main():
    # 检查必要的环境变量
    if not os.getenv("AI_LIFE_COACH_KEY"):
        print("错误：请设置 AI_LIFE_COACH_KEY 环境变量")
        return

    if not os.getenv("AI_LIFE_COACH_MODEL"):
        print("错误：请设置 AI_LIFE_COACH_MODEL 环境变量")
        return

    try:
        model = OpenAIServerModel(
            api_base="https://api.siliconflow.cn/v1",
            model_id=os.getenv("AI_LIFE_COACH_MODEL", ""),
            api_key=os.getenv("AI_LIFE_COACH_KEY", ""),
        )

        # 为Agent提供工具
        tools = [get_user_input, display_message, should_continue_conversation]
        agent = CodeAgent(tools=tools, model=model)

        # 初始提示
        print("你好，我是你的 AI 人生教练。有什么可以帮到你吗？")
        print("(输入 'exit', 'quit', 'bye', '退出' 等退出程序)")
        print("-" * 50)

        # 让Agent控制对话循环
        initial_prompt = """
你是一个AI人生教练。请使用提供的工具来与用户进行对话：

1. 使用 get_user_input() 获取用户输入
2. 使用 display_message() 向用户显示回复
3. 使用 should_continue_conversation() 检查用户是否想要退出

请开始与用户对话，持续进行直到用户表示想要退出。对每个用户输入都要给出有帮助的回复。
"""

        result = agent.run(initial_prompt)
        print(f"\n对话结束")

    except Exception as e:
        print(f"初始化模型时出错：{e}")
        print("请检查网络连接和API配置是否正确")
