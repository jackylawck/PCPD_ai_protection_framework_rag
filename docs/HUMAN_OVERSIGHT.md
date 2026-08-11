# 👁️ Human Oversight & Explainability
# 人為監督與可解釋性政策

> **Compliance Alignment / 合規對齊**: ISO/IEC 42001:2023 Controls A.9.2, A.9.3 | PCPD 2024 Framework Part 2 & 4 | AIGP Domain IV

---

## 1. Transparency & Traceability Links / 透明度與條文追溯鏈

### 🇬🇧 English
* **Page-Level Citations**: Every generated合規 recommendation provides direct, page-level citation links back to official PCPD PDF documents.
* **Open Reasoning**: RAG output explicitly displays the retrieved source text chunks, making the AI reasoning transparent, verifiable, and fully auditable for internal/external auditors.

### 🇭🇰 中文 (繁體)
* **頁碼級別引文追溯**：每條產出的合規建議均提供 PCPD 官方 PDF 文件之頁碼級別引文連結。
* **完全透明化推論**：RAG 檢索結果公開展示原始文字切片，使 AI 推論過程完全透明、可驗證，符合審計需求。

---

## 2. Anti-Hallucination Guardrails / 防幻覺截斷護欄

### 🇬🇧 English
* **Confidence Cutoff**: Enforces a strict mathematical similarity threshold (`confidence < 30%`).
* **Hardcoded Refusal**: Inquiries that cannot be matched to official PCPD text with high confidence trigger automatic system refusals, preventing speculative or fabricated AI inferences.

### 🇭🇰 中文 (繁體)
* **相似度置信度截斷**：硬碼執行嚴格的餘弦相似度門檻（`confidence < 30%`）。
* **自動化拒答機制**：無法高置信度匹配官方條文的查詢將自動觸發系統拒答，徹底杜絕生成式幻覺與盲目推測。

---

## 3. Human-in-the-Loop (HITL) Protocol / 人在環中執行協定

### 🇬🇧 English
* **Assistive Legal Tech**: System outputs serve solely as assistive legal tech for internal compliance research.
* **Human Accountability**: Authorized human compliance officers remain strictly accountable for interpreting RAG citations and approving final corporate AI governance policies.

### 🇭🇰 中文 (繁體)
* **輔助型 Legal Tech**：系統輸出僅作為企業內部合規研究之輔助工具。
* **最終人為問責**：授權之合規官須負責解讀 RAG 檢索條文，並對最終企業 AI 管治政策之簽署負全責。
