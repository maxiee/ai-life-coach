"""
工具描述格式规范

每个工具按照以下格式描述，确保小模型能够清晰理解：

### 工具名称: 简洁功能描述
**何时使用**: 具体使用场景
**输入参数**:
- 参数1: 描述
- 参数2: 描述
**输出**: 返回内容描述
**示例**: 简单使用示例

"""

# 工具模板
TOOL_TEMPLATE = """### {tool_name}: {description}
**何时使用**: {when_to_use}
**输入参数**: 
{parameters}
**输出**: {output}
**示例**: {example}
"""

# 示例工具描述
EXAMPLE_TOOLS = """
### save_user_info: 保存用户个人信息
**何时使用**: 用户首次提供个人信息时
**输入参数**: 
- info_type: 信息类型(个人资料/目标/问题等)
- content: 具体信息内容
**输出**: 保存确认消息
**示例**: save_user_info("个人资料", "25岁程序员，想转行")

### get_user_history: 获取用户历史记录
**何时使用**: 需要了解用户过往咨询记录时
**输入参数**: 
- query_type: 查询类型(全部/最近/特定主题)
- limit: 返回条数限制
**输出**: 历史记录列表
**示例**: get_user_history("最近", 5)

### search_advice: 搜索相关建议
**何时使用**: 需要查找特定主题的建议时
**输入参数**: 
- topic: 搜索主题
- context: 用户具体情况
**输出**: 相关建议列表
**示例**: search_advice("职业规划", "程序员转行")
"""


def format_tool_description(
    tool_name, description, when_to_use, parameters, output, example
):
    """
    格式化工具描述

    Args:
        tool_name: 工具名称
        description: 功能描述
        when_to_use: 使用场景
        parameters: 参数列表(字典格式)
        output: 输出描述
        example: 使用示例

    Returns:
        格式化的工具描述字符串
    """
    # 格式化参数列表
    param_lines = []
    for param, desc in parameters.items():
        param_lines.append(f"- {param}: {desc}")
    parameters_str = "\n".join(param_lines)

    return TOOL_TEMPLATE.format(
        tool_name=tool_name,
        description=description,
        when_to_use=when_to_use,
        parameters=parameters_str,
        output=output,
        example=example,
    )


def generate_tools_section(tools_list):
    """
    生成完整的工具部分，用于插入到主prompt的占位符中

    Args:
        tools_list: 工具描述列表

    Returns:
        完整的工具部分字符串
    """
    return "\n".join(tools_list)
