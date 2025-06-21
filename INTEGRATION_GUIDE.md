# 🚀 AI Life Coach 快速使用指南

## 📋 系统已集成完成！

你的 AI Agent 系统已经成功集成到 `cli.py` 中，具备以下功能：

### ✅ 已实现功能

1. **优化的 AI Agent Prompt** - 小模型友好的结构化指令
2. **统一工具管理系统** - 动态工具加载和管理
3. **智能工具调用** - 自动解析和执行工具
4. **对话式交互** - 持续对话历史管理
5. **模拟工具执行** - 完整的工具调用演示

### 🎯 当前工具集

- `save_user_info` - 保存用户信息
- `get_user_history` - 获取历史记录
- `search_advice` - 搜索专业建议

## 🚀 运行方式

### 方法1：直接启动（推荐）
```bash
cd /Volumes/ssd/Code/ai-life-coach
poetry run alc
```

### 方法2：测试模式
```bash
# 运行集成测试
python test_integration.py

# 运行功能演示
python demo.py
```

## 💬 使用示例

启动后，你可以这样与AI对话：

```
👤 你: 我想学习Python编程，但不知道从哪开始

🤖 AI导师: 我来帮你制定学习计划...
🔧 执行工具...
   调用 save_user_info...
   ✅ 已保存goal信息: 学习Python编程...
   调用 search_advice...
   ✅ 💡 关于'Python学习'的建议...

🎯 最终建议: 基于你的情况，我建议...
```

## 🔧 系统架构

```
cli.py (主入口)
├── 工具管理器 (ToolManager)
├── 工具执行器 (execute_tool)
├── 工具解析器 (parse_tool_calls)
└── 对话处理器 (process_with_tools)
```

## 📝 下一步扩展

### 1. 添加真实工具
将 `execute_tool` 中的模拟函数替换为真实的数据库操作、API调用等。

### 2. 改进工具解析
当前使用简单正则表达式，可以升级为更智能的解析方法。

### 3. 添加更多工具
使用 `tool_manager.add_tool()` 轻松添加新工具。

### 4. 持久化存储
添加数据库支持，保存用户信息和对话历史。

## 🎉 现在就试试吧！

```bash
poetry run alc
```

然后尝试这些问题：
- "我想改变职业方向"
- "帮我制定学习计划"
- "我感到很焦虑，该怎么办"
- "我的时间管理有问题"

系统会自动选择合适的工具来帮助你！
