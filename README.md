# 🤖 PCPD AI Protection Framework RAG Advisor

本專案是基於檢索增強生成 (RAG) 架構的「智能合規顧問系統」，為 **方案 B**，與方案 A（決定性守門員）形成企業風險管理的雙軌隔離防禦。

This project is an advanced AI Compliance Advisor driven by a Retrieval-Augmented Generation (RAG) architecture, serving as **Track B** to form a dual-track risk isolation matrix alongside Track A.

👉 **[🚀 點此立即訪問線上 RAG 智能顧問系統 (Live RAG Advisor)](https://pcpd-ai-protection-framework-rag.streamlit.app/)** *(請替換為您部署後的實際網址)*

---

## 🛠️ 技術架構與管治硬化 (Tech Stack & Security Hardening)

本系統直接將本地持有的 **PCPD 2024 官方中英文指引完整 PDF 文本** 進行向量化切片 (Chunking)，並透過內存向量資料庫 (Chroma DB) 進行語義檢索。系統內建以下 ISO 42001 / DPP 4 安全控制點：
- **低熵解讀：** 強制限制 LLM Temperature = 0.1，徹底壓縮模型發散空間。
- **提示詞注入防禦：** 系統內建嚴格的 System Prompt Guardrail，任何試圖繞過 PCPD 文本的惡意 Prompt 將被硬性拒絕。
- **條文精準溯源：** 每次回答均會動態翻閱知識庫，並自動吐出對應的官方文件頁碼與條文出處。

---

## 👥 聯絡與專業交流 (Contact)

👉 **[🌐 Connect on LinkedIn | 羅子淇 Jacky Law](https://www.linkedin.com/in/jackylawck)**
