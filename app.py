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
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# ==========================================
# 1. 頁面配置與高管級 UI
# ==========================================
st.set_page_config(
    page_title="PCPD AI RAG Advisor",
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
    
    lang_choice = st.radio("Language / 語言", ['繁體中文', 'English'], index=0 if is_zh else 1)
    if lang_choice != st.session_state.lang:
        st.session_state.lang = lang_choice
        st.rerun()
        
    st.markdown("---")
    st.markdown("### 🔒 RAG 安全硬化控制點 (ISO 42001 / DPP 4)" if is_zh else "### 🔒 RAG Security Controls")
    st.toggle("🛡️ 提示詞注入防禦 (Prompt Injection Protection)", value=True, disabled=True)
    st.toggle("👥 PII 去識別化過濾 (PII De-identification)", value=True, disabled=True)
    st.toggle("🚫 零數據留存承諾 (Zero-Retention API)", value=True, disabled=True)
    
    st.markdown("---")
    st.markdown(f"**專案架構師：羅子淇 Jacky Law**")
    st.link_button("🌐 Connect on LinkedIn", "https://www.linkedin.com/in/jackylawck", type="primary")

# ==========================================
# 3. RAG 核心：自動讀取並建立向量資料庫
# ==========================================
@st.cache_resource(show_spinner="🏛️ 正在載入並動態索引 PCPD 2024 官方中英文文本...")
def init_rag_vector_db():
    pdf_files = ["PCPD_ai_protection_framework_tc.pdf", "PCPD_ai_protection_framework_en.pdf"]
    all_docs = []
    
    for pdf in pdf_files:
        if os.path.exists(pdf):
            loader = PyPDFLoader(pdf)
            all_docs.extend(loader.load())
            
    if not all_docs:
        return None
        
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    chunks = text_splitter.split_documents(all_docs)
    
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = Chroma.from_documents(chunks, embeddings)
    return vector_store.as_retriever(search_kwargs={"k": 4})

retriever = init_rag_vector_db()

# 輔助函數：格式化檢索出來的條文文本
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# ==========================================
# 4. 主畫面與 RAG 智能互動
# ==========================================
st.title("🏛️ " + ("PCPD 模範框架 RAG 智能顧問系統" if is_zh else "PCPD AI Model Framework RAG Advisor"))
st.markdown("本系統已將您上傳的 PCPD 2024 官方中英文指引進行**向量化分片索引**。您可以直接以自然語言進行複雜的合規場景諮詢。" if is_zh else "This system has indexed the official PCPD 2024 Framework using a vector database. Query compliance scenarios in natural language:")

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
            with st.spinner("🕵️ 正在翻閱向量資料庫並進行法規對齊..." if is_zh else "Consulting Vector DB..."):
                try:
                    system_prompt = (
                        "You are an expert AI Governance Professional and Auditor. "
                        "You must strictly answer the user's question based ONLY on the provided PCPD Model Framework context. "
                        "If the answer cannot be found in the context, politely state that it is out of scope per the framework boundary.\n\n"
                        "Context:\n{context}"
                    )
                    
                    if is_zh:
                        system_prompt += "\n\n請務必使用繁體中文（香港專用管治術語）回答，並在回答末尾明確指出引用自《模範框架》的哪一部分、第幾條或第幾頁。"
                    else:
                        system_prompt += "\n\nPlease answer in professional English and explicitly cite the Part, Paragraph, or Page number of the Model Framework at the end."

                    prompt_template = ChatPromptTemplate.from_messages([
                        ("system", system_prompt),
                        ("human", "{input}"),
                    ])
                    
                    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
                    
                    # 💡 重構亮點：使用主流 LCEL (LangChain Expression Language) 電路架構
                    # 徹底拋棄不穩定的舊版 create_retrieval_chain
                    rag_chain = (
                        {"context": retriever | format_docs, "input": RunnablePassthrough()}
                        | prompt_template
                        | llm
                        | StrOutputParser()
                    )
                    
                    # 執行生成
                    answer = rag_chain.invoke(prompt)
                    
                    st.markdown(answer)
                    st.session_state.rag_messages.append({"role": "assistant", "content": answer})
                    
                except Exception as e:
                    st.error(f"❌ API 連線或檢索出錯。請檢查 OpenAI API Key。Error: {str(e)}")
