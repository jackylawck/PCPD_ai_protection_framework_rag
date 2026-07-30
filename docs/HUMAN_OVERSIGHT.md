# 👁️ Human Oversight & Explainability (人為監督與可解釋性)

## 1. Transparency by Default (預設透明)
* 本 RAG 系統並非「黑盒（Black Box）」。所有建議均附帶 **【官方原始條文段落】**，強制公開 AI 推論的底層依據，確保完全的可解釋性（Explainability）。
* 顯示精確的 **匹配置信度（Confidence Score）**，讓人類決策者清楚評估該條文與當前情境的關聯強度。

## 2. Anti-Hallucination Guardrails (防幻覺護欄)
* **Confidence Cutoff (置信度截斷)**: 系統內建硬性防線（`if confidence < 30: continue`）。當人類使用者的問題無法在官方指引中找到具備足夠數學關聯性的條文時，系統依法拒絕給出衍生性推論，強制依賴人為判斷。

## 3. Human-in-the-Loop (HITL) Execution
* 系統定位為「合規自查工作站」，輸出結果需由具備管治背景的專業人員進行二次確認。
* **Semantic Nuance Evaluation**: 人類監督者需負責評估 RAG 檢索出的法規段落，是否真正適用於複雜的現實企業環境（例如跨國資料傳輸的特定豁免條款）。

## 4. Cryptographic Non-Repudiation (密碼學不可否認性)
每筆查詢皆附帶 `ISO 42001 Cryptographic Audit ID`，確保當人類決策者依據系統建議採取行動時，擁有不可篡改的證據鏈（Evidentiary Chain），保障決策問責制（Accountability）。
