# CRUD and Filtering

مدیریت چرخه حیات داده‌ها (CRUD)، مدیریت شناسه‌ها (IDs) و فیلترینگ مبتنی بر متادیتا در پایگاه‌های داده برداری.

## Scripts & Notebooks

- [`01_crud_operations.ipynb`](./01_crud_operations.ipynb): چرخه حیات داده‌ها (Create, Read, Update, Delete)، پیشگیری از ایجاد داده‌های تکراری با شناسه‌های صریح و هش محتوا (`hashlib.md5`)، خواندن مستقیم با متد `get`، عملیات حذف با `delete`، و تحلیل امتیازات فاصله و شباهت کسینوسی در `similarity_search_with_score`.
- [`02_metadata_filtering.ipynb`](./02_metadata_filtering.ipynb): فیلترینگ ترکیبی مبتنی بر متادیتا (Metadata Filtering)، جلوگیری از توهم بازیابی (Retrieval Hallucination)، عملگرهای مقایسه‌ای و منطقی ChromaDB به سبک MongoDB (`$eq`, `$in`, `$and`)، مقایسه معماری Pre-filtering در برابر Post-filtering، و معرفی تکنیک Self-Querying.
