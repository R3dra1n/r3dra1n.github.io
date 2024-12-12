import streamlit as st

# 设置页面标题
st.title('Streamlit的功能和demo')

# 输出一行文字
st.write("欢迎使用Streamlit！")

name = st.text_input("输入名字：")
add = st.text_area("输入地址")
st.write(f"Hi {name}!, 您住的地方是{add}")