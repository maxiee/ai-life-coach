"""
演示脚本 - 展示 AI Agent 工具调用功能

这个脚本模拟用户输入，展示系统如何工作
"""

import sys
sys.path.append('src')

from ai_life_coach.cli import init_tools, tool_manager, execute_tool, parse_tool_calls

def demo_tool_calls():
    """演示工具调用功能"""
    print("🎭 AI Agent 工具调用演示")
    print("="*50)
    
    # 初始化工具
    init_tools()
    print(f"✅ 已加载 {tool_manager.get_tools_count()} 个工具\n")
    
    # 模拟AI回复场景
    scenarios = [
        {
            "user_input": "我想学习Python，但不知道从哪开始",
            "ai_response": """
**理解**: 你想学习Python编程，需要学习路径指导。

**行动**: 我先保存你的学习目标，然后搜索相关的学习建议。
save_user_info('goal', '学习Python编程，寻求学习路径指导')
search_advice('Python学习路径', '编程初学者想要系统学习')

**建议**: 基于搜索结果，我会为你制定详细的学习计划。

**下一步**: 请告诉我你的编程基础和可用学习时间。
            """
        },
        {
            "user_input": "我之前问过什么问题吗？",
            "ai_response": """
**理解**: 你想了解之前的咨询历史。

**行动**: 让我查看你的历史记录。
get_user_history('recent', 5)

**建议**: 我会根据历史记录为你提供连贯的建议。

**下一步**: 基于历史记录，我们可以继续深入讨论之前的话题。
            """
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"📋 场景 {i}: {scenario['user_input']}")
        print(f"🤖 AI回复:\n{scenario['ai_response'].strip()}")
        
        # 解析工具调用
        tool_calls = parse_tool_calls(scenario['ai_response'])
        
        if tool_calls:
            print(f"\n🔧 检测到 {len(tool_calls)} 个工具调用:")
            
            for tool_name, kwargs in tool_calls:
                print(f"   📞 调用: {tool_name}")
                print(f"   📝 参数: {kwargs}")
                
                # 执行工具
                result = execute_tool(tool_name, **kwargs)
                print(f"   ✅ 结果: {result}")
                print()
        
        print("="*50 + "\n")

def show_system_prompt():
    """显示完整的系统提示词"""
    print("📄 完整系统提示词:")
    print("="*50)
    prompt = tool_manager.get_prompt()
    print(prompt)
    print("="*50)

if __name__ == "__main__":
    # 运行演示
    demo_tool_calls()
    
    # 询问是否显示系统提示词
    show_prompt = input("是否查看完整的系统提示词? (y/n): ").lower()
    if show_prompt in ['y', 'yes', '是']:
        print()
        show_system_prompt()
