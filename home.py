import streamlit as st


def run_home():
    st.title("⚾️ MLB 선수 기록 조회 및 예측 서비스 ⚾️")

    # 이미지 폭 조절
    st.image("mlb_players.jpg", use_column_width='always')

    st.markdown(
        """
        야구 팬 여러분, 안녕하세요! 👋

        MLB 선수 기록 조회 및 예측 서비스에 오신 것을 환영합니다. 🎉

        이 플랫폼은 **Major League Baseball (MLB)** 선수들의 기록을 쉽게 조회하고, 다양한 지표를 분석하며, 앞으로의 성과를 예측할 수 있는 종합적인 대시보드입니다. 📈
        """
    )

    # 주요 기능 강조
    st.markdown("---")
    st.header("✨ 주요 기능 ✨")

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("🔍 선수 기록 조회")
            st.markdown(
                """
                - **상세 기록**: 타율, 홈런, 타점, 출루율, 장타율, OPS, 안타, 도루, 볼넷, 삼진아웃 등 주요 타자 및 투수 기록을 한눈에 확인하세요.
                - **리그(시즌) 평균 비교**: 특정 시즌에서의 성과를 조회하고, 해당 시즌 평균과 비교해 볼 수 있습니다.
                """
            )

        with col2:
            st.subheader("📊 성과 예측")
            st.markdown(
                """
                - **알고리즘 기반 예측**: 최신 머신 러닝 알고리즘을 활용하여 타자와 투수의 다양한 기록을 예측합니다.
                - **맞춤형 예측**: 사용자가 선택한 조건에 따라 맞춤형 예측을 제공하여, 전략적 판단에 도움을 줍니다.
                - **트렌드 분석**: 선수들의 최근 경기 흐름을 분석하여 향후 성과를 예측합니다.
                """
            )

        with col3:
            st.subheader("📈 데이터 시각화")
            st.markdown(
                """
                - **그래프 및 차트**: 데이터를 시각화하여 이해하기 쉽게 제공하며, 다양한 시각적 도구를 통해 직관적인 분석이 가능합니다.
                - **트렌드 분석**: 타자와 투수의 리그 평균 지표 변화 추이를 시각화하여, 경기의 흐름을 한눈에 파악할 수 있습니다.
                - **인터랙티브 대시보드**: 사용자가 원하는 대로 대시보드를 커스터마이징하여, 필요한 정보만을 빠르게 조회할 수 있습니다.
                """
            )

    # 추가 정보 (선택 사항)
    st.markdown("---")
    with st.expander("🤔 더 알아보기"):
        st.write(
            """
            이 서비스는 야구 팬들이 선수들의 기록을 깊이 있게 이해하고, 미래 성과를 예측하는 데 도움을 주기 위해 만들어졌습니다.

            각 기능들은 다음과 같은 목표를 가지고 있습니다:
            - **트렌드 분석**: 리그 전체의 흐름을 분석하여, 전략적 판단에 유용한 인사이트를 제공합니다.
            - **기록 조회**: 상세한 선수 기록을 제공하여, 개별 선수의 성과를 쉽게 확인할 수 있습니다.
            - **성과 예측**: 과거 데이터를 기반으로 미래 성과를 예측하여, 선수들의 잠재력을 평가합니다.

            궁금한 점이 있으시면 언제든지 문의해주세요! 😊
            """
        )
    with st.expander("(용어 설명) 🏌️‍♂️타자 지표"):
        st.markdown("""
        ### Batting Average (타율)
        - **정의**: 타자가 얼마나 자주 안타를 치는지를 나타내는 지표.
        - **계산 방법**: 타율 = 안타 수 / 타수
        - **의미**: 타자의 타격 성공률을 보여줌.

        ### On-Base Percentage (출루율)
        - **정의**: 타자가 얼마나 자주 출루하는지를 나타내는 지표.
        - **계산 방법**: 출루율 = (안타 + 볼넷 + 사구) / (타수 + 볼넷 + 사구 + 희생 플라이)
        - **의미**: 타자의 출루 능력을 평가하는 지표.

        ### Slugging Percentage (장타율)
        - **정의**: 타자의 장타 능력을 평가하는 지표.
        - **계산 방법**: 장타율 = (1루타 + 2 * 2루타 + 3 * 3루타 + 4 * 홈런) / 타수
        - **의미**: 타자의 장타력(한 번의 타격으로 많은 베이스를 차지하는 능력)을 나타냄.

        ### OPS (출루율 + 장타율)
        - **정의**: 출루율과 장타율을 합친 값으로, 타자의 종합적인 공격력을 평가하는 지표.
        - **계산 방법**: OPS = 출루율 + 장타율
        - **의미**: 타자의 전반적인 타격 능력을 종합적으로 평가함.

        ### Hits (안타)
        - **정의**: 타자가 친 공이 페어 지역에 떨어져 안전하게 1루에 도달한 횟수.
        - **의미**: 타격 성공 횟수를 나타냄.

        ### RBIs (타점)
        - **정의**: 타자가 친 공으로 인해 주자가 득점한 횟수.
        - **의미**: 타자의 득점 기여도를 평가하는 지표.

        ### Home Runs (홈런)
        - **정의**: 타자가 공을 쳐서 바로 홈런을 기록한 횟수.
        - **의미**: 타자의 강력한 타격 능력을 평가하는 지표.

        ### Stolen Bases (도루)
        - **정의**: 주자가 투수가 던지는 동안 다음 베이스로 성공적으로 도루한 횟수.
        - **의미**: 주자의 빠른 발과 도루 능력을 평가하는 지표.

        ### Walks (볼넷)
        - **정의**: 타자가 볼넷을 받아 출루한 횟수.
        - **의미**: 타자의 선구안과 인내심을 평가하는 지표.
        """)

    # 투수 지표
    with st.expander("(용어 설명) ⚾투수 지표"):
        st.markdown("""
        ### Earned Run Average (평균자책점)
        - **정의**: 투수가 9이닝 동안 허용한 평균 자책점.
        - **계산 방법**: 평균자책점 = (자책점 / 이닝) * 9
        - **의미**: 투수의 실점을 평가하는 지표.

        ### WHIP (이닝당 볼넷 + 피안타)
        - **정의**: 이닝당 허용하는 볼넷과 안타의 합.
        - **계산 방법**: WHIP = (볼넷 + 피안타) / 이닝
        - **의미**: 투수의 이닝당 출루 허용 능력을 평가하는 지표.

        ### Wins (승수)
        - **정의**: 투수가 승리한 경기에 기여한 횟수.
        - **의미**: 투수의 승리 기여도를 나타냄.

        ### Losses (패배)
        - **정의**: 투수가 패배한 경기에 기여한 횟수.
        - **의미**: 투수의 패배 기여도를 나타냄.

        ### Strikeouts (탈삼진)
        - **정의**: 투수가 타자를 삼진 아웃시킨 횟수.
        - **의미**: 투수의 삼진 능력을 평가하는 지표.

        ### Innings Pitched (이닝)
        - **정의**: 투수가 던진 이닝 수.
        - **의미**: 투수의 경기 소화 능력을 평가하는 지표.

        ### Walks (볼넷)
        - **정의**: 투수가 타자에게 볼넷을 허용한 횟수.
        - **의미**: 투수의 제구력을 평가하는 지표.

        ### Hits Allowed (피안타)
        - **정의**: 투수가 타자에게 안타를 허용한 횟수.
        - **의미**: 투수의 피안타 허용 능력을 평가하는 지표.
        """)
