# Rag Architecture

مفاهیم بنیادین، آناتومی سه‌گانه Retrieval-Augmented Generation و پیاده‌سازی خط‌لوله با LCEL در LangChain.

## Scripts & Notebooks
- [`01_rag_architecture_and_lcel.ipynb`](./01_rag_architecture_and_lcel.ipynb): تمثیل آزمون کتاب‌باز در برابر آزمون حفظی، چرخه گام‌به‌گام سوال تا پاسخ مستند، راه‌اندازی پایگاه برداری Chroma و تبدیل به `Retriever` با `as_retriever(search_kwargs={"k": 3})`، مهندسی پرامپت RAG برای کنترل توهم، ساخت زنجیره مدرن با LCEL (`{"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()`)، راستی‌آزمایی پاسخگویی و تست عدم توهم برای سوال ناموجود، و کالبدشکافی ۳ نقطه‌ضعف مرگبار سیستم‌های Naive RAG (شامل Semantic Drift، Lost in the Middle و Redundancy).