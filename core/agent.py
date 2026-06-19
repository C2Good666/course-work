class SimpleAgent:

    def route(self, query: str):

        q = query.lower().strip()

        print("DEBUG QUERY:", q)

        # 🧮 数学问题
        if any(op in q for op in ["+", "-", "*", "/"]):
            print("DEBUG: calculator hit")
            return "calculator"

        # ⏰ 时间问题
        if any(word in q for word in ["time", "时间", "now", "current"]):
            print("DEBUG: time hit")
            return "time"

        # 📚 RAG关键词匹配
        rag_keywords = [
            "jc3510",
            "what is",
            "what is this",
            "explain",
            "about",
            "course",
            "document",
            "pdf"
        ]

        hit_count = sum(1 for word in rag_keywords if word in q)

        print("DEBUG: rag keyword hits =", hit_count)

        if hit_count >= 1:
            print("DEBUG: rag hit")
            return "rag"

        # 🟡 边界增强：防止垃圾输入进RAG
        noise_patterns = [
            "asdf",
            "qwerty",
            "why you sunlight",
            "just come",
        ]

        if any(p in q for p in noise_patterns):
            print("DEBUG: unknown hit")
            return "unknown"

        # ❗关键修复：fallback 不再默认 rag
        print("DEBUG: fallback → unknown")
        return "unknown"