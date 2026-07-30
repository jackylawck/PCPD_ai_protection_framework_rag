# ⚠️ AI System Risk Assessment (系統風險評估)

## 1. Risk Tiering (風險分級)
本系統作為企業內部的法規檢索增強沙盒，不直接處理 PII，亦不具備直接執行權限（No Execution Authority）。依據國際 AI 風險框架，評定為 **低至中度風險（Low-to-Medium Risk）** 工具。

## 2. RAG-Specific Threat Modeling (檢索增強特定威脅建模)

| 識別風險 (Risk Identified) | 潛在影響 (Potential Impact) | 緩解措施 (Mitigation Strategy) |
| :--- | :--- | :--- |
| **Model Hallucination (模型幻覺)** | 系統可能拼湊無關段落，生成看似合法但錯誤的指引。 | 停用 LLM 的自由生成能力，強制系統「僅」輸出檢索到的官方原文（Extractive RAG），從物理層面消滅生成式幻覺。 |
| **Adversarial Prompting (對抗性提示)** | 用戶可能輸入惡意 Prompt 試圖越獄（Jailbreak）或干擾向量檢索。 | 採用原生 SentenceTransformer 進行高維度語意映射，對抗性 Prompt 將因無法在法規中找到對應語意而觸發低置信度拒答。 |
| **Out-of-Context Retrieval (脫離語境檢索)** | 檢索到的法規片段可能因為缺乏前後文而導致誤讀。 | 實施 100 字元的 Overlap（重疊切片），並強制顯示文件來源與頁碼，要求人類決策者查閱完整段落。 |

## 3. Residual Risk Acceptance (剩餘風險接受)
本系統依賴用戶自行上傳文件。若用戶惡意上傳經篡改的偽造法規文件（Spoofed Documents），系統將基於該偽造文件進行錯誤推論。此風險（Data Poisoning at User Level）透過強制提供官方下載連結及明確的免責聲明來緩解，並由企業管理層接受此剩餘風險。
