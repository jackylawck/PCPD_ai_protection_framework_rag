# 🏛️ PCPD AI Framework Enterprise Advisor (Track B)

本專案是基於本地向量語義檢索與法規追溯架構的「企業級合規審計系統」，為 **方案 B**。本系統與方案 A（決定性守門員）形成企業風險管理的雙軌隔離防禦矩陣，專為高管、董事會及合規稽核員（Auditor）設計。

This project is an advanced Enterprise Compliance & Audit System driven by local semantic vector search, serving as **Track B** to form a dual-track risk isolation matrix alongside Track A.

👉 **[🚀 點此立即訪問線上 PCPD 智能顧問系統 (Live Advisor)](https://pcpd-ai-protection-framework-rag.streamlit.app/)**

---

## 🛠️ 技術架構與安全管治硬化 (Tech Stack & ISO 42001 Hardening)

為了徹底杜絕生成式大語言模型的「AI 幻覺（AI Hallucination）」風險並確保數據隱私，本系統採用與 *Cap. 57 僱傭條例顧問系統* 相同之**企業級金標準（Gold Standard）純本地 RAG 檢索架構**。系統直接掃描並動態索引專案目錄下的 PCPD 2024 官方中英文指引文本，並內建以下安全管治控制點：

- **零幻覺保障 (Zero-Hallucination Assurance)：** 系統不進行任何推測性的文本生成，純粹透過本地 `FAISS` 向量庫提取官方原始答覆文本，確保合規精準度。
- **密碼學審計軌跡 (Cryptographic Audit Trail)：** 系統內建符合 **ISO 42001** 規範的 Non-repudiation 機制。每次用戶查詢與檢索結果均會即時生成唯一的 SHA-256 密碼學審計 ID，並寫入地端不可篡改之日誌分類帳（Local Ledger）。
- **高透明度溯源 (Traceability Link)：** 自動計算並輸出歐氏距離歸一化之匹配置信度（Confidence Score %），且精確標註原始文件的 Page 頁碼、Doc_ID 與檔名，消滅硬編碼與合規盲區。
- **100% 數據隱私與零成本：** 採用純本地開源多語言向量模型（Sentence-Transformers），無任何外部 API 呼叫（免金鑰），零數據留存洩漏風險（Zero Data Leakage）。

---

## 🏛️ 架構對齊與管治指標监控 (Audit Monitoring)

系統主畫面整合了即時審計監控面板，可隨時調閱以下核心指標：
- 已動態掃描與安全加載的官方 PDF 數量
- 自動解構的法規文字切片總數 (Chunks)
- 即時合規排查審計日誌檔 (`compliance_audit.log`)

---

## 👥 專案架構師與專業交流 (Contact)

👉 **[🌐 Connect on LinkedIn | 羅子淇 Jacky Law](https://www.linkedin.com/in/jackylawck)**
