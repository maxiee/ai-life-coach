# AI Agent Prompt 系统使用指南

## 概述

这个系统提供了一个优化的 AI Agent Prompt 框架，特别适合小模型进行工具调用。主要特点：

- 🎯 **小模型友好**: 简洁清晰的指令结构
- 🔧 **统一工具格式**: 标准化的工具描述模板
- 📝 **占位符设计**: 灵活的工具插入机制
- 🚀 **易于管理**: 简单的工具管理接口

## 文件结构

```
src/ai_life_coach/prompts/
├── prompt_main.py      # 主 Prompt 模板(包含占位符)
├── tool_format.py      # 工具格式规范
├── tool_manager.py     # 工具管理器
├── example_usage.py    # 使用示例
└── README.md          # 本文档
```

## 快速开始

### 1. 使用预定义工具集

```python
from ai_life_coach.prompts.tool_manager import create_basic_life_coach_tools

# 创建基础工具集
manager = create_basic_life_coach_tools()

# 获取完整的 prompt
complete_prompt = manager.get_prompt()
print(complete_prompt)
```

### 2. 自定义工具集

```python
from ai_life_coach.prompts.tool_manager import ToolManager

# 创建工具管理器
manager = ToolManager()

# 添加自定义工具
manager.add_tool(
    name="your_tool_name",
    description="工具功能描述",
    when_to_use="使用场景说明",
    parameters={
        "param1": "参数1描述",
        "param2": "参数2描述"
    },
    output="输出内容描述",
    example="your_tool_name('示例参数')"
)

# 生成完整 prompt
prompt = manager.get_prompt()
```

### 3. 动态管理工具

```python
# 添加工具
manager.add_tool(...)

# 移除工具
manager.remove_tool("tool_name")

# 清空所有工具
manager.clear_tools()

# 查看工具数量
count = manager.get_tools_count()
```

## 工具格式规范

每个工具必须包含以下字段：

- **name**: 工具名称(简洁明了)
- **description**: 功能描述(一句话说明)
- **when_to_use**: 使用场景(帮助模型判断何时调用)
- **parameters**: 参数列表(字典格式)
- **output**: 输出描述(说明返回什么)
- **example**: 使用示例(具体调用示例)

## Prompt 优化特点

### 1. 结构化设计
- 清晰的角色定义
- 明确的任务流程
- 标准化的响应格式

### 2. 小模型优化
- 简洁的语言表达
- 分步骤的工作流程
- 明确的工具选择规则

### 3. 工具调用优化
- 统一的工具描述格式
- 明确的使用场景说明
- 具体的调用示例

## 实际应用示例

```python
# 在你的 AI Agent 中使用
def create_agent_prompt(available_tools):
    manager = ToolManager()
    
    # 根据实际可用工具动态添加
    for tool_config in available_tools:
        manager.add_tool(**tool_config)
    
    return manager.get_prompt()

# 使用生成的 prompt
agent_prompt = create_agent_prompt(your_tools_config)
# 将 agent_prompt 发送给你的 AI 模型
```

## 测试运行

```bash
# 在项目根目录运行
poetry run python -c "
from src.ai_life_coach.prompts.tool_manager import create_basic_life_coach_tools
manager = create_basic_life_coach_tools()
print(manager.get_prompt())
"
```

## 自定义扩展

你可以根据需要：

1. 修改 `prompt_main.py` 中的基础模板
2. 在 `tool_format.py` 中调整工具格式
3. 创建特定领域的工具集合
4. 添加更多的预定义工具管理器

## 注意事项

- 保持工具描述简洁明了
- 确保参数说明具体清晰
- 提供有意义的使用示例
- 工具数量适中(建议10个以内)

这样的设计确保小模型能够：
- 快速理解工具功能
- 准确判断使用时机
- 正确调用工具参数
