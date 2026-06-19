def rag_tool(db, query):

    docs = db.similarity_search(query, k=3)

    results = []

    for i, d in enumerate(docs):

        source = d.metadata.get("source", None)

        if source is None:
            source = d.metadata.get("file_path", None)

        if source is None:
            source = "data/test.pdf"

        results.append({
            "chunk_id": i + 1,
            "content": d.page_content,
            "source": source
        })

    context = "\n".join([r["content"] for r in results])

    return context, results