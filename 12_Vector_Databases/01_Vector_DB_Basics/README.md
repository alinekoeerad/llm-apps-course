# Vector DB Basics

مفاهیم پایه و معماری پایگاه داده‌های برداری (Vector Databases).

## Scripts & Notebooks
- [`01_why_vector_databases.ipynb`](./01_why_vector_databases.ipynb): بررسی تفاوت جستجوی لغوی با معنایی، شکست SQL در جستجوی معنایی، بنچمارک مقیاس‌پذیری $O(N)$ و معرفی تکنیک ANN.
- [`02_vector_databases_architecture.ipynb`](./02_vector_databases_architecture.ipynb): معماری دیتابیس‌های برداری (Storage Layer در مقابل Index Layer)، تمثیل استادیوم، مقایسه الگوریتم‌های IVF و HNSW، مثلث مصالحه (Speed vs Recall vs Memory) و پیاده‌سازی عملی با ChromaDB و LangChain همراه با فیلترینگ متادیتا.
- [`03_similarity_metrics_and_spaces.ipynb`](./03_similarity_metrics_and_spaces.ipynb): ریاضیات شباهت، بررسی سه معیار اصلی (فاصله اقلیدسی $L_2$، شباهت کسینوسی و ضرب داخلی Dot Product)، علت خطای $L_2$ در NLP، و تنظیم فضای برداری (`hnsw:space`) در ChromaDB بومی و LangChain.
- [`04_setting_up_chroma_db.ipynb`](./04_setting_up_chroma_db.ipynb): راه‌اندازی پایگاه داده برداری پایدار (Persistent Storage) با ChromaDB و LangChain، ذخیره‌سازی داده‌ها و متادیتا روی دیسک، کالبدشکافی `chroma.sqlite3` و فایل‌های HNSW، و بازیابی معنایی.
