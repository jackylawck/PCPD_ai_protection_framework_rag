# 🔄 AI System Lifecycle Management (AI 系統生命週期管理)

## 1. Overview (概述)
本文件定義了「PCPD AI Framework Dynamic RAG Advisor」的生命週期管治機制。作為一個檢索增強生成（RAG）系統，生命週期管理涵蓋了底層嵌入模型（Embedding Model）的維護、動態向量索引（Dynamic Vector Indexing）的效能，以及法規知識庫的時效性。

## 2. Phase 1: Planning & Design (規劃與設計)
* **Architecture Choice**: 採用「純地端開源 RAG（Local Open-Source RAG）」架構，以完全阻斷第三方 API（如 OpenAI）帶來的資料出境（Data Exfiltration）與商業機密外洩風險。
* **Component Selection**: 選用輕量級、高精準的 `paraphrase-multilingual-MiniLM-L12-v2` 處理中英文多語境合規語意，確保在無 GPU 支援的普通硬體上亦能順暢運行。

## 3. Phase 2: Deployment & Operation (部署與營運)
* **Dynamic Instantiation (動態實例化)**: 系統採用「零留存（Zero-Retention）」部署策略。每次瀏覽器會話（Session）建立時，實時將官方 PDF 檔案轉換為 FAISS 向量資料庫（Vector DB）；會話結束，資料庫即刻物理性銷毀。
* **Audit Trail Generation**: 部署階段強制啟用 ISO 42001 密碼學審計軌跡，以 SHA-256 哈希值記錄所有推論行為。

## 4. Phase 3: Monitoring & Tuning (監控與調校)
* **Knowledge Base Currency (知識庫時效性)**: 系統本身不儲存法規。維護重點在於定期審查前端 UI 提供的「官方單一真實來源（Single Source of Truth, SSOT）」下載連結是否有效。
* **Threshold Tuning (閾值調校)**: 管治團隊將定期檢視 RAG 檢索的餘弦相似度（Cosine Similarity），適時調校防雜訊控制線（目前設定為 `confidence < 30`），以平衡「召回率（Recall）」與「準確率（Precision）」。

## 5. Phase 4: System Retirement (系統退役)
退役時，由於系統不包含持久化數據庫（Persistent Database），僅需關閉 Streamlit 雲端實例，並於 GitHub 標記為 Archive 狀態，即可安全完成系統生命週期終止。
