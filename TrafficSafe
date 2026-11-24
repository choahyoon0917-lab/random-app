import streamlit as st

# 1. 리스트(list) 데이터 구조 설계: 각 항목별 안내 내용을 리스트로 관리
crime_standard_list = [
    "음주운전: 혈중알코올농도 0.03% 이상인 상태에서 운전하는 행위",
    "무면허운전: 운전면허를 받지 않거나 효력이 정지된 상태에서 운전하는 행위",
    "뺑소니(도주치상): 사고로 사람을 다치게 하고 구호 조치 없이 현장을 떠나는 행위",
    "난폭운전: 신호위반, 중앙선 침범 등을 연달아 하여 다른 사람에게 위협을 주는 행위"
]

crime_law_list = [
    "도로교통법: 도로에서 일어나는 교통상의 모든 위험과 장해를 방지하고 제거하기 위한 기본 법령",
    "특정범죄 가중처벌 등에 관한 법률(특가법): 음주운전 사망사고(윤창호법), 어린이 보호구역 사고(민식이법) 등을 가중 처벌",
    "교통사고처리 특례법: 12대 중과실 사고 발생 시 보험 가입 여부와 관계없이 형사 처벌 대상이 됨"
]

safety_cause_list = [
    "전방 주시 태만: 운전 중 스마트폰 사용이나 내비게이션 조작으로 시선을 뺏기는 경우",
    "신호 및 속도 위반: 황색불 무리한 진입 및 제한속도 초과로 제동거리가 길어지는 경우",
    "안전거리 미확보: 앞차와의 거리를 충분히 두지 않아 급정거 시 추돌하는 경우",
    "졸음운전: 피로 누적 및 환기 부족으로 순간적으로 의식을 잃는 경우"
]

safety_rule_list = [
    "전 좌석 안전벨트 착용: 출발 전 운전자와 동승자 모두 반드시 안전벨트를 착용합니다.",
    "보행 중 스마트폰 자제: 횡단보도를 건널 때는 이어폰을 빼고 좌우를 살핍니다.",
    "어린이 보호구역(스쿨존) 서행: 시속 30km 이하로 서행하며 주변을 철저히 살핍니다.",
    "방어운전 및 양보운전: 교차로 진입 전 속도를 줄이고 방향지시등을 미리 켭니다."
]


# 2. 함수(def)와 반복구조(for) 정의: 리스트의 항목들을 화면에 깔끔하게 출력하는 함수
def display_guide_items(title_text, item_list):
    st.subheader(title_text)
    # 반복구조(for)를 사용하여 리스트에 담긴 내용을 하나씩 꺼내 출력
    for item in item_list:
        st.info(f"📌 {item}")


# 3. 메인 웹 화면 구성 함수(def)
def main():
    st.title("🚦 교통범죄 및 안전 안내서")
    st.write("교통 관련 법률 정보와 안전 수칙을 쉽게 확인할 수 있는 안내 웹입니다.")
    st.divider()

    # 1단계: 큰 주제 선택
    st.subheader("1단계: 어떤 내용이 궁금하신가요?")
    main_category = st.radio(
        "궁금한 분야를 선택하세요:",
        ["교통범죄", "교통안전"],
        horizontal=True
    )

    st.divider()

    # 2단계: 선택구조(if-elif-else)를 활용한 세부 메뉴 분기
    st.subheader("2단계: 세부 항목을 선택해 주세요.")

    if main_category == "교통범죄":
        sub_category = st.selectbox(
            "교통범죄의 어떤 정보가 필요하신가요?",
            ["선택하세요", "교통범죄의 기준", "교통범죄 관련 법"]
        )

        # 세부 선택에 따른 결과 출력
        if sub_category == "교통범죄의 기준":
            display_guide_items("🚨 주요 교통범죄의 기준", crime_standard_list)
        elif sub_category == "교통범죄 관련 법":
            display_guide_items("⚖️ 교통범죄 처벌 및 관련 법률", crime_law_list)

    elif main_category == "교통안전":
        sub_category = st.selectbox(
            "교통안전의 어떤 정보가 필요하신가요?",
            ["선택하세요", "교통사고 원인", "교통안전수칙"]
        )

        # 세부 선택에 따른 결과 출력
        if sub_category == "교통사고 원인":
            display_guide_items("⚠️ 주요 교통사고 발생 원인", safety_cause_list)
        elif sub_category == "교통안전수칙":
            display_guide_items("🛡️ 꼭 지켜야 할 교통안전수칙", safety_rule_list)

    # 3단계: 세부 항목을 선택해 내용이 출력된 이후, 추가 질문 여부 확인
    if sub_category != "선택하세요":
        st.divider()
        st.subheader("3단계: 궁금한 점이 해결되셨나요?")
        more_question = st.radio(
            "더 알아보실 내용이 있나요?",
            ["아니요, 모두 해결되었습니다.", "네, 다른 내용도 궁금합니다."],
            key="more_check"
        )

        # 추가 질문 여부에 따른 선택구조(if-else)
        if more_question == "네, 다른 내용도 궁금합니다.":
            st.success("👆 위쪽의 **1단계** 또는 **2단계** 선택지를 변경하시면 다른 정보를 바로 확인하실 수 있습니다!")
        else:
            st.balloons()
            st.write("안전한 교통 문화를 만들어가는 데 함께해 주셔서 감사합니다! 😊")


# 프로그램 실행
if __name__ == "__main__":
    main()
