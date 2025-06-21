import os
import sys
import json
from openai import OpenAI
from .prompts.tool_manager import ToolManager
from .prompts.prompt_main import prompt_main

client = OpenAI(
    api_key=os.getenv("AI_LIFE_COACH_KEY", ""), base_url="https://api.siliconflow.cn/v1"
)

model_Qwen3_30B_A3B = "Qwen/Qwen3-30B-A3B"


# Global tool manager
tool_manager = ToolManager()


# 初始化基础工具集
def init_tools():
    """初始化AI生活导师的基础工具集"""

    # 模拟工具1：保存用户信息
    tool_manager.add_tool(
        name="save_user_info",
        description="保存用户个人信息",
        when_to_use="用户首次提供个人信息或更新信息时",
        parameters={
            "info_type": "信息类型(profile/goal/problem/preference)",
            "content": "具体信息内容",
        },
        output="保存成功确认和信息ID",
        example="save_user_info('goal', '我想在6个月内学会Python编程')",
    )

    # 模拟工具2：获取用户历史
    tool_manager.add_tool(
        name="get_user_history",
        description="获取用户的历史咨询记录",
        when_to_use="需要了解用户过往问题和建议历史时",
        parameters={
            "query_type": "查询类型(recent/all/by_topic)",
            "limit": "返回记录数量(默认5)",
        },
        output="按时间排序的历史记录列表",
        example="get_user_history('recent', 3)",
    )

    # 模拟工具3：搜索建议
    tool_manager.add_tool(
        name="search_advice",
        description="从知识库搜索相关建议",
        when_to_use="需要为特定问题查找专业建议时",
        parameters={"topic": "搜索主题关键词", "user_context": "用户具体情况描述"},
        output="相关建议列表和实用性评分",
        example="search_advice('时间管理', '上班族想提高工作效率')",
    )


# 模拟工具执行函数
def execute_tool(tool_name, **kwargs):
    """模拟工具执行，返回模拟结果"""
    if tool_name == "save_user_info":
        info_type = kwargs.get("info_type", "")
        content = kwargs.get("content", "")
        return f"✅ 已保存{info_type}信息: {content[:50]}... (ID: user_info_001)"

    elif tool_name == "get_user_history":
        query_type = kwargs.get("query_type", "recent")
        limit = kwargs.get("limit", 3)
        return f"📋 找到{limit}条{query_type}记录:\n1. 上次咨询职业规划问题\n2. 讨论学习方法\n3. 时间管理建议"

    elif tool_name == "search_advice":
        topic = kwargs.get("topic", "")
        context = kwargs.get("user_context", "")
        return f"💡 关于'{topic}'的建议:\n1. 制定明确的学习计划\n2. 采用番茄工作法\n3. 定期复习和反思\n(基于: {context})"

    else:
        return f"⚠️ 未知工具: {tool_name}"


# MsgStructure: maintain memory and steps as placeholders, always fill prompt_main
def build_system_prompt(memory, steps):
    """Build the system prompt with memory and steps placeholders."""
    tools_section = "\n".join(tool_manager.tools)
    return prompt_main.format(
        memory_placeholder=memory or "(empty)",
        steps_placeholder=steps or "(empty)",
        tools_placeholder=tools_section,
    )


def chat(user_input, memory, steps, model=model_Qwen3_30B_A3B):
    """Chat with the AI model using MsgStructure."""
    system_prompt = build_system_prompt(memory, steps)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=2048,
        temperature=0.7,
    )
    return response.choices[0].message.content


def parse_tool_calls(response_text):
    """解析AI回复中的工具调用（简单版本）"""
    tool_calls = []

    # 简单的工具调用检测（你可以根据需要改进这个解析逻辑）
    import re

    # 检测类似 save_user_info('goal', '我想学Python') 的调用
    patterns = [
        r"save_user_info\(['\"]([^'\"]+)['\"],\s*['\"]([^'\"]+)['\"]\)",
        r"get_user_history\(['\"]([^'\"]+)['\"],?\s*(\d+)?\)",
        r"search_advice\(['\"]([^'\"]+)['\"],\s*['\"]([^'\"]+)['\"]\)",
    ]

    for pattern in patterns:
        matches = re.findall(pattern, response_text)
        for match in matches:
            if "save_user_info" in pattern:
                tool_calls.append(
                    ("save_user_info", {"info_type": match[0], "content": match[1]})
                )
            elif "get_user_history" in pattern:
                limit = int(match[1]) if match[1] else 3
                tool_calls.append(
                    ("get_user_history", {"query_type": match[0], "limit": limit})
                )
            elif "search_advice" in pattern:
                tool_calls.append(
                    ("search_advice", {"topic": match[0], "user_context": match[1]})
                )

    return tool_calls


# MsgStructure: memory/steps are strings, not message lists
def process_with_tools(user_input, memory, steps):
    """Process user input, update memory and steps as MsgStructure placeholders."""
    # 1st round: send user_input, get AI response
    ai_response = chat(user_input, memory, steps)
    print(f"🤖 AI导师: {ai_response}")

    # Update steps with this round
    steps = (steps or "") + f"\n[User]: {user_input}\n[AI]: {ai_response}\n"

    # Check for tool calls
    tool_calls = parse_tool_calls(ai_response)
    if tool_calls:
        print("\n🔧 执行工具...")
        tool_results = []
        for tool_name, kwargs in tool_calls:
            print(f"   调用 {tool_name}...")
            result = execute_tool(tool_name, **kwargs)
            tool_results.append(f"工具 {tool_name} 结果: {result}")
            print(f"   ✅ {result}")
        # Feedback tool results to AI
        tool_feedback = "\n".join(tool_results)
        tool_feedback_input = (
            f"工具执行结果:\n{tool_feedback}\n\n请基于这些结果给出最终建议。"
        )
        final_response = chat(tool_feedback_input, memory, steps)
        print(f"\n🎯 最终建议: {final_response}")
        steps += f"[Tool]: {tool_feedback}\n[AI]: {final_response}\n"
        return memory, steps
    return memory, steps


def main():
    """Main function, handles CLI input and MsgStructure memory/steps."""
    init_tools()
    print("🌟 AI人生导师已启动！")
    print("💡 提示：你可以询问关于职业规划、学习方法、时间管理等问题")
    print("🔧 我会根据需要使用工具来更好地帮助你")
    print("👋 输入 'quit' 或 'exit' 退出\n")

    memory = ""  # Temporary memory placeholder
    steps = ""  # History steps placeholder

    while True:
        try:
            user_input = input("👤 你: ").strip()
            if user_input.lower() in ["quit", "exit", "退出"]:
                print("👋 再见！祝你生活愉快！")
                break
            if not user_input:
                continue
            print()
            memory, steps = process_with_tools(user_input, memory, steps)
            print("\n" + "=" * 50 + "\n")
        except KeyboardInterrupt:
            print("\n👋 再见！")
            break
        except Exception as e:
            print(f"❌ 错误: {e}", file=sys.stderr)
            print("请重试...\n")


if __name__ == "__main__":
    main()
