# 🛡️ Integrated Governance & Security Policy (RAG Architecture)
# 綜合 AI 管治與資訊安全政策 (RAG 架構)

> **Compliance Standards / 遵循標準**: 
> * ISO/IEC 42001:2023 AI Management System (AIMS) Controls A.6.2, A.8.3, A.8.5, A.9.2, A.9.3
> * PCPD 2024 Model Framework (香港私隱專員公署《個人資料保障模範框架》)
> * IAPP AIGP Body of Knowledge (Domains I - IV)

---

## 1. Governance Principles & Human Oversight (管治原則與人為監督)

### 🇬🇧 English
* **Transparency & Citation Links**: Every RAG output provides direct page-level citation links back to official PCPD documents, rendering the AI reasoning completely transparent and auditable.
* **Confidence Threshold Guardrails**: Hardcoded cutoffs (`confidence < 30%`) automatically intercept low-relevance queries, preventing speculative AI inference and hallucinations.
* **Human-in-the-Loop (HITL)**: System recommendations serve purely as assistive legal tech. Human compliance officers remain solely accountable for final organizational decisions.

### 🇭🇰 中文 (繁體)
* **透明度與條文追溯**：每條 RAG 建議均提供 PCPD 官方指引之頁碼級別引文連結，實現完全透明與可審計的 AI 推論過程。
* **置信度門檻護欄**：硬碼截斷機制（`confidence < 30%`）自動攔截低關聯度查詢，徹底杜絕生成式幻覺與盲目推測。
* **人在環中 (HITL)**：系統建議僅作為輔助型 Legal Tech 工具，最終企業決策完全由授權的合規官負責。

---

## 2. Data Governance & Zero Data Retention (數據管治與零數據留存)

### 🇬🇧 English
* **Transient Vector Memory**: Operates under strict Zero Data Retention (ZDR). Uploaded PDFs and generated FAISS vector embeddings reside exclusively in volatile Session RAM and are purged upon disconnection.
* **Single Source of Truth (SSOT)**: Repository stores zero copyrighted PDF binaries. Users connect directly with official government sources, ensuring pristine data provenance and single-source integrity.
* **Data Minimization & Noise Filtration**: Ingests text-only regulatory data, stripping layout noise, images, and print artifacts to prevent "Garbage In, Garbage Out".

### 🇭🇰 中文 (繁體)
* **短暫向量記憶體**：貫徹極致的零數據留存 (ZDR)。載入之 PDF 與 FAISS 向量索引僅存於揮發性 Session RAM，關閉網頁即時徹底銷毀。
* **單一真實來源 (SSOT)**：代碼倉庫不分發任何具版權之 PDF，由使用者親自對接官方管道，維護權威數據血統。
* **數據最小化與雜訊過濾**：僅萃取純文字法規切片，過濾版面印刷與圖像雜訊，防止「廢料進，廢品出」。

---

## 3. Threat Modeling & Risk Assessment (威脅建模與風險評估)

### 🇬🇧 English
* **Risk Classification**: Classified as a **Low-to-Medium Risk Assistive RAG Sandbox** with no direct execution or automated decision-making (ADM) authority.
* **Threat Mitigation Matrix**:

| Identified Threat / 識別威脅 | Impact / 潛在影響 | Mitigation Control / 緩解控制措施 |
| :--- | :--- | :--- |
| **Model Hallucination (模型幻覺)** | AI fabricates non-existent privacy rules. (AI 虛構不存在的私隱規則) | Enforce confidence cutoffs and restrict output strictly to retrieved text chunks (Extractive RAG). |
| **Adversarial Prompting (對抗性提示)** | User attempts prompt injection or jailbreak. (用戶嘗試越獄或注入惡意 Prompt) | Native SentenceTransformer semantic mapping renders adversarial prompts unmatchable to privacy law. |
| **Out-of-Context Retrieval (斷章取義)** | Retrieved snippet lacks legal context. (檢索片段缺乏前後文語境) | Implement sliding window chunking (100-char overlap) and mandate page-level source link review. |

### 🇭🇰 中文 (繁體)
* **系統風險等級**：評定為 **低至中度風險輔助型 RAG 沙盒**，不具備自動化決策 (ADM) 權限。
* **威脅緩解矩陣**：如上表所示，結合置信度截斷、抽取式 RAG 及滑動視窗切片，確保風控無死角。

---

## 4. DevSecOps & Security Policy (資安政策與開發安全)

### 🇬🇧 English
* **Zero API Dependency**: Completely decoupled from external LLM APIs (e.g., OpenAI). Operations run 100% locally/in-container, eliminating third-party API data leakage risks.
* **Automated CI/CD Security**: GitHub Actions triggers automated SAST scans using `CodeQL` and `Bandit` on every commit. Merge requests require 100% pass rates (`✓`).
* **Non-Repudiation Logging**: Every query transaction logs a unique SHA-256 cryptographic hash with UTC timestamps for ISO 42001 verification without storing raw user text.

### 🇭🇰 中文 (繁體)
* **零 API 依賴**：完全解耦第三方 API（如 OpenAI），100% 本地/容器內運行，阻斷 API 資料外洩風險。
* **自動化 CI/CD 防線**：每次 commit 自動觸發 `CodeQL` 與 `Bandit` SAST 掃描，必須 100% 通過始可合併。
* **不可否認性日誌**：每筆查詢生成 SHA-256 密碼學哈希值，符合 ISO 42001 審計驗證。
