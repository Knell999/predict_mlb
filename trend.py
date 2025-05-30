import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
from streamlit_option_menu import option_menu
from utils import load_data, load_pitcher_data
from i18n import get_text
from config import FONT_PATH # 설정 파일에서 폰트 경로 가져오기

fontprop = fm.FontProperties(fname=FONT_PATH, size=12) # 경로 수정

# 리그 평균 계산 함수 추가
def calculate_league_averages(df, metrics):
    """
    시즌별 리그 평균을 계산하는 함수입니다.
    
    Args:
        df: 분석할 데이터프레임
        metrics: 계산할 지표들의 리스트
        
    Returns:
        시즌별로 그룹화된 리그 평균 데이터프레임
    """
    league_averages = df.groupby('Season')[metrics].mean().reset_index()
    return league_averages

# 이동평균 계산 함수 추가
def calculate_moving_average(df, metrics, window):
    """
    특정 윈도우 크기의 이동평균을 계산하는 함수입니다.
    
    Args:
        df: 분석할 데이터프레임
        metrics: 계산할 지표들의 리스트
        window: 이동평균 윈도우 크기
        
    Returns:
        이동평균이 계산된 데이터프레임
    """
    moving_avg = df.copy()
    for metric in metrics:
        moving_avg[metric] = moving_avg[metric].rolling(window=window, min_periods=1).mean()
    return moving_avg

# 타자와 투수의 리그 평균 계산
batting_metrics = ['BattingAverage', 'OnBasePercentage', 'SluggingPercentage', 'OPS', 'Hits', 'RBIs', 'HomeRuns', 'StolenBases', 'Walks', 'StrikeOuts']
pitching_metrics = ['EarnedRunAverage', 'Whip', 'Wins', 'Losses', 'StrikeOuts', 'InningsPitched', 'Walks', 'HitsAllowed']

df_batters = load_data()
df_pitchers = load_pitcher_data()

batting_league_avg = calculate_league_averages(df_batters, batting_metrics)
pitching_league_avg = calculate_league_averages(df_pitchers, pitching_metrics)

batting_moving_avg_5 = calculate_moving_average(batting_league_avg, batting_metrics, 5)
batting_moving_avg_10 = calculate_moving_average(batting_league_avg, batting_metrics, 10)
batting_moving_avg_20 = calculate_moving_average(batting_league_avg, batting_metrics, 20)

pitching_moving_avg_5 = calculate_moving_average(pitching_league_avg, pitching_metrics, 5)
pitching_moving_avg_10 = calculate_moving_average(pitching_league_avg, pitching_metrics, 10)
pitching_moving_avg_20 = calculate_moving_average(pitching_league_avg, pitching_metrics, 20)

def plot_metric(ax, metric, league_avg, moving_avg_5, moving_avg_10, moving_avg_20, lang="ko"):
    """
    리그 평균 지표와 이동평균을 시각화하는 함수입니다.
    
    Args:
        ax: 그래프를 그릴 matplotlib 축
        metric: 시각화할 지표명
        league_avg: 리그 평균 데이터프레임
        moving_avg_5: 5년 이동평균 데이터프레임
        moving_avg_10: 10년 이동평균 데이터프레임
        moving_avg_20: 20년 이동평균 데이터프레임
        lang: 언어 코드 (기본값: 'ko')
    """
    # 다국어 레이블 정의
    labels = {
        'ko': {
            'league_avg': '리그 평균', 
            'moving_avg_5': '5년 이동평균',
            'moving_avg_10': '10년 이동평균',
            'moving_avg_20': '20년 이동평균',
            'title_prefix': '리그 평균',
            'season': '시즌'
        },
        'en': {
            'league_avg': 'League Average', 
            'moving_avg_5': '5-Year Moving Average',
            'moving_avg_10': '10-Year Moving Average',
            'moving_avg_20': '20-Year Moving Average',
            'title_prefix': 'League Average',
            'season': 'Season'
        },
        'ja': {
            'league_avg': 'リーグ平均', 
            'moving_avg_5': '5年移動平均',
            'moving_avg_10': '10年移動平均',
            'moving_avg_20': '20年移動平均',
            'title_prefix': 'リーグ平均',
            'season': 'シーズン'
        }
    }
    
    # 기본 언어 설정
    if lang not in labels:
        lang = "ko"
    
    label_text = labels[lang]
    
    sns.lineplot(data=league_avg, x='Season', y=metric, ax=ax, marker='o', label=label_text['league_avg'])
    sns.lineplot(data=moving_avg_5, x='Season', y=metric, ax=ax, linestyle='--', color='gray',
                 label=label_text['moving_avg_5'])
    sns.lineplot(data=moving_avg_10, x='Season', y=metric, ax=ax, linestyle='-.', color='blue',
                 label=label_text['moving_avg_10'])
    sns.lineplot(data=moving_avg_20, x='Season', y=metric, ax=ax, linestyle=':', color='red',
                 label=label_text['moving_avg_20'])
    ax.set_title(f"{label_text['title_prefix']} {metric} {get_text('trend_overview', lang).split(' ')[-1]}", fontproperties=fontprop)
    ax.set_xlabel(label_text['season'], fontproperties=fontprop)
    ax.set_ylabel(metric, fontproperties=fontprop)
    ax.legend()
    ax.tick_params(axis='x', rotation=45)

def run_trend(lang="ko"):
    """MLB 리그 트렌드를 분석하고 시각화하는 함수입니다."""

    st.title(get_text("trend_title", lang))

    # 다국어 메뉴 옵션 정의
    menu_options = {
        'ko': ['타자', '투수'],
        'en': ['Batters', 'Pitchers'],
        'ja': ['打者', '投手']
    }
    
    selected_lang_options = menu_options.get(lang, menu_options['ko'])
    
    selected = option_menu(
        None,
        selected_lang_options,
        icons=['person', 'ball'],
        menu_icon='cast',
        default_index=0,
        orientation='horizontal',
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "blue", "font-size": "20px"},
            "nav-link": {"font-size": "15px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#4CAF50"},
        }
    )

    # 언어에 따른 메뉴 옵션 매핑
    batter_options = {'ko': '타자', 'en': 'Batters', 'ja': '打者'}
    batter_option = batter_options.get(lang, '타자')
    
    pitcher_options = {'ko': '투수', 'en': 'Pitchers', 'ja': '投手'} # Added
    pitcher_option = pitcher_options.get(lang, '투수') # Added
    
    if selected == batter_option:
        metrics = batting_metrics
        league_avg = batting_league_avg
        moving_avg_5 = batting_moving_avg_5
        moving_avg_10 = batting_moving_avg_10
        moving_avg_20 = batting_moving_avg_20
    else:
        metrics = pitching_metrics
        league_avg = pitching_league_avg
        moving_avg_5 = pitching_moving_avg_5
        moving_avg_10 = pitching_moving_avg_10
        moving_avg_20 = pitching_moving_avg_20

    # 언어에 따른 서브헤더 텍스트
    subheader_text = {
        'ko': f"{selected} 리그 평균 지표 변화 추이 (2000-2023)",
        'en': f"{selected} League Average Metrics Trend (2000-2023)",
        'ja': f"{selected} リーグ平均指標変化推移 (2000-2023)"
    }
    
    st.subheader(subheader_text.get(lang, subheader_text['ko']))

    # 언어에 따른 보고서 타이틀
    report_title = {
        'ko': "MLB 타자 리그 평균 지표 변화 추이 보고서 (2000-2023)",
        'en': "MLB Batters League Average Metrics Trend Report (2000-2023)",
        'ja': "MLB打者リーグ平均指標変化推移レポート (2000-2023)"
    }
    
    # 언어에 따른 개요 섹션
    overview_text = {
        'ko': """
            ### 1. 개요
            이 보고서는 2000년부터 2023년까지의 MLB 타자 리그 평균 지표 변화 추이를 분석한 것입니다. 각 지표에 대해 리그 평균 및 5개년, 10개년, 20개년 이동평균선을 포함하여 분석했습니다.""",
        'en': """
            ### 1. Overview
            This report analyzes the trends in MLB batter league average metrics from 2000 to 2023. Each metric is analyzed with league averages and 5-year, 10-year, and 20-year moving averages.""",
        'ja': """
            ### 1. 概要
            このレポートは、2000年から2023年までのMLB打者リーグ平均指標の変化推移を分析したものです。各指標について、リーグ平均および5年、10年、20年の移動平均線を含めて分析しました。"""
    }
    
    if selected == batter_option:
        st.markdown("---")
        st.subheader(report_title.get(lang, report_title['ko']))
        
        st.markdown(overview_text.get(lang, overview_text['ko']))
        
        # Add metrics description text based on language
        if lang == "en":
            st.markdown("""
            ### 2. Analysis Metrics
            - **Batting Average**
            - **On-Base Percentage**
            - **Slugging Percentage**
            - **OPS (On-base + Slugging)**
            - **Hits**
            - **RBIs**
            - **Home Runs**
            - **Stolen Bases**
            - **Walks**
            - **Strikeouts**

            ### 3. Key Metrics Analysis and Meaning
            """)
        elif lang == "ja":
            st.markdown("""
            ### 2. 分析指標
            - **打率**
            - **出塁率**
            - **長打率**
            - **OPS (出塁率 + 長打率)**
            - **ヒット**
            - **打点**
            - **ホームラン**
            - **盗塁**
            - **四球**
            - **三振**

            ### 3. 主要指標分析と意味
            """)
        else:  # Default to Korean
            st.markdown("""
            ### 2. 분석 지표
            - **Batting Average (타율)**
            - **On-Base Percentage (출루율)**
            - **Slugging Percentage (장타율)**
            - **OPS (출루율 + 장타율)**
            - **Hits (안타)**
            - **RBIs (타점)**
            - **Home Runs (홈런)**
            - **Stolen Bases (도루)**
            - **Walks (볼넷)**
            - **Strikeouts (삼진)**

            ### 3. 주요 지표 분석 및 의미
            """)

        for metric in metrics:
            st.markdown(f"#### 3.{metrics.index(metric) + 1}. {metric}")
            fig, ax = plt.subplots(figsize=(10, 5))
            plot_metric(ax, metric, league_avg, moving_avg_5, moving_avg_10, moving_avg_20, lang)
            st.pyplot(fig)

            # Moved and indented metric descriptions to be INSIDE the loop
            if metric == "BattingAverage":
                st.markdown(
                """
                - **변화 추이**: 2000년대 초반에는 대체로 안정적이었으나, 2010년대 중반부터 점차 감소하는 추세를 보입니다.
                - **의미**: 타율의 지속적인 감소는 투수들의 기량 향상과 더불어, 방어율과 삼진율의 증가, 현대 야구에서의 분석 기술 발달로 인한 수비 시프트의 증가 등을 반영할 수 있습니다. 이는 타자들이 투수들의 다양하고 정교한 투구에 대처하는 데 어려움을 겪고 있음을 나타냅니다.
                """
                )
            elif metric == "OnBasePercentage":
                st.markdown(
                """
                - **변화 추이**: 출루율 역시 타율과 유사한 패턴을 보이며, 2010년대 중반 이후로 감소하는 경향이 나타납니다.
                - **의미**: 출루율의 감소는 타자들이 볼넷을 얻기 어려워졌음을 의미할 수 있으며, 투수들의 제구력 향상과 더불어, 타자들이 삼진을 피하기 위해 더 많은 공을 치려고 시도하고 있음을 시사합니다.
                """
                )
            elif metric == "SluggingPercentage":
                st.markdown(
                """
                - **변화 추이**: 2000년대 초반에는 비교적 높은 수준을 유지했으나, 2010년대 후반부터 변동이 심화되며 감소 추세를 보입니다.
                - **의미**: 장타율의 감소는 홈런과 같은 장타를 치는 것이 점점 더 어려워지고 있음을 나타냅니다. 이는 투수들의 구속 증가, 변화구의 다양화, 그리고 수비 시프트의 영향으로 타자들이 장타를 치기 어려워지고 있음을 반영합니다.
                """
                )
            elif metric == "OPS":
                st.markdown(
                """
                - **변화 추이**: 타율 및 출루율과 유사한 패턴으로, 2010년대 중반 이후 감소하는 경향이 두드러집니다.
                - **의미**: OPS의 감소는 타자들이 출루와 장타 모두에서 어려움을 겪고 있음을 시사합니다. 이는 투수들의 전반적인 기량 향상과 현대 야구의 전략적 변화가 타자들에게 불리하게 작용하고 있음을 시사합니다.
                """
                )
            elif metric == "Hits":
                st.markdown(
                """                    - **변화 추이**: 2000년대 초반부터 2010년대 중반까지는 상대적으로 안정적인 추이를 보였으나, 최근 몇 년간 변동이 심화되었습니다.
                - **의미**: 안타 수의 변동은 타자들이 투수들의 다양한 구종과 전략에 적응하는 과정에서 일어나는 자연스러운 변화일 수 있습니다. 특히 최근 몇 년간의 변동은 타자들이 새로운 투구 패턴에 적응하는 데 어려움을 겪고 있음을 나타낼 수 있습니다.
                """
                )
            elif metric == "RBIs":
                st.markdown(
                """
                - **변화 추이**: 타점은 2000년대 초반부터 점진적으로 감소하는 경향을 보입니다.
                - **의미**: 타점의 감소는 득점 기회에서 타자들이 성공적으로 안타를 치는 빈도가 줄어들고 있음을 의미할 수 있습니다. 이는 투수들이 득점권 상황에서 더 효과적인 투구를 하고 있음을 시사합니다.
                """
                )
            elif metric == "HomeRuns":
                st.markdown(
                """
                - **변화 추이**: 홈런 수는 비교적 안정적이지만, 2010년대 후반부터 약간의 변동을 보입니다.
                - **의미**: 홈런 수의 변동은 타자들이 홈런을 치기 위한 전략적 변화와 투수들의 변화구 사용 증가 등 다양한 요인의 영향을 받을 수 있습니다. 안정적인 홈런 수는 여전히 타자들이 파워 히팅에 중점을 두고 있음을 나타냅니다.
                """
                )
            elif metric == "StolenBases":
                st.markdown(
                """
                - **변화 추이**: 도루 수는 전반적으로 감소 추세를 보이며, 특히 최근 몇 년간 급격히 줄어들었습니다.
                - **의미**: 도루 수의 감소는 현대 야구에서 도루의 전략적 중요성이 감소했음을 시사합니다. 이는 홈런과 같은 장타를 통한 득점 전략이 더 선호되며, 도루의 리스크가 더 크다고 평가되는 현상을 반영할 수 있습니다.
                """
                )
            elif metric == "Walks":
                st.markdown(
                """
                - **변화 추이**: 볼넷 수는 전반적으로 안정적인 추이를 보였으나, 최근 몇 년간 변동이 심화되었습니다.
                - **의미**: 볼넷 수의 변동은 타자들이 투수들의 구종과 제구력에 적응하는 과정에서 발생할 수 있습니다. 최근 변동은 타자들이 더 공격적으로 타격하려는 경향을 나타낼 수 있습니다.
                """
                )
            elif metric == "StrikeOuts":
                st.markdown(
                """
                - **변화 추이**: 삼진 수는 전반적으로 증가 추세를 보이며, 특히 최근 몇 년간 급격히 증가했습니다.
                - **의미**: 삼진 수의 급격한 증가는 투수들의 구속 증가와 함께 변화구의 다양화가 타자들에게 큰 도전이 되고 있음을 나타냅니다. 또한, 현대 야구에서 타자들이 홈런을 노리는 스윙을 더 자주 시도하면서, 삼진의 리스크를 감수하는 경향이 증가하고 있음을 시사합니다. 이는 파워 중심의 타격 접근 방식이 보편화되었음을 반영합니다.
                """
                )

        st.markdown(
        """
        4. 결론 및 시사점

        전반적인 추세
        - **타자 성적의 하락**: 여러 지표에서 볼 수 있듯이, 타자들의 성적은 전반적으로 하락하는 추세를 보이고 있습니다. 이는 투수들의 기량 향상, 더 정교해진 수비 시프트, 데이터 분석 기술의 발달로 인한 투수 전략의 고도화 등 다양한 요인들이 복합적으로 작용한 결과일 수 있습니다.
        - **삼진 증가**: 삼진의 급격한 증가는 현대 야구에서의 타격 접근 방식 변화와 투수들의 향상된 기량을 반영합니다. 이는 타자들이 더 큰 리스크를 감수하면서도 높은 보상을 추구하는 전략을 채택하고 있음을 나타냅니다.

        시사점
        1. **투수와 타자의 균형 변화**: 투수들이 리그 전체적으로 더 우위를 점하고 있다는 것을 보여줍니다. 이는 팀 전략 수립에 있어 투수진 강화가 중요함을 시사합니다.
        2. **타자들의 적응 필요성**: 타자들은 투수들의 변화구와 높은 구속에 대응할 수 있는 기술과 전략을 강화해야 합니다. 특히, 출루율과 장타율을 회복하기 위한 다양한 접근이 필요합니다.
        3. **전략적 변화**: 도루와 같은 전통적인 공격 전략이 감소하고 있음을 반영하여, 팀들은 홈런과 같은 파워 히팅을 극대화하는 방향으로 전략을 재조정할 필요가 있습니다. 이는 타자 발굴 및 훈련에도 영향을 미칠 수 있습니다.
        4. **데이터 분석의 중요성**: 데이터 분석과 인공지능 기술을 활용하여 타자들의 약점을 보완하고, 투수들의 강점을 극대화할 수 있는 맞춤형 전략 수립이 중요합니다.

        이번 분석을 통해 MLB 타자들의 리그 평균 지표 변화 추이를 명확히 파악할 수 있었으며, 이는 선수 평가 및 전략 수립에 중요한 자료로 활용될 수 있을 것입니다. 현대 야구의 전략적 변화와 투수들의 우위 속에서 타자들이 어떻게 적응하고 발전할 수 있을지에 대한 지속적인 연구와 분석이 필요합니다.
        """
        )

    elif selected == pitcher_option: # Changed to use pitcher_option
        st.markdown("---")
        st.subheader("MLB 투수 리그 평균 지표 변화 추이 보고서 (2000-2023)")

        st.markdown(
        """
        1. 개요
        이 보고서는 2000년부터 2023년까지 MLB 투수들의 리그 평균 지표 변화 추이를 분석한 결과입니다. 각 지표별 변화 패턴과 그 의미를 살펴보고, 투수 기록 트렌드의 종합적인 시사점을 도출했습니다.

        2. 분석 대상 지표
        - **ERA (평균자책점)**
        - **WHIP (이닝당 볼넷 + 피안타)**
        - **Wins (승리)**
        - **Losses (패배)**
        - **Strikeouts (탈삼진)**
        - **Innings Pitched (이닝)**
        - **Walks (볼넷)**
        - **Hits Allowed (피안타)**

        3. 주요 지표 분석 및 의미
        """
        )

        for metric in metrics:
            st.markdown(f"#### 3.{metrics.index(metric) + 1}. {metric}")
            fig, ax = plt.subplots(figsize=(10, 5))
            plot_metric(ax, metric, league_avg, moving_avg_5, moving_avg_10, moving_avg_20, lang)
            st.pyplot(fig)

            if metric == "EarnedRunAverage":
                st.markdown(
                    """
                    - **변화 추이**: 2000년대 초반에는 변동이 심하지만, 2010년대 후반부터는 점차 감소하는 추세를 보입니다.
                    - **의미**: 평균자책점의 감소는 투수들의 기량 향상, 특히 구속과 제구력의 향상으로 인한 것입니다. 또한, 투수들이 더 효과적으로 타자들을 상대하고 있음을 나타냅니다.
                    """
                )
            elif metric == "Whip":
                st.markdown(
                    """
                    - **변화 추이**: WHIP는 전반적으로 감소 추세를 보이며, 이는 투수들이 이닝당 볼넷과 피안타를 줄이고 있음을 시사합니다.
                    - **의미**: WHIP의 감소는 투수들의 제구력 향상과 타자들의 출루를 효과적으로 제한하는 능력이 향상되고 있음을 나타냅니다.
                    """
                )
            elif metric == "Wins":
                st.markdown(
                    """
                    - **변화 추이**: 승리 수는 전반적으로 안정적인 추이를 보이며, 최근 몇 년간 약간의 변동이 있습니다.
                    - **의미**: 승리 수의 안정성은 투수들이 경기에서의 성과를 꾸준히 유지하고 있으며, 팀 승리에 효과적으로 기여하고 있음을 나타냅니다.
                    """
                )
            elif metric == "Losses":
                st.markdown(
                    """
                    - **변화 추이**: 패배 수는 전반적으로 안정적인 추이를 보이며, 최근 몇 년간 약간의 감소 추세를 보입니다.
                    - **의미**: 패배 수의 안정성과 감소는 투수들이 경기에서의 성과를 안정적으로 유지하고 있으며, 더 나은 경기 운영을 통해 패배를 줄이고 있음을 나타냅니다.
                    """
                )
            elif metric == "StrikeOuts":
                st.markdown(
                    """
                    - **변화 추이**: 탈삼진 수는 전반적으로 증가 추세를 보이며, 특히 최근 몇 년간 급격히 증가했습니다.
                    - **의미**: 탈삼진 수의 증가는 투수들의 구속과 변화구 능력이 향상되었음을 시사합니다. 또한, 현대 야구에서 투수들이 타자들을 직접 처리하는 것이 더 효과적인 전략으로 인식되고 있음을 반영합니다.
                    """
                )
            elif metric == "InningsPitched":
                st.markdown(
                    """
                    - **변화 추이**: 이닝 수는 전반적으로 안정적인 추이를 보이며, 최근에는 약간의 변동이 있습니다.
                    - **의미**: 이닝 수의 안정성은 투수들이 꾸준히 많은 이닝을 던지며 팀에 기여하고 있음을 나타냅니다. 이는 투수들의 체력 관리와 경기 운영 능력이 향상되었음을 반영합니다.
                    """
                )
            elif metric == "Walks":
                st.markdown(
                    """
                    - **변화 추이**: 볼넷 수는 전반적으로 감소 추세를 보이며, 특히 최근 몇 년간 크게 줄어들었습니다.
                    - **의미**: 볼넷 수의 감소는 투수들의 제구력이 크게 향상되었음을 시사합니다. 이는 투수들이 더 정확한 투구를 통해 타자들을 효과적으로 제어하고 있음을 나타냅니다.
                    """
                )
            elif metric == "HitsAllowed":
                st.markdown(
                    """
                    - **변화 추이**: 피안타 수는 전반적으로 감소 추세를 보이며, 특히 최근 몇 년간 더욱 감소했습니다.
                    - **의미**: 피안타 수의 감소는 투수들이 타자들의 타격을 효과적으로 제한하고 있음을 시사합니다. 이는 투수들의 구위 향상과 더 효과적인 투구 전략의 결과일 수 있습니다.
                    """
                )

        st.markdown(
            """
            ### 4. 결론 및 시사점

            #### 전반적인 추세
            - **투수 성적의 향상**: 여러 지표에서 볼 수 있듯이, 투수들의 성적은 전반적으로 향상되는 추세를 보이고 있습니다. 이는 투수들의 기량 향상, 데이터 분석 기술의 발달, 더 정교해진 투구 전략 등이 복합적으로 작용한 결과일 수 있습니다.
            - **제구력 향상**: 볼넷 수의 감소와 WHIP의 개선에서 볼 수 있듯이, 투수들의 제구력이 크게 향상되었습니다. 이는 투수들이 더 효과적으로 타자들을 상대할 수 있게 해주는 핵심 요소입니다.
            - **탈삼진 능력 향상**: 탈삼진 수의 지속적인 증가는 투수들의 구위와 변화구 능력이 향상되었음을 보여줍니다. 이는 현대 야구에서 투수들이 더 공격적인 투구 스타일을 채택하고 있음을 시사합니다.
            - **기량 안정성**: 승리 수와 이닝 수의 안정적인 추이는 투수들이 일관된 성과를 유지하고 있음을 나타냅니다. 이는 투수들의 체력 관리와 경기 운영 능력의 향상을 반영합니다.

            #### 향후 전망 및 시사점
            1. **투수 육성 전략**: 구속과 제구력 향상에 중점을 둔 투수 육성 전략이 더욱 중요해질 것으로 예상됩니다. 특히, 탈삼진 능력과 볼넷 제한 능력은 핵심 요소로 부각될 것입니다.
            2. **데이터 활용**: 투수 성적 향상을 위해 데이터 분석과 바이오메카닉스 연구의 활용이 더욱 중요해질 것입니다. 이를 통해 투수들의 약점을 보완하고 강점을 극대화할 수 있습니다.
            3. **체력 관리**: 투수들의 꾸준한 성과 유지를 위해 더 효과적인 체력 관리와 부상 예방 전략이 필요합니다. 이는 투수들의 장기적인 성공에 중요한 요소가 될 것입니다.
            4. **투수 육성**: 투수들의 체력 관리, 기술 향상, 멘탈 트레이닝 등 종합적인 육성 프로그램이 중요합니다. 이는 투수들이 장기적으로 안정적인 성과를 유지하는 데 도움이 됩니다.

            이번 분석을 통해 MLB 투수들의 리그 평균 지표 변화 추이를 명확히 파악할 수 있었으며, 이는 선수 평가 및 전략 수립에 중요한 자료로 활용될 수 있을 것입니다. 투수들의 기량 향상과 현대 야구의 전략적 변화가 어떻게 투수 지표에 반영되는지에 대한 지속적인 연구와 분석이 필요합니다.
            """
        )

if __name__ == "__main__":
    run_trend()
