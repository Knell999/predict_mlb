import streamlit as st

def run_home() :
    st.title('환영합니다! MLB 선수 기록 조회 및 예측 서비스')
    st.image('mlb_players.jpg')
    st.markdown("""
                야구 팬 여러분, 안녕하세요! \n
                MLB 선수 기록 조회 및 예측 서비스에 오신 것을 환영합니다.\n
                이곳은 Major League Baseball(MLB) 선수들의 기록을 쉽게 조회하고, 앞으로의 성과를 예측할 수 있는 플랫폼입니다.
                """)

    # 주요 기능
    st.header("주요 기능")

    st.subheader("1. 선수 기록 조회")
    st.markdown("""
    - **상세 기록**: 타율, 홈런, 타점, 출루율 등 주요 타자 및 투수 기록을 한눈에 확인하세요.
    - **경기별 기록**: 특정 경기에서의 성과를 조회하고, 중요한 순간을 다시 되짚어볼 수 있습니다.
    - **팀별 기록**: 각 팀의 주요 선수들의 시즌 기록을 비교하고 분석할 수 있습니다.
    """)

    st.subheader("2. 성과 예측")
    st.markdown("""
    - **알고리즘 기반 예측**: 최신 머신 러닝 알고리즘을 활용하여 선수들의 미래 성과를 예측합니다.
    - **맞춤형 예측**: 사용자가 선택한 조건에 따라 맞춤형 예측을 제공하여, 전략적 판단에 도움을 줍니다.
    - **트렌드 분석**: 선수들의 최근 경기 흐름을 분석하여 향후 성과를 예측합니다.
    """)

    st.subheader("3. 데이터 시각화")
    st.markdown("""
    - **그래프 및 차트**: 데이터를 시각화하여 이해하기 쉽게 제공하며, 다양한 시각적 도구를 통해 직관적인 분석이 가능합니다.
    - **인터랙티브 대시보드**: 사용자가 원하는 대로 대시보드를 커스터마이징하여, 필요한 정보만을 빠르게 조회할 수 있습니다.
    """)