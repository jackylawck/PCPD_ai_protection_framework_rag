# 📋 ISO 42001 Model Card: PCPD AI Framework Dynamic RAG Advisor
# ISO 42001 模型卡：PCPD 人工智能框架動態 RAG 顧問

> **ISO 42001 Alignment / ISO 42001 標準對齊**: 
> * Controls A.6.2: AI System Lifecycle (AI 系統生命週期)
> * Controls A.8.3 & A.8.5: Data Quality & Zero Data Ingestion/Retention (數據質量與零數據輸入/留存)
> * Controls A.9.2: Traceability & Explainability (可追溯性與可解釋性)

---

## 1. System Overview & Administrative Metadata / 系統概述與管理元數據

* **System Name / 系統名稱**: PCPD AI Framework Dynamic Zero-Retention RAG Advisor (方案 B：動態零留存 RAG 沙盒)
* **Model Version / 模型版本**: v2.1.0 (Enterprise RAG / 企業級 RAG 版)
* **System Architecture / 系統架構**: Local Semantic Vector Retrieval-Augmented Generation (地端語意向量檢索增強生成 RAG)
* **Governance & Development Lead / 管治與開發負責人**: Jacky Law 羅子淇 (Certified ISO 42001 Lead Auditor / AIGP Candidate)
* **Last Audit Date / 最近審計日期**: 2026-07-30
* **Repository / 程式碼倉庫**: [jackylawck/PCPD_ai_protection_framework_rag](https://github.com/jackylawck/PCPD_ai_protection_framework_rag)

---

## 2. Intended Use & Governance Scope / 預期用途與管治範圍

### 🇬🇧 English
* **Intended Purpose**:
  * Natural language semantic querying of official regulatory guidelines (PCPD Model Framework 2024 / DPO Guidelines).
  * Instant traceability of corporate AI governance queries back to exact official document pages and text chunks.
* **Target Audience**: Board members, Chief Privacy Officers (CPOs), Internal Auditors, HR & Procurement Directors.

### 🇭🇰 中文 (繁體)
* **預期用途**:
  * 對官方監管指引（私隱專員公署 PCPD 2024《模範框架》及保障資料主任指引）進行自然語言語意查詢。
  * 提供企業 AI 管治查詢之即時審計追溯鏈，精準定位至官方文件之具體頁碼與文字切片。
* **目標使用者**: 董事會成員、首席私隱官 (CPO)、內部審計師、人力資源及採購總監。

---

## 3. Underlying AI / ML Components / 底層 AI 及機器學習組件

### 🇬🇧 English
* **Embedding Engine**: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (Local Open-Source Model).
* **Vector Index**: Meta FAISS (`IndexFlatIP` with L2 Normalized Cosine Similarity Search).
* **Chunking Strategy**: Sliding Window Chunking (Chunk Size: 500 characters, Overlap: 100 characters). Ingests ~68 high-precision text-only vectors.

### 🇭🇰 中文 (繁體)
* **嵌入引擎 (Embedding Engine)**：`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`（地端開源多語言模型）。
* **向量索引 (Vector Index)**：Meta FAISS (`IndexFlatIP` 搭配 L2 正規化餘弦相似度搜尋)。
* **切片策略 (Chunking Strategy)**：滑動視窗切片（切片大小：500 字元，重疊：100 字元），萃取約 68 個高精準純文字向量切片。

---

## 4. Privacy, Security & Compliance Controls / 私隱、資安與合規控制

### 🇬🇧 English
* **Zero Data Retention (ZDR)**: Ingested PDF documents exist exclusively in transient browser Session Memory (RAM) and are physically purged upon session closure.
* **Single Source of Truth (SSOT)**: Repository contains zero copyrighted PDF binaries. Users connect directly with official sources to ensure compliance and avoid stale legal data.
* **Anti-Hallucination Guardrail**: Similarity score threshold enforced (`confidence < 30%`). Low-relevance queries trigger automatic refusal.
* **Cryptographic Audit Trail (ISO 42001 A.9.3)**: Generates an SHA-256 audit hash for every query transaction.

### 🇭🇰 中文 (繁體)
* **零數據留存 (ZDR)**：載入之 PDF 文件僅存在於當前瀏覽器 Session 揮發性記憶體 (RAM) 中，會話關閉即物理物理銷毀。
* **單一真實來源 (SSOT)**：程式碼倉庫不包含任何受版權保護之 PDF 二進位檔，由用戶直接對接官方來源，確保法規時效性與合規性。
* **防幻覺護欄**：設置相似度置信度截斷門檻（`confidence < 30%`），低關聯度查詢自動觸發拒答。
* **密碼學審計軌跡 (ISO 42001 A.9.3)**：每筆查詢皆生成不可逆之 SHA-256 哈希值。

---

## 5. System Limitations & Known Trade-offs / 系統局限與已知權衡

### 🇬🇧 English
* **Performance Metrics**: ~3-5 seconds query latency for vector space computation.
* **Mitigation Strategy**: Operates within a **Dual-Track Defense Matrix** alongside Project 1 (Deterministic Evaluator) for structured and unstructured legal triage.

### 🇭🇰 中文 (繁體)
* **效能指標**：高維度向量空間運算平均查詢延遲約 3–5 秒。
* **緩解策略**：作為**雙軌防禦矩陣 (Dual-Track Defense Matrix)** 的第二軌部署，與專案一（決定性預審門神）搭配，實現結構化與非結構化之法規風險分流。
