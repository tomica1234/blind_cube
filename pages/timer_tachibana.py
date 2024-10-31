import streamlit as st
import time

st.title('タイマー')

def timer():
    if 'esolveway' in st.session_state and 'csolveway' in st.session_state and 'spinmark' in st.session_state:
        if "mitai" not in st.session_state:
            st.session_state.mitai = False
        if "spinmark" not in st.session_state:
            st.session_state.spinmark=None
        if  st.session_state.spinmark is not None:
            st.write(' '.join(st.session_state.spinmark))

        if st.button('文字列を見る/見ない', key='character_button'):
            st.session_state.mitai = not st.session_state.mitai  

        if st.session_state.mitai:
            st.write(''.join(st.session_state.esolveway))
            st.write(''.join(st.session_state.csolveway))
        else:
            st.write('文字列非表示中')
    else:
        st.write('scrambleを実行すると文字列がここに表示されます')

    if 'running' not in st.session_state:
        st.session_state.running = False
        st.session_state.start_time = 0.0
        st.session_state.elapsed_time = 0.0
        st.session_state.time_list = []  

    elapsed_display = st.empty()

    if st.button('スタート/ストップ', key='toggle_button'):
        if st.session_state.running:
            # Stop the timer
            st.session_state.elapsed_time += time.time() - st.session_state.start_time
            elapsed_display.write(f"停止: 経過時間は {st.session_state.elapsed_time:.2f} 秒です。")
            st.session_state.running = False

            st.session_state.time_list.append(st.session_state.elapsed_time)

            if st.session_state.time_list:
                average = sum(st.session_state.time_list) / len(st.session_state.time_list)
                st.write(f"平均時間は {average:.2f} 秒です")
        else:
            st.session_state.elapsed_time = 0.0  
            st.session_state.start_time = time.time()  
            st.session_state.running = True

    while st.session_state.running:
        current_time = time.time()
        elapsed = st.session_state.elapsed_time + (current_time - st.session_state.start_time)
        elapsed_display.write(f"経過時間: {elapsed:.2f} 秒")
        time.sleep(0.1) 

timer()
