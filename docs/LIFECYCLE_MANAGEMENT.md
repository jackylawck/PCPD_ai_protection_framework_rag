# 🔄 AI System Lifecycle Management
# AI 系統生命週期管理政策

> **Compliance Alignment / 合規對齊**: ISO/IEC 42001:2023 Control A.6.2 | PCPD 2024 Framework Part 1 | AIGP Domain III

---

## 1. Planning & Architectural Selection / 規劃與架構選型

### 🇬🇧 English
* **Local Open-Source RAG**: Built using open-source `SentenceTransformers` and `Meta FAISS` running 100% locally/in-container.
* **Zero API Dependency**: Decoupled from third-party API keys (e.g., OpenAI) to prevent vendor lock-in and external telemetry risk during the system lifecycle.

### 🇭🇰 中文 (繁體)
* **純地端開源 RAG**：採用開源 `SentenceTransformers` 與 `Meta FAISS` 於容器內獨立運行。
* **零 API 依賴**：完全解耦第三方 API 金鑰（如 OpenAI），排除供應商鎖定與生命週期中數據外洩之風險。

---

## 2. Dynamic Operation & Maintenance / 動態運算與維護

### 🇬🇧 English
* **Dynamic Instantiation**: The RAG vector space is dynamically built per user session and destroyed upon completion, eliminating database drift and indexing degradation over time.
* **Model Benchmark Verification**: Embedding models are evaluated periodically to ensure multilingual Chinese/English alignment remains compliant with updated ISO standards.

### 🇭🇰 中文 (繁體)
* **動態實例化運算**：向量空間依使用者 Session 動態建立，會話結束即銷毀，物理性排除資料庫漂移與索引老化問題。
* **模型基準驗證**：定期評估嵌入模型，確保中英文雙語語意對齊持續符合最新 ISO 標準。

---

## 3. Decommissioning & Data Purge / 系統退役與數據清掃

### 🇬🇧 English
* **Zero Residual Footprint**: Because no persistent storage volumes exist, system decommissioning is executed simply by shutting down the application container, leaving zero residual regulatory data.

### 🇭🇰 中文 (繁體)
* **零殘留退役**：由於不掛載任何持久化儲存卷冊，系統退役僅需關閉雲端容器實例，不留下任何歷史數據足跡。
