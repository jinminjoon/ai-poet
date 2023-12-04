#from langchain.llms import OpenAI
#llm = OpenAI(open_api_key='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')

#from langchain.llms import OpenAI
#llm = OpenAI(api_key='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')
#result = llm.predict("hi")
#print(result)

import time
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('인공지능 시인')
content = st.text_input('시의 주제를 입력하시오.')

if st.button('시 주제 입력하기'):
    with st.spinner('로딩중입니다. 잠시만 기다려 주세요^^'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        str.write(result)
