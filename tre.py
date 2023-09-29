import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示 ')
'Start!!'

condition=st.slider('あなたの今の調子は？',0, 100, 50)
'コンディション:', condition

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

df = pd.DataFrame(
     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
     columns=['lat','lon']
)
st.map(df)

list_d = pd.DataFrame(
     np.random.rand(20, 3),
     columns=['a','b','c']
)
list_d

st.bar_chart(list_d)