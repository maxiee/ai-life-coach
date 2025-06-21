"""
AI Agent 工具管理器

这个模块提供了简单的接口来管理和生成 AI Agent 的工具描述
"""

from .prompt_main import prompt_main
from .tool_format import format_tool_description


class ToolManager:
    """工具管理器，用于动态生成和管理 AI Agent 工具"""

    def __init__(self):
        self.tools = []

    def add_tool(self, name, description, when_to_use, parameters, output, example):
        """
        添加一个工具

        Args:
            name: 工具名称
            description: 功能描述
            when_to_use: 使用场景
            parameters: 参数字典 {参数名: 描述}
            output: 输出描述
            example: 使用示例
        """
        tool_desc = format_tool_description(
            tool_name=name,
            description=description,
            when_to_use=when_to_use,
            parameters=parameters,
            output=output,
            example=example,
        )
        self.tools.append(tool_desc)
        return tool_desc

    def remove_tool(self, name):
        """根据工具名称移除工具"""
        self.tools = [
            tool for tool in self.tools if not tool.startswith(f"### {name}:")
        ]

    def get_prompt(self):
        """生成包含所有工具的完整 prompt"""
        tools_section = "\n".join(self.tools)
        return prompt_main.format(tools_placeholder=tools_section)

    def clear_tools(self):
        """清空所有工具"""
        self.tools = []

    def get_tools_count(self):
        """获取工具数量"""
        return len(self.tools)


# 预定义的常用工具集合
def create_basic_life_coach_tools():
    """创建基础人生导师工具集"""
    manager = ToolManager()

    # 用户信息管理工具
    manager.add_tool(
        name="save_user_info",
        description="保存用户信息",
        when_to_use="用户提供新信息时",
        parameters={
            "info_type": "信息类型(profile/goal/problem)",
            "content": "信息内容",
        },
        output="保存确认",
        example="save_user_info('goal', '想在一年内转行到数据科学')",
    )

    # 历史记录查询工具
    manager.add_tool(
        name="get_history",
        description="获取用户历史",
        when_to_use="需要了解用户背景时",
        parameters={"query_type": "查询类型(recent/all)", "limit": "数量限制"},
        output="历史记录",
        example="get_history('recent', 3)",
    )

    # 建议搜索工具
    manager.add_tool(
        name="search_advice",
        description="搜索相关建议",
        when_to_use="需要专业建议时",
        parameters={"topic": "主题关键词", "context": "用户情况"},
        output="建议列表",
        example="search_advice('职业规划', '程序员3年经验')",
    )

    return manager


# 使用示例
if __name__ == "__main__":
    # 方式1：使用预定义工具集
    basic_manager = create_basic_life_coach_tools()
    print("=== 基础工具集 Prompt ===")
    print(basic_manager.get_prompt())
    print(f"\n工具数量: {basic_manager.get_tools_count()}")

    # 方式2：自定义工具集
    custom_manager = ToolManager()
    custom_manager.add_tool(
        name="mood_analysis",
        description="分析用户情绪",
        when_to_use="用户表达情感时",
        parameters={"message": "用户消息"},
        output="情绪分析结果",
        example="mood_analysis('我最近很焦虑')",
    )

    print("\n=== 自定义工具集 Prompt ===")
    print(custom_manager.get_prompt())
