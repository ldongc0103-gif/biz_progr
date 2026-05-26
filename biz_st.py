import streamlit as st
st.title("첫번째 웹 어플 만들기🍕🍻🙌🏽")
"""
#비즈니스 모델 분석

[네이버](https://www.naver.com/)  
[홍익대힉교](https://www.hongik.ac.kr/)  

이것이 일반 본문 **이것이 굵은 글씨** *이것이 기울인 글씨* ~~이것이 취소선~~  
:red[빨간 글씨] :blue[파란 글씨] :green[초록 글씨]

```ython
import streamlit as st


print("코드 블럭")
```

"""

st.caption('캡션(작고 흐린 글씨로 표현됨):st.caption()')

with st.echo():
    name=st.text_input("ldc")
    st.write(f"안녕하세요 {name}님")

st.latex('''e^{i\pi}+1=0''')
st.latex('\int_a^b f(x)dx')
"###:orange[이미지:st.image()]"
st.image("./data/python_image.png", caption="파이썬 로고", width=500)
