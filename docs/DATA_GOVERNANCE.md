# 📊 Data Governance & Privacy Controls
# 數據管治與私隱控制政策

> **Compliance Alignment / 合規對齊**: ISO/IEC 42001:2023 Controls A.8.3, A.8.5 | PCPD 2024 Framework Part 3 | AIGP Domain III

---

## 1. Zero Data Retention (ZDR) Architecture / 零數據留存架構

### 🇬🇧 English
* **In-Memory Vector Operations**: All uploaded PDF guidelines (PCPD / DPO) and generated Meta FAISS vector embeddings are processed strictly in volatile Session RAM.
* **Transient Dispoal**: Vector indices and document chunks are physically purged immediately upon browser session disconnection or refresh. Zero personal or regulatory data is stored to disk or cloud storage.

### 🇭🇰 中文 (繁體)
* **純記憶體向量運算**：所有載入之 PDF 指引（私隱公署/保障資料主任）及生成的 Meta FAISS 向量索引，僅於揮發性 Session RAM 中運算。
* **即時物理銷毀**：網頁會話中斷或刷新後，向量索引與文字切片即刻物理銷毀。絕不寫入硬碟或雲端資料庫，貫徹資料不落地。

---

## 2. Single Source of Truth (SSOT) & Data Provenance / 單一真實來源與數據血統

### 🇬🇧 English
* **Zero Copyright Redistribution**: To comply with copyright laws and prevent stale legal advice, the repository contains zero pre-packaged PDF binaries.
* **Authoritative Data Provenance**: Users connect directly with official government portals (PCPD/OGCIO) to load pristine guidelines, ensuring 100% data provenance integrity and single-source-of-truth standards.

### 🇭🇰 中文 (繁體)
* **零版權二次分發**：為符合著作權法規並杜絕過期法規風險，代碼倉庫不分發任何預載 PDF 二進位檔。
* **權威數據血統**：用戶直接對接官方政府管道載入指引，維護 100% 權威數據血統與單一真實來源 (SSOT) 標準。

---

## 3. Chunking Strategy & Data Quality / 切片策略與數據質量

### 🇬🇧 English
* **Sliding Window Chunking**: Employs a sliding window algorithm (Chunk Size: 500 characters, Overlap: 100 characters) to preserve natural semantic continuity across legal sections.
* **Noise Filtration**: Extracted text strips layout artifacts, print codes, and images (~68 high-precision chunks), eliminating "Garbage In, Garbage Out" risks under ISO 42001 Control A.8.3.

### 🇭🇰 中文 (繁體)
* **滑動視窗切片**：採用具脈絡重疊之滑動視窗演算法（切片大小：500 字元，重疊：100 字元），確保法規條文之語意連貫性。
* **雜訊降噪過濾**：萃取純文字並自動過濾版面印刷與圖像雜訊（濃縮至約 68 個高精準切片），防止「廢料進，廢品出」。
