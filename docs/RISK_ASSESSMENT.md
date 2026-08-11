# ⚠️ AI System Risk Assessment & Threat Modeling
# AI 系統風險評估與威脅建模

> **Compliance Alignment / 合規對齊**: ISO/IEC 42001:2023 Control A.6.1 | PCPD 2024 Framework Part 2 | AIGP Domain II

---

## 1. Risk Tiering & Classification / 風險分級與歸類

### 🇬🇧 English
* **Low-to-Medium Risk Rating**: Evaluated as a **Low-to-Medium Risk Assistive RAG Sandbox**.
* **Zero Direct Execution**: The system executes no automated decision-making (ADM), processes no biometric data, and possesses no direct administrative execution power over individuals.

### 🇭🇰 中文 (繁體)
* **低至中度風險評定**：評定為 **低至中度風險輔助型 RAG 沙盒**。
* **零直接執行權**：系統不執行自動化決策（ADM）、不處理生物辨識特徵，對個人不具備直接行政處分權。

---

## 2. Threat Mitigation Matrix / 威脅緩解矩陣

### 🇬🇧 English & 🇭🇰 中文 (繁體)

| Threat Identified / 識別威脅 | Impact / 潛在影響 | Mitigation Control / 緩解控制措施 |
| :--- | :--- | :--- |
| **Model Hallucination (模型幻覺)** | System fabricates inaccurate privacy guidance. (生成不實私隱指引) | Hardcoded similarity cutoffs (`confidence < 30%`) block low-relevance results; restrict output to extractive text chunks. |
| **Adversarial Injection (對抗性注入)** | User inputs malicious prompts to jailbreak RAG. (惡意 Prompt 嘗試越獄) | Native SentenceTransformer semantic mapping renders adversarial prompts unmatchable to privacy law text. |
| **Context Fragmentation (斷章取義)** | Retrieved snippet loses broader legal meaning. (檢索片段缺失前後文) | Implement 100-character overlapping sliding window chunking and enforce mandatory page-level source link review. |
| **Data Poisoning (數據污染)** | User uploads spoofed PDF guideline. (使用者上傳偽造指引) | System enforces Zero Data Retention (ZDR); session-only scope prevents poisoned vectors from affecting other users. |

---

## 3. Cryptographic Non-Repudiation / 密碼學不可否認性

### 🇬🇧 English
* **SHA-256 Audit Hashes**: Every RAG transaction generates a unique SHA-256 cryptographic audit hash and UTC timestamp. This log preserves compliance auditability while stripping raw user prompts.

### 🇭🇰 中文 (繁體)
* **SHA-256 密碼學哈希**：每筆 RAG 查詢生成 SHA-256 哈希值與 UTC 時間戳，在脫敏原始 Prompt 的前提下，保障 ISO 42001 審計軌跡。
