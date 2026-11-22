# بخش ۲: الگوریتم‌های بازیابی (Retrieval Algorithms)

این پوشه شامل درسنامه‌ها، پروژه‌ها و پیاده‌سازی‌های عملی استراتژی‌های پیشرفته بازیابی اطلاعات در خطوط لوله RAG است.

---

## 🗂️ فهرست درسنامه‌ها و نت‌بوک‌ها

### ۱. [01_mmr_and_retrieval_strategies.ipynb](file:///d:/Project/LLM/llm-apps-course/14_External_Knowledge_and_RAG/02_Retrieval_Algorithms/01_mmr_and_retrieval_strategies.ipynb)
* **مفاهیم اصلی:**
  * معضل افزونگی (Redundancy) و اشباع کانتکست با چانک‌های تکراری در `Similarity Search`.
  * تشبیه شهودی تیم فوتبال (۱۱ دروازه‌بان در برابر تیم متعادل).
  * الگوریتم **MMR (Maximal Marginal Relevance)** برای ایجاد توازن پویا میان ارتباط (`Relevance`) و تنوع (`Diversity`).
  * تنظیم پارامترهای `fetch_k`, `k` و ضریب تعادل `lambda_mult` (مقایسه 1.0 و 0.5 و 0.0).
  * دفاع در برابر سوالات پرت و توهم (Hallucination) با فیلتر آستانه شباهت (`similarity_score_threshold`).
  * پیاده‌سازی زنجیره کامل LCEL با استفاده از مدل **Google Gemini** (`gemini-flash-lite-latest`).
  * ماتریس تصمیم‌گیری (Decision Matrix) برای انتخاب بهترین استراتژی بازیابی.
