# 📋 ISO 42001 Model Card: PCPD AI Framework Dynamic RAG Advisor

> **ISO 42001 Alignment**: Controls A.6.2 (AI System Lifecycle), A.8.3 (Data Quality), A.8.5 (Zero Data Ingestion/Retention), and A.9.2 (Traceability & Explainability).

---

## 1. System Overview & Administrative Metadata
* **System Name**: PCPD AI Framework Dynamic Zero-Retention RAG Advisor (方案 B：動態零留存 RAG 沙盒)
* **Model Version**: v2.1.0 (Enterprise RAG)
* **System Architecture**: Local Semantic Vector Retrieval-Augmented Generation (RAG)
* **Governance & Development Lead**: Jacky Law (Certified ISO 42001 Lead Auditor / AIGP Candidate)
* **Last Audit Date**: 2026-07-30
* **Repository**: [jackylawck/PCPD_ai_protection_framework_rag](https://github.com/jackylawck/PCPD_ai_protection_framework_rag)

---

## 2. Intended Use & Governance Scope
* **Intended Purpose**:
  * Natural language semantic querying of official regulatory guidelines (PCPD Model Framework 2024 / DPO Guidelines).
  * Instant traceability of corporate AI governance queries back to exact official document pages and text chunks.
* **Target Audience**: Board members, Chief Privacy Officers (CPOs), Internal Auditors, HR & Procurement Directors.

---

## 3. Underlying AI / ML Components
* **Embedding Engine**: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (Local Open-Source Model).
* **Vector Index**: Meta FAISS (`IndexFlatIP` with L2 Normalized Cosine Similarity Search).
* **Chunking Strategy**:
  * Sliding Window Chunking (Chunk Size: 500 characters, Overlap: 100 characters).
  * Ingested Chunks: ~68 high-precision text vectors (100% text-only extraction, zero print-layout noise).

---

## 4. ISO 42001 Security, Privacy & Compliance Controls
* **Zero Data Retention (ZDR)**:
  * Ingested PDF documents exist **exclusively in transient browser Session Memory (RAM)**.
  * Zero persistent storage on cloud servers; data is destroyed instantly upon session closure.
* **Responsibility Shifting / Single Source of Truth (SSOT)**:
  * Open-source repository contains **zero copyrighted binary PDF files**. Users upload official PDFs directly from government/PCPD portals, ensuring compliance with single-source-of-truth standards.
* **Noise Interruption & Anti-Hallucination Guardrail**:
  * Similarity score threshold enforced (`confidence < 30%`). Low-relevance queries trigger automatic refusal to prevent speculative AI inference.
* **Non-Repudiation Audit Trail (ISO 42001 A.9.3)**:
  * Generates an SHA-256 cryptographic audit hash (`ISO 42001 Cryptographic Audit ID`) for every query-response transaction.

---

## 5. Performance Metrics & Environmental Performance
* **Query Latency**: ~3-5 seconds for vector space computation.
* **UI Resilience**: Features high-contrast CSS overrides (`.official-text !important`) to eliminate dark-mode readability glitches.
