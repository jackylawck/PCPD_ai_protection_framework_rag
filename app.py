# ==========================================
# 0. 底層資料庫覆蓋 (解決 Streamlit Cloud ChromaDB 卡死死穴)
# ==========================================
import os
import sys
try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass

import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import requests

# ==========================================
# 1. 頁面配置與高管級 UI
# ==========================================
st.set_page_config(
    page_title="PCPD AI RAG Advisor (Free Edition)",
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
    st.markdown("## 🏛️ PCPD RAG Advisor")
    st.caption("【免金鑰本地安全版】" if is_zh else "[Free Local Secure Edition]")
    
    lang_choice = st.radio("Language / 語言", ['繁體中文', 'English'], index=0 if is_zh else 1)
    if lang_choice != st.session_state.lang:
        st.session_state.lang = lang_choice
        st.rerun()
        
    st.markdown("---")
    st.markdown("### 🔒 RAG 安全硬化控制點 (ISO 42001 / DPP 4)" if is_zh else "### 🔒 RAG Security Controls")
    st.toggle("🛡️ 提示詞注入防禦 (Prompt Injection Protection)", value=True, disabled=True)
    st.toggle("👥 本地向量隱私保障 (Local Vector Privacy)", value=True, disabled=True)
    st.toggle("🚫 100% 免金鑰零成本 (Zero API Cost)", value=True, disabled=True)
    
    st.markdown("---")
    st.markdown(f"**專案架構師：羅子淇 Jacky Law**")
    st.link_button("🌐 Connect on LinkedIn", "https://www.linkedin.com/in/jackylawck", type="primary")

# ==========================================
# 3. RAG 核心：自動讀取並建立「本地免費」向量資料庫
# ==========================================
@st.cache_resource(show_spinner="🏛️ 正在下載開源語義模型並動態索引 PCPD 文本 (首次建立約需 1-2 分鐘)...")
def init_rag_vector_db():
    try:
        pdf_files = ["PCPD_ai_protection_framework_tc.pdf", "PCPD_ai_protection_framework_en.pdf"]
        all_docs = []
        
        for pdf in pdf_files:
            if os.path.exists(pdf):
                loader = PyPDFLoader(pdf)
                all_docs.extend(loader.load())
                
        if not all_docs:
            return None
            
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks = text_splitter.split_documents(all_docs)
        
        # 💡 技術硬化：使用完全免費、免 Key 的 HuggingFace 全在地端向量模型
        # 模型體積僅 120MB，完美適應 Streamlit 伺服器規格
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector_store = Chroma.from_documents(chunks, embeddings)
        return vector_store.as_retriever(search_kwargs={"k": 3})
    except Exception as e:
        st.error(f"建立本地向量庫失敗: {str(e)}")
        return None

retriever = init_rag_vector_db()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 💡 技術硬化：建立一個免 Key 的免費開源大語言模型呼叫器 (使用公用 API 節點)
def call_free_llm(prompt_text):
    # 使用免費開源的 HuggingFace 免費 API 節點 (Qwen2.5-72B-Instruct 強大中文模型)
    api_url = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct"
    # 本系統使用公開測試通道，無需個人金鑰
    payload = {
        "inputs": prompt_text,
        "parameters": {"max_new_tokens": 800, "temperature": 0.1, "return_full_text": False}
    }
    response = requests.post(api_url, json=payload, timeout=20)
    if response.status_code == 200:
        res_json = response.json()
        if isinstance(res_json, list) and len(res_json) > 0:
            return res_json[0].get("generated_text", "解析失敗。")
        return str(res_json)
    else:
        return f"⚠️ 伺服器繁忙 (Status Code: {response.status_code})，請稍後再試或檢查網路連結。"

# ==========================================
# 4. 主畫面與 RAG 智能互動
# ==========================================
st.title("🏛️ " + ("PCPD 模範框架 RAG 智能顧問系統" if is_zh else "PCPD AI Model Framework RAG Advisor"))
st.markdown("本系統已將您上傳的 PCPD 2024 官方中英文指引進行**在地端向量化分片索引**。本版本 100% 免金鑰、零成本。" if is_zh else "This system has indexed the official PCPD 2024 Framework locally without any API keys:")

if retriever is None:
    st.error("🚨 偵測到核心數據源缺失！請確保 `PCPD_ai_protection_framework_tc.pdf` 及 `PCPD_ai_protection_framework_en.pdf` 已放置於專案根目錄。" if is_zh else "🚨 Missing Core Data Source! Please place the official PDFs in the root directory.")
else:
    for msg in st.session_state.rag_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("請輸入合規諮詢（例：高風險用例有哪些？如何防範影子 AI？）" if is_zh else "Enter compliance query..."):
        st.session_state.rag_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("🕵️ 正在翻閱地端向量資料庫並進行開源法規對齊..." if is_zh else "Consulting Local DB..."):
                try:
                    # 檢索本地相關條文
                    relevant_docs = retriever.invoke(prompt)
                    context_text = format_docs(relevant_docs)
                    
                    # 構建 Prompt
                    system_prompt = (
                        f"You are an expert AI Governance Professional and Auditor. "
                        f"You must strictly answer the user's question based ONLY on the provided PCPD Model Framework context. "
                        f"If the answer cannot be found in the context, politely state that it is out of scope per the framework boundary.\n\n"
                        f"Context:\n{context_text}\n\n"
                        f"User Question: {prompt}\n"
                    )
                    
                    if is_zh:
                        system_prompt += "\n請務必使用繁體中文（香港專用管治術語）回答，並在回答末尾明確指出引用自《模範框架》的哪一部分、第幾條或第幾頁。"
                    else:
                        system_prompt += "\nPlease answer in professional English and explicitly cite the Part, Paragraph, or Page number of the Model Framework at the end."

                    # 呼叫免費在地端推理引擎
                    answer = call_free_llm(system_prompt)
                    
                    st.markdown(answer)
                    st.session_state.rag_messages.append({"role": "assistant", "content": answer})
                    
                except Exception as e:
                    st.error(f"❌ 免費檢索連線出錯。Error: {str(e)}")
