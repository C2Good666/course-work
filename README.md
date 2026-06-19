# 📚 RAG Agent 智能问答系统

## 📌 项目简介

本项目实现了一个基于 **Retrieval-Augmented Generation (RAG)** 的智能问答系统，结合向量数据库与大模型，实现对本地文档的语义检索与问答能力。

系统支持：
- PDF 文档解析与切分
- 向量化检索（Embedding）
- 向量数据库存储与召回
- 基于 Agent 的智能工具调用（RAG / Time / Calculator）
- 多工具协同推理问答

---

## 🧠 系统架构

```
用户问题
   ↓
Agent 调度层 (core/agent.py)
   ↓
工具选择（RAG / 时间 / 计算器）
   ↓
RAG 检索模块（rag/）
   ├── 文档加载 loader.py
   ├── 文本切分 splitter.py
   ├── 向量化 embedding.py
   └── 向量数据库 vectorstore.py
   ↓
大模型生成答案
```

---

## 📁 项目结构

```
rag_agent_project/
│
├── main.py
├── app.py
├── run.sh
├── requirements.txt
│
├── data/
│   └── test.pdf
│
├── core/
│   └── agent.py
│
├── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── embedding.py
│   ├── vectorstore.py
│
├── tools/
│   ├── rag_tool.py
│   ├── time_tool.py
│   ├── calculator.py
│
└── README.md
```

---

## ⚙️ 环境依赖

```bash
pip install -r requirements.txt
```

如果使用 HuggingFace embedding：

```bash
pip install sentence-transformers faiss-cpu
```

---

## 🚀 运行方式

### 1️⃣ 直接运行主程序

```bash
python main.py
```

### 2️⃣ 或启动测试接口

```bash
python app.py
```

---

## 💡 核心功能说明

### 📌 1. RAG 检索问答
- PDF 文档切分 chunk
- embedding 向量化
- 向量数据库存储
- 相似度检索 + LLM 生成回答

---

### 📌 2. Agent 智能调度
系统自动判断问题类型：

| 类型 | 调用工具 |
|------|----------|
| 文档问答 | RAG |
| 数学计算 | Calculator |
| 时间查询 | Time Tool |

---

### 📌 3. 向量数据库
支持：
- FAISS 向量检索
- Cosine similarity
- 本地轻量存储

---

## 🧪 示例问题

```text
PDF讲了什么？
总结文档核心内容
现在几点？
计算 125 * 456
```

---

## 🧩 技术栈

- Python 3.10+
- RAG Pipeline
- SentenceTransformers
- FAISS
- Agent Tool Calling

---

## 📈 项目亮点

- ✔ 完整RAG流程（加载→切分→向量化→检索）
- ✔ Agent多工具调度系统
- ✔ 模块化工程设计
- ✔ 支持PDF真实问答
- ✔ 可扩展工具架构

---

## 👨‍💻 作者
华南师范大学阿伯丁数据科学与人工智能学院 ai1班陈段果
学号：20233801065



