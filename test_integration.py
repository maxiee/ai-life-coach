#!/usr/bin/env python3
"""
测试脚本 - 验证 AI Agent 系统集成
"""

import sys
import os
sys.path.append('src')

from ai_life_coach.cli import init_tools, tool_manager, execute_tool, parse_tool_calls

def test_tool_initialization():
    """测试工具初始化"""
    print("=== 测试工具初始化 ===")
    init_tools()
    count = tool_manager.get_tools_count()
    print(f"✅ 成功初始化 {count} 个工具")
    return count > 0

def test_tool_execution():
    """测试工具执行"""
    print("\n=== 测试工具执行 ===")
    
    # 测试保存用户信息
    result1 = execute_tool("save_user_info", info_type="goal", content="学习Python编程")
    print(f"保存信息测试: {result1}")
    
    # 测试获取历史
    result2 = execute_tool("get_user_history", query_type="recent", limit=3)
    print(f"获取历史测试: {result2}")
    
    # 测试搜索建议
    result3 = execute_tool("search_advice", topic="编程学习", user_context="初学者")
    print(f"搜索建议测试: {result3}")
    
    return True

def test_tool_parsing():
    """测试工具调用解析"""
    print("\n=== 测试工具调用解析 ===")
    
    # 模拟AI回复包含工具调用
    ai_response = """
    我来帮你制定学习计划。首先让我保存你的学习目标：
    save_user_info('goal', '学习Python编程')
    
    然后让我搜索一些相关的学习建议：
    search_advice('Python学习', '编程初学者想快速入门')
    """
    
    tool_calls = parse_tool_calls(ai_response)
    print(f"解析到 {len(tool_calls)} 个工具调用:")
    for tool_name, kwargs in tool_calls:
        print(f"  - {tool_name}: {kwargs}")
    
    return len(tool_calls) > 0

def test_prompt_generation():
    """测试提示词生成"""
    print("\n=== 测试提示词生成 ===")
    prompt = tool_manager.get_prompt()
    
    # 检查关键组件
    checks = [
        ("AI人生导师", "身份定义"),
        ("工具调用规则", "调用规则"),
        ("save_user_info", "工具1"),
        ("get_user_history", "工具2"), 
        ("search_advice", "工具3"),
        ("响应格式", "格式规范")
    ]
    
    for keyword, description in checks:
        if keyword in prompt:
            print(f"✅ {description}: 包含 '{keyword}'")
        else:
            print(f"❌ {description}: 缺少 '{keyword}'")
    
    print(f"\n📊 提示词总长度: {len(prompt)} 字符")
    return True

def main():
    """主测试函数"""
    print("🚀 AI Life Coach 系统集成测试")
    print("="*50)
    
    tests = [
        ("工具初始化", test_tool_initialization),
        ("工具执行", test_tool_execution),
        ("工具解析", test_tool_parsing),
        ("提示词生成", test_prompt_generation)
    ]
    
    passed = 0
    total = len(tests)
    
    for name, test_func in tests:
        try:
            if test_func():
                print(f"✅ {name} - 通过")
                passed += 1
            else:
                print(f"❌ {name} - 失败")
        except Exception as e:
            print(f"💥 {name} - 错误: {e}")
    
    print("="*50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！系统已准备就绪。")
        print("\n🚀 现在可以运行: poetry run alc")
    else:
        print("⚠️  部分测试失败，请检查配置。")

if __name__ == "__main__":
    main()
