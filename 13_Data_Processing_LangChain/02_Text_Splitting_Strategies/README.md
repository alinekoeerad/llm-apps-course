# Text Splitting Strategies

استراتژی‌های خرد کردن اسناد و تکه‌تکه کردن متون (Chunking) با حفظ ساختار و انسجام معنایی در LangChain.

## Scripts & Notebooks
- [`01_text_splitting_strategies.ipynb`](./01_text_splitting_strategies.ipynb): تمثیل کیک عروسی و مفهوم کپسول معنایی، مقایسه شکست `CharacterTextSplitter` در برابر الگوریتم سلسله‌مراتبی `RecursiveCharacterTextSplitter`، بهینه‌سازی جداکننده‌ها برای زبان فارسی و نیم‌فاصله، و راهنمای انتخاب اندازه چانک (`chunk_size`).
- [`02_context_preservation_and_overlap.ipynb`](./02_context_preservation_and_overlap.ipynb): هنر حفظ بافتار، تراژدی «ضمیرهای سرگردان»، تکنیک همپوشانی چانک‌ها (`chunk_overlap`) و نسبت بهینه ۱۰٪ تا ۲۰٪، ارث‌بری خودکار متادیتای والد به فرزندان با `split_documents`، متادیتای بافتی با `MarkdownHeaderTextSplitter`، و خط لوله دو مرحله‌ای (Two-Stage Chunking).
- [`03_semantic_chunking.ipynb`](./03_semantic_chunking.ipynb): تقسیم‌بندی معنایی (Semantic Chunking)، حل مشکل مخلوط شدن موضوعات نامربوط (قورمه‌سبزی و ارسطو!)، کالبدشکافی مکانیسم درونی و محاسبه فواصل کسینوسی جملات با NumPy، پیاده‌سازی کامل هر ۳ روش آستانه شکست (Percentile, Standard Deviation, Interquartile/IQR)، و بنچمارک مقایسه‌ای زمان و واریانس طول چانک‌ها.
