# AI agent & Local MCP

## 从0开始构建 100% 的本地 AI Agent Examples
1. [Building a 100% Local MCP Client with Ollama: Secure and Private AI Tool Integration](https://atalupadhyay.wordpress.com/2025/05/21/building-a-100-local-mcp-client-with-ollama-secure-and-private-ai-tool-integration/)
2. [Building a 100% local MCP Client
](https://blog.dailydoseofds.com/p/building-a-100-local-mcp-client)

## MCP 架构
一套 MCP 体系由两大核心部分组成：

    MCP Server：把外部 API、数据库或任意数据源包装成 MCP 工具，并开放给客户端调用；当客户端发起请求时，由 Server 实际执行对应函数。
    MCP Client：被 AI 应用或智能体用来与 MCP Server 通信，负责发现 Server 提供的工具并触发函数调用。

## Agent Function call
① 什么是 function calling？

    大模型不仅能「说话」，还能「动手」：
    当用户问「北京现在多少度？」，模型不会直接编一个温度，而是返回一条指令：
    call: get_weather(city="北京")
    你的代码收到这条指令，去调真正的天气 API，再把结果给模型，让它用自然语言回答。

② 为什么「必须支持」？

    如果模型不会发这种指令（很多旧版开源模型就不会），那 FunctionAgent 就收不到工具调用，整个自动流程就断了。
    支持 function calling 的模型会在训练时被教会「识别何时调函数 + 按 JSON 格式输出参数」。

## LlamaIndex 
[LlamaIndex](https://docs.llamaindex.ai/en/stable/) is the leading framework for building LLM-powered agents over your data with LLMs and workflows.


## Other function call

