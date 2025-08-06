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

对，就是这个「两段式推理」流程，只是 LlamaIndex 帮你把**两段**都自动化了。可以把它想成：

---

### 🔁 标准两段循环（伪代码）

1. **第一段推理**（模型决定要不要调工具）  
   ```
   LLM([user_msg]) → tool_call = {"name":"get_weather","arguments":{"city":"北京"}}
   ```

2. **FunctionAgent 执行**  
   ```
   result = get_weather("北京")  # 拿到实时天气
   ```

3. **第二段推理**（把用户消息 + 工具结果一起喂给模型）  
   ```
   LLM([
       user_msg,
       tool_call,
       tool_result
   ]) → "北京现在 28℃，晴朗。"
   ```

---

### ✅ LlamaIndex 的隐藏细节
- 它把 **用户消息 + 工具描述** 一次性塞进 prompt → 模型返回 tool_call  
- 自动执行工具 → 把 **工具输出** 追加到对话 → 再次调用模型 → 得到最终回答  
- 如果工具结果还不够，模型可以再发新的 tool_call，循环直到满意为止（所以可能是 N 段）。

---

### 📌 一句话记忆
> **FunctionAgent 就是「模型先想，再动手，再想」的循环；LlamaIndex 帮你串起了这两段（或多段）推理，你只需一句 `agent.chat()`。**

## LlamaIndex 
[LlamaIndex](https://docs.llamaindex.ai/en/stable/) is the leading framework for building LLM-powered agents over your data with LLMs and workflows.


## 本地小型 MCP 方案

### Tiny Agents （hf course 的 eaxmple
[50 行代码实现 AI agent](https://huggingface.co/blog/tiny-agents) 
相关包改到了 smolagents ，感觉可以用 Gradio + smolagents 快速实现。

### 