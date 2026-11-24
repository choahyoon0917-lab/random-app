import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="점심 메뉴 추천기", page_icon="🍽️")

# 제목 및 설명
st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라드립니다!")

# 1. 점심 메뉴 리스트
menus = ["짜장면", "마라탕", "제육볶음", "돈까스", "떡볶이", "햄버거", "초밥"]

# 현재 후보 메뉴 보여주기 (선택 사항)
with st.expander("현재 등록된 메뉴 후보 보기"):
    st.write(", ".join(menus))

st.divider()

# 2. 버튼 생성 및 랜덤 선택 실행
if st.button("🎲 오늘의 메뉴 추천받기", type="primary", use_container_width=True):
    selected_menu = random.choice(menus)
    
    # 결과 출력 및 축하 효과
    st.success(f"### 🎯 오늘의 추천 메뉴: **{selected_menu}**")
    st.balloons()
