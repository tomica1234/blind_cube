import streamlit as st
import time

def timer():
    if st.session_state.esolveway:
        st.write(' '.join(st.session_state.esolveway))
        st.write(' '.join(st.session_state.csolveway))
    
    # セッション状態を設定
    if 'running' not in st.session_state:
        st.session_state.running = False
        st.session_state.start_time = 0.0
        st.session_state.elapsed_time = 0.0
        st.session_state.time_list = []  # タイマーの経過時間を格納するリスト

    # 空のコンテナを作成
    elapsed_display = st.empty()

    # ボタンの表示と動作
    if st.button('スタート/ストップ', key='toggle_button'):
        if st.session_state.running:
            # タイマーを停止
            st.session_state.elapsed_time += time.time() - st.session_state.start_time
            elapsed_display.write(f"停止: 経過時間は {st.session_state.elapsed_time:.2f} 秒です。")
            st.session_state.running = False
            
            # 経過時間をリストに追加
            st.session_state.time_list.append(st.session_state.elapsed_time)

            # 平均時間の計算
            if st.session_state.time_list:
                average = sum(st.session_state.time_list) / len(st.session_state.time_list)
                st.write(f"平均時間は {average:.2f} 秒です")
            
        else:
            # タイマーをリセットしてスタート
            st.session_state.elapsed_time = 0.0  # 経過時間をリセット
            st.session_state.start_time = time.time()  # 現在の時間をスタート時間に設定
            st.session_state.running = True

    # タイマーの経過時間を表示
    while st.session_state.running:
        current_time = time.time()
        elapsed = st.session_state.elapsed_time + (current_time - st.session_state.start_time)
        
        # 経過時間を更新
        elapsed_display.write(f"経過時間: {elapsed:.2f} 秒")
        time.sleep(0.1)  # 100msごとに更新

# タイマー関数を実行
timer()
