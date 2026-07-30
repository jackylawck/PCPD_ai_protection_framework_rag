# 📊 Data Governance & Privacy Controls (數據管治與私隱控制)

## 1. Zero Data Retention Principle (零數據留存原則)
* **Transient Memory Processing (短暫內存處理)**: 本系統落實極致的資料不落地政策。使用者上傳的 PCPD 或 DPO 官方指引，僅在當前 RAM 中進行向量切片（Chunking），絕對不會將二進位檔案寫入硬碟或雲端儲存體。
* **No Telemetry**: 嚴格禁止收集用戶 IP、硬體特徵或輸入提示（Prompts）作任何二次訓練（Secondary Training）用途。

## 2. Data Provenance & SSOT (數據溯源與單一真實來源)
* **Responsibility Shifting (責任轉嫁設計)**: 系統本身不分發（Distribute）任何法規文件，徹底規避版權（Copyright）與法規過期風險。
* 用戶必須親自從官方政府網站（SSOT）下載最新文件並上傳，確保系統「食（Ingest）」入的知識永遠是最新、最權威的版本。

## 3. Chunking Strategy & Data Quality (切片策略與數據質量)
* **Sliding Window Algorithm**: 採用具脈絡重疊的滑動視窗切片（Chunk size: 500, Overlap: 100），確保法規上下文的語意連貫性（Semantic Continuity）。
* **Noise Filtration**: 透過 PyPDF 引擎萃取純文字，將 9.5MB 的印刷級 PDF 自動清洗、濃縮至最核心的法規文本切片，徹底消除「廢料進，廢品出（Garbage In, Garbage Out）」風險。

## 4. Auditability of Data (數據可審計性)
每一個法規切片在生成時皆賦予獨一無二的 HashID（Doc_ID）。在輸出合規建議時，強制顯示溯源標籤（Traceability Link），使任何結果皆可被內部審計師精確追蹤至官方文件的具體頁碼。
