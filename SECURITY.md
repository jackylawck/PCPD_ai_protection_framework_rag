# 🛡️ Security & Zero-Trust Policy (資安與零信任政策)

## Supported Versions
| Version | Supported          | Architecture |
| ------- | ------------------ | ------------ |
| 2.x.x   | :white_check_mark: | Dynamic RAG  |
| 1.x.x   | :x:                | Deprecated   |

## 1. Zero-Trust Execution Environment (零信任執行環境)
* **No API Keys**: 本系統完全依賴開源套件（PyPDF, FAISS, SentenceTransformers）於本機 / 雲端容器內獨立運行，無須配置 OpenAI 或任何外部金鑰，阻絕第三方服務遭駭或憑證外洩（Credential Leakage）的風險。
* **In-Memory Operations**: 不掛載持久化卷冊（No Persistent Volumes）。所有動態向量化操作皆於揮發性記憶體（Volatile Memory）中完成。

## 2. Automated Security Pipeline (DevSecOps 防線)
本專案整合了嚴謹的 GitHub Actions 自動化合規掃描：
* **CodeQL Analysis**: 深入代碼語意層面的安全性掃描。
* **Bandit Scan**: 嚴格阻擋 Python 常見漏洞（如 YAML 注入、不安全的反序列化）。
* **Stale / Labeler Governance**: 落實開源變更管理（Change Management），確保無人維護的問題不會成為未來的安全盲區。

## 3. Vulnerability Reporting (漏洞通報)
本專案為遵循 ISO 42001 及企業 AI 管治標準之展示原型。如發現任何能繞過「置信度截斷機制」或引發「跨會話資料洩漏（Cross-Session Data Leakage）」的重大漏洞，請透過 GitHub [Security Advisory] 私下通報管治團隊，請勿公開利用。
