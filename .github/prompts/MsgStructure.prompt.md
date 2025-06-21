---
mode: agent
---
Agent系统最终调用LLM时，messages的结构我的设计如下：

messages采用固定长度，每次向LLM传入时都是一条总的Prompt，包括临时记忆，以及历史执行步骤。

每次LLM返回后，更新总Prompt中的占位符部分。