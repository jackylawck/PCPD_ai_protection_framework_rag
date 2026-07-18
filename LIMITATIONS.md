# 系統限制與 RAG 管治邊界控制 (RAG System Limitations & Governance Controls)

## 1. 隨機性與非零幻覺風險管理 (Stochastic Nature & Hallucination Mitigation)
- **中文：** 本系統採用檢索增強生成 (RAG) 架構。雖已將檢索溫度 (Temperature) 降至極低的 0.1 以確保高度對齊文本，但由於大語言模型 (LLM) 的隨機本質，系統仍存在非零的「合規幻覺」概率。所有輸出僅供管治顧問參考，不具備絕對決定性法律約束力。
- **English:** This system operates on a Retrieval-Augmented Generation (RAG) architecture. While the LLM temperature is set to a deterministic 0.1 to maximize grounding, a non-zero risk of "compliance hallucination" remains due to the stochastic nature of generative AI. Outputs are for advisory reference only.

## 2. PII 資料保安與 API 傳輸邊界 (PII Security & API Data Flow Controls)
- **中文：** 依據 PCPD 模範框架第三部及保障資料第 4 原則（資料保安），使用者在向本系統進行場景諮詢時，**嚴禁輸入任何未經去識別化 (De-identified) 的企業敏感個人資料 (PII)**。系統呼叫外部 OpenAI API 時承諾零數據留存，但用戶仍須負起上游輸入端的資料管治責任。
- **English:** In compliance with Part III of the PCPD Model Framework and DPP 4 (Data Security), users are strictly prohibited from inputting unanonymised Corporate PII. The system enforces zero-retention API controls with OpenAI, but upstream data minimisation remains the user's primary responsibility.
