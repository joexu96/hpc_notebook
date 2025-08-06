# 抱抱脸的MCP 单元小测

## MCP 的概念与术语

Q1. MCP的主要目的是什么?

A. 限制 AI 模型的训练数据
B. 使 AI 模型能够和外部数据源,工具和环境链接
C. 替代使用大语言模型时的 Prompt
D. 为 AI 创建一种新的编程语言

Q2. MCP 首要解决什么问题

A. 缺乏 AI 模型
B. 训练大语言模型的高昂成本
C. M x N 的集成问题
D. 创建新 AI 算法的困难

Q3. 以下哪项是 MCP 的关键优势?

A. 降低 AI 模型精度
B. 增加 AI 开发的复杂度
C. 在 AI 生态中实现标准化和互操作性
D. 将 AI 模型和外部系统隔离

Q4. 在 MCP 架构里, Host 指的是什么?

A. 暴露能力的外部程序
B. 只面向用户的 AI 应用
C. 只读数据源
D. 交互据的预定义模板

Q5. 在 AI 应用背景下, "M x N 集成问题"指的是什么?

A. 用N个数据训练M个模型的困难
B. 在没有标准的情况下, 把 M 个 AI 应用连接到 N 个外部工具所面临的挑战
C. 在 N 个应用中管理 M 个用户的问题
D. 为 N 个不同用户群体开发 M 项功能的复杂性

## MCP SDK

Q1：MCP SDK 的主要用途是什么？  
A. 定义 MCP 协议规范  
B. 简化 MCP 客户端与服务器的实现  
C. 为 MCP 交互提供可视化界面  
D. 取代编程语言  

Q2：以下哪项功能通常由 MCP SDK 处理？  
A. 优化 MCP 服务器  
B. 定义新的 AI 算法  
C. 消息的序列化/反序列化 
D. 托管大语言模型  

Q3：根据所给文本，哪家公司维护 MCP 的官方 Python SDK？  
A. Google  
B. Anthropic   
C. Microsoft  
D. JetBrains  

Q4：使用名为 server.py 的 Python 文件启动开发版 MCP 服务器应执行哪条命令？  
A. python server.py run  
B. mcp start server.py  
C. mcp dev server.py 
D. serve mcp server.py  

Q5：JSON-RPC 2.0 在 MCP 中扮演什么角色？  
A. 作为远程通信的主要传输机制  
B. 作为客户端与服务器之间所有通信的消息格式 
C. 作为调试 AI 模型的工具  
D. 作为定义 AI 能力（工具与资源）的方法

## 单元小测

Q1. 以下哪一项不是课程材料中描述的四种主要 MCP 能力类型之一？
A. 工具（Tools）
B. 资源（Resources）
C. 提示（Prompts）
D. 控制器（Controllers）  

Q2. 在 Host 与 Server 之间，MCP 是如何解决安全问题的？
A. MCP 提供了自己内置的身份验证系统。
B. 所有安全事务都由操作系统负责。
C. MCP 使用一台中央安全服务器进行所有身份验证。
D. MCP 依赖传输层安全和应用层机制。

Q3. MCP Sampling 提供了什么独特能力？
A. 生成用于 MCP Tools 的随机测试数据
B. 允许 Server 触发 Host 端的 LLM 调用 
C. 提供 Tool 使用情况的统计分析
D. 启用常见 Tool 结果的缓存

Q4. 如何将遗留系统（legacy system）接入 MCP 生态？
A. 用完全符合 MCP 的新系统替换遗留系统
B. 让 AI 应用直接查询遗留系统
C. 构建一个 MCP Server 适配器来封装遗留系统
D. 遗留系统无法接入 MCP

Q5. 为了最大化复用性，设计 MCP Tool 的最佳做法是什么？
A. 创建大型、复杂的工具，一次性处理多种操作
B. 设计粒度细小、只执行单一逻辑操作的工具
C. 构建与特定数据源紧耦合的工具
D. 尽量避免对工具进行参数化

Q6. 在 Gradio 的 MCP 集成中，把 mcp_server=True 会发生什么？
A. 不会生效，因为 Gradio 不支持 MCP
B. 为 MCP 客户端创建独立的 Web 界面
C. Gradio 函数会被自动转换成 MCP Tools
D. 启用 MCP 但需手动配置每个工具

Q7. mcp dev 与正式生产 MCP 服务器部署的主要区别是什么？
A. mcp dev 提供自动重载和详细日志，生产部署注重稳健性与可扩展性
B. mcp dev 仅支持 Python，生产环境可用任何语言
C. mcp dev 无法处理真实用户请求
D. 没有显著区别；mcp dev 可直接用于生产

Q8. 根据课程资料，哪种 MCP 传输方式最适合多客户端场景？
A. stdio 传输，因为它更安全
B. HTTP+SSE/Streamable HTTP，因为它能跨网络工作
C. WebSockets，因为它比 HTTP 更快
D. stdio 与 HTTP+SSE 在所有场景下都同样适用

Q9. 根据课程资料，Anthropic 官方维护的是哪个 SDK？
A. C# SDK
B. Python SDK
C. Swift SDK
D. Kotlin SDK

Q10. M×N 集成问题是 MCP 的重要推动力。若一家企业有 7 个 AI 应用，需与 12 个外部服务集成，请计算使用和不使用 MCP 时的集成数量。
A. 不使用 MCP：84 个；使用 MCP：19 个 
B. 不使用 MCP：84 个；使用 MCP：84 个，但 MCP 让构建更简单
C. 不使用 MCP：19 个；使用 MCP：84 个，MCP 增加开销
D. 无法计算，MCP 使用不同的消息总线