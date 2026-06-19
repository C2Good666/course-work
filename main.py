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


def main():

    # =========================
    # 1. RAG初始化
    # =========================
    docs = load_pdf("data/test.pdf")
    chunks = split_docs(docs)

    embedding = get_embedding()
    db = build_vectorstore(chunks, embedding)

    print("✔ 系统初始化完成")

    # =========================
    # 2. 初始化Agent
    # =========================
    agent = SimpleAgent()

    # =========================
    # 3. 交互循环
    # =========================
    while True:

        # ✅ Step 1：用户输入（必须最先）
        query = input("\n请输入问题：")

        # ⏱ 计时开始
        start_time = time.time()

        # 🧠 Step 2：Agent路由
        route = agent.route(query)

        # 🧠 Agent日志
        print("\n🧠 Agent Decision Log")
        print("----------------------")
        print("Query:", query)
        print("Route:", route)

        # 📌 TOOL LOG
        print("\n📌 TOOL LOG")
        print("Query:", query)
        print("Route:", route)

        # =========================
        # 4. Tool执行
        # =========================
        if route == "calculator":
            result = calculator_tool(query)

        elif route == "time":
            result = time_tool()

        else:
            result = rag_tool(db, query)

        # ⏱ 计时结束
        end_time = time.time()

        # =========================
        # 5. JSON LOG
        # =========================
        log = {
            "query": query,
            "route": route,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "latency": round(end_time - start_time, 4)
        }

        print("\n📦 JSON LOG")
        print(json.dumps(log, indent=2, ensure_ascii=False))

        # =========================
        # 6. 输出结果
        # =========================
        print("\n💡回答：\n", result)
        print(f"\n⏱耗时: {round(end_time - start_time, 2)}s")
        print("-" * 40)


if __name__ == "__main__":
    main()