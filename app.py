import streamlit as st
import time
import json

from rag.loader import load_pdf
from rag.splitter import split_docs
from rag.embedding import get_embedding
from rag.vectorstore import build_vectorstore

from core.agent import SimpleAgent
from tools.calculator import calculator_tool
from tools.time_tool import time_tool
from tools.rag_tool import rag_tool


# =========================
# 初始化系统
# =========================
@st.cache_resource
def init_system():
    docs = load_pdf("data/test.pdf")
    chunks = split_docs(docs)

    embedding = get_embedding()
    db = build_vectorstore(chunks, embedding)

    agent = SimpleAgent()

    return db, agent


db, agent = init_system()


# =========================
# UI基础配置
# =========================
st.set_page_config(page_title="RAG Agent", layout="wide")

st.title("🧠 RAG + Agent System (Enhanced UI)")
st.caption("AI系统：Agent路由 + RAG检索 + Tool调用")


query = st.text_input("请输入问题：")


# =========================
# 主逻辑
# =========================
if query:

    start_time = time.time()

    route = agent.route(query)

    docs = None

    # =========================
    # tool执行
    # =========================
    docs = None

    if route == "calculator":
        result = calculator_tool(query)

    elif route == "time":
        result = time_tool()

    elif route == "rag":
        result, docs = rag_tool(db, query)

    elif route == "unknown":
        result = "Sorry, I cannot understand this question. Please ask a question related to the uploaded document, time, or calculation."
        docs = None

    elif route == "no_answer":
        result = "我无法确定该问题的答案，请提供更多信息。"
        docs = None

    else:
        result = "Sorry, this question is outside the supported scope of the system."
        docs = None

    end_time = time.time()


    # =========================
    # 3列布局（核心升级🔥）
    # =========================
    col1, col2, col3 = st.columns(3)


    # -------------------------
    # 🧠 Agent Column
    # -------------------------
    with col1:
        st.markdown("## 🧠 Agent")

        st.metric("Route", route)

        st.markdown("### Reasoning Path")

        reasoning_path = [
            "User Input",
            "Lowercase Processing",
            "Intent Matching",
            f"Selected: {route}"
        ]

        for step in reasoning_path:
            st.write("➡️", step)


    # -------------------------
    # 💡 Answer Column
    # -------------------------
    with col2:
        st.markdown("## 💡 Answer")

        st.success(result)

        st.markdown("### ⏱ Latency")
        st.info(f"{round(end_time - start_time, 4)} s")


    # -------------------------
    # 📚 RAG Column
    # -------------------------
    with col3:
        st.markdown("## 📚 RAG Results")
        if docs:
            for i, doc in enumerate(docs[:3]):
                st.markdown(f"### Chunk {i+1}")
                st.write(doc["content"][:200])

                source = doc.get("source", "data/test.pdf")
                st.caption(f"📁 {source}")
        else:
            st.write("No RAG used")


    # =========================
    # JSON LOG（底部）
    # =========================
    st.markdown("---")
    st.markdown("## 📦 JSON Log")

    log = {
        "query": query,
        "route": route,
        "latency": round(end_time - start_time, 4)
    }

    st.json(log)