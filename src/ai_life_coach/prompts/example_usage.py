"""
使用示例：如何生成完整的 AI Agent Prompt

这个文件展示了如何使用工具格式规范来生成完整的 prompt
"""

from .prompt_main import prompt_main
from .tool_format import format_tool_description, generate_tools_section


def create_complete_prompt():
    """
    创建包含所有工具的完整 prompt
    """
    # 定义你的工具
    tools = []

    # 工具1：保存用户信息
    tool1 = format_tool_description(
        tool_name="save_user_info",
        description="保存用户个人信息到数据库",
        when_to_use="用户首次提供个人信息或更新信息时",
        parameters={
            "info_type": "信息类型(profile/goal/problem/preference)",
            "content": "具体信息内容",
            "user_id": "用户唯一标识符",
        },
        output="保存成功确认和信息摘要",
        example="save_user_info('profile', '25岁程序员，想学习新技能', 'user123')",
    )
    tools.append(tool1)

    # 工具2：获取用户历史
    tool2 = format_tool_description(
        tool_name="get_user_history",
        description="获取用户的历史咨询记录",
        when_to_use="需要了解用户过往问题和建议时",
        parameters={
            "user_id": "用户唯一标识符",
            "query_type": "查询类型(recent/all/by_topic)",
            "limit": "返回记录数量限制(默认10)",
        },
        output="按时间排序的历史记录列表",
        example="get_user_history('user123', 'recent', 5)",
    )
    tools.append(tool2)

    # 工具3：搜索建议库
    tool3 = format_tool_description(
        tool_name="search_advice_db",
        description="从建议库中搜索相关建议",
        when_to_use="需要为特定问题查找专业建议时",
        parameters={
            "topic": "搜索主题关键词",
            "user_context": "用户具体情况描述",
            "advice_type": "建议类型(career/relationship/health/finance)",
        },
        output="相关建议列表和匹配度评分",
        example="search_advice_db('职业转行', '程序员5年经验', 'career')",
    )
    tools.append(tool3)

    # 工具4：设置提醒
    tool4 = format_tool_description(
        tool_name="set_reminder",
        description="为用户设置后续跟进提醒",
        when_to_use="给出建议后需要定期跟进时",
        parameters={
            "user_id": "用户唯一标识符",
            "reminder_text": "提醒内容",
            "schedule_time": "提醒时间(天数或具体日期)",
        },
        output="提醒设置成功确认",
        example="set_reminder('user123', '检查学习进度', '7天')",
    )
    tools.append(tool4)

    # 生成工具部分
    tools_section = generate_tools_section(tools)

    # 将工具部分插入到主prompt中
    complete_prompt = prompt_main.format(tools_placeholder=tools_section)

    return complete_prompt


# 使用示例
if __name__ == "__main__":
    # 生成完整的 prompt
    full_prompt = create_complete_prompt()
    print("=== 完整的 AI Agent Prompt ===")
    print(full_prompt)

    # 你也可以单独生成某个工具的描述
    single_tool = format_tool_description(
        tool_name="analyze_mood",
        description="分析用户当前情绪状态",
        when_to_use="用户表达情感或需要情绪支持时",
        parameters={"user_message": "用户的原始消息", "context": "对话上下文"},
        output="情绪分析结果和建议",
        example="analyze_mood('我最近压力很大', '工作相关咨询')",
    )
    print("\n=== 单个工具示例 ===")
    print(single_tool)
