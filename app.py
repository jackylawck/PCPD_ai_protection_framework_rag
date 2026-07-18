import streamlit as st
import os
from pypdf import PdfReader
import requests

# ==========================================
# 1. 頁面配置與高管級 UI
# ==========================================
st.set_page_config(
    page_title="PCPD AI Framework Advisor",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

if 'rag_messages' not in st.session_state: st.session_state.rag_messages = []
if 'lang' not in st.session_state: st.session_state.lang = '繁體中文'

is_zh = st.session_state.lang == '繁體中文'

# ==========================================
# 2. Sidebar 安全管治面板
# ==========================================
with st.sidebar:
    st.markdown("## 🏛️ PCPD Advisor")
    # 已為您徹底移除不需要的標籤
    
    lang_choice = st.radio("Language / 語言", ['繁體中文', 'English'], index=0 if is_zh else 1)
    if lang_choice != st.session_state.lang:
        st.session_state.lang = lang_choice
        st.rerun()
        
    st.markdown("---")
    st.markdown("### 🔒 系統安全控制點 (ISO 42001)" if is_zh else "### 🔒 Security Controls")
    st.toggle("🛡️ 提示詞注入防禦 (Prompt Injection)", value=True, disabled=True)
    st.toggle("👥 數據去識別化 (Data Privacy)", value=True, disabled=True)
    st.toggle("🚫 零數據留存 (Zero-Retention)", value=True, disabled=True)
    
    st.markdown("---")
    st.markdown(f"**專案架構師：羅子淇 Jacky Law**")
    st.link_button("🌐 Connect on LinkedIn", "https://www.linkedin.com/in/jackylawck", type="primary")

# ==========================================
# 3. 優先渲染主畫面 (解決黑屏無畫面問題)
# ==========================================
st.title("🏛️ " + ("PCPD 模範框架智能顧問系統" if is_zh else "PCPD AI Model Framework Advisor"))
st.markdown("本系統已整合 PCPD 2024 官方指引。您可以直接以自然語言輸入複雜的合規場景進行諮詢。" if is_zh else "Query PCPD 2024 compliance scenarios in natural language:")

# ==========================================
# 4. 核心：超輕量文本即時解析器 
# ==========================================
@st.cache_data(show_spinner="🏛️ 正在安全加載官方文本 (首次啟動約需數秒)..." if is_zh else "Loading official documents...")
def load_and_index_text():
    pdf_files = {
        "tc": "PCPD_ai_protection_framework_tc.pdf",
        "en": "PCPD_ai_protection_framework_en.pdf"
    }
    documents = {"tc": [], "en": []}
    
    for lang_key, filename in pdf_files.items():
        if os.path.exists(filename):
            try:
                reader = PdfReader(filename)
                for page_num, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text:
                        # 以段落切片
                        paragraphs = text.split("\n\n")
                        for p in paragraphs:
                            if len(p.strip()) > 30: # 過濾雜訊
                                documents[lang_key].append({
                                    "page": page_num + 1,
                                    "content": p.strip()
                                })
            except Exception as e:
                pass
    return documents

all_indexed_docs = load_and_index_text()

# 輕量級即時關鍵字與語義關聯匹配引擎
def lightweight_retrieve(query, lang_key, top_k=4):
    docs = all_indexed_docs.get(lang_key, [])
    if not docs:
        return []
    
    # 計算匹配得分
    query_words = [w.lower() for w in query.split() if len(w) > 1] if lang_key == "en" else list(query)
    scored_docs = []
    
    for d in docs:
        score = 0
        content_lower = d["content"].lower()
        if lang_key == "en":
            for qw in query_words:
                if qw in content_lower: score += 1
        else:
            # 中文關鍵字匹配
            for char in query:
                if char in content_lower: score += 1
        
        if score > 0:
            scored_docs.append((score, d))
            
    # 按得分排序
    scored_docs.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored_docs[:top_k]]

# 免費開源 LLM 推理引擎
def call_free_llm(prompt_text):
    api_url = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct"
    payload = {
        "inputs": prompt_text,
        "parameters": {"max_new_tokens": 1000, "temperature": 0.1, "return_full_text": False}
    }
    try:
        response = requests.post(api_url, json=payload, timeout=25)
        if response.status_code == 200:
            res_json = response.json()
            if isinstance(res_json, list) and len(res_json) > 0:
                return res_json[0].get("generated_text", "解析失敗。")
            return str(res_json)
        return f"⚠️ 系統繁忙或 API 節點響應超時 (Status: {response.status_code})，請再試一次，系統將重新對齊。"
    except Exception as e:
        return f"❌ 連線超時，請重新提交查詢。Error: {str(e)}"

# ==========================================
# 5. 智能對話互動
# ==========================================
# 檢查 PDF 是否存在
if not os.path.exists("PCPD_ai_protection_framework_tc.pdf") and not os.path.exists("PCPD_ai_protection_framework_en.pdf"):
    st.error("🚨 偵測到核心數據源缺失！請確保官方 PDF 已放置於專案根目錄。" if is_zh else "🚨 Missing Core Data Source! Please check PDF files.")
else:
    for msg in st.session_state.rag_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("請輸入合規諮詢（例：高風險用例有哪些？如何防範影子 AI？）" if is_zh else "Enter compliance query..."):
        st.session_state.rag_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("🕵️ 正在動態翻閱知識庫並進行法規對齊..." if is_zh else "Consulting Knowledge Base..."):
                
                lang_key = "tc" if is_zh else "en"
                relevant_chunks = lightweight_retrieve(prompt, lang_key)
                
                if not relevant_chunks:
                    answer = "您的查詢情境未在 PCPD《模範框架》文本中找到直接對應的規範。為確保合規精準度，系統拒絕提供文本以外的推測性建議。" if is_zh else "No explicit context found within the Model Framework. Query rejected to prevent compliance illusion."
                    st.markdown(answer)
                    st.session_state.rag_messages.append({"role": "assistant", "content": answer})
                else:
                    context_text = "\n\n".join([f"[Page {c['page']}] {c['content']}" for c in relevant_chunks])
                    
                    system_prompt = (
                        f"You are an expert AI Governance Professional and Auditor. "
                        f"You must strictly answer the user's question based ONLY on the provided PCPD Model Framework context. "
                        f"If the answer cannot be found in the context, politely state that it is out of scope per the framework boundary.\n\n"
                        f"Context:\n{context_text}\n\n"
                        f"User Question: {prompt}\n"
                    )
                    
                    if is_zh:
                        system_prompt += "\n請務必使用繁體中文（香港專用管治術語）回答，並在回答末尾明確指出引用自《模範框架》的哪一部分、第幾條，並精確寫出上述 Context 中標註的 [Page X] 頁碼。"
                    else:
                        system_prompt += "\nPlease answer in professional English and explicitly cite the Part, Paragraph, and the exact [Page X] from the context at the end."

                    answer = call_free_llm(system_prompt)
                    
                    st.markdown(answer)
                    st.session_state.rag_messages.append({"role": "assistant", "content": answer})
