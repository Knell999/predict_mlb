"""
다국어 지원 모듈: 다양한 언어로 텍스트를 제공합니다.
"""
from typing import Dict, List, Any, Optional

# 한국어 텍스트 사전
KO = {
    # 공통
    "app_title": "MLB 선수 기록 조회 및 예측 서비스",
    "home": "홈",
    "trend_analysis": "트렌드 분석",
    "search_records": "기록 조회",
    "predict_records": "기록 예측",
    
    # 홈 페이지
    "welcome_message": "야구 팬 여러분, 안녕하세요! 👋",
    "app_intro": "MLB 선수 기록 조회 및 예측 서비스에 오신 것을 환영합니다. 🎉",
    "app_description": "이 플랫폼은 **Major League Baseball (MLB)** 선수들의 기록을 쉽게 조회하고, 다양한 지표를 분석하며, 앞으로의 성과를 예측할 수 있는 종합적인 대시보드입니다. 📈",
    "main_features": "✨ 주요 기능 ✨",
    "search_feature": "🔍 선수 기록 조회",
    "prediction_feature": "🔮 성과 예측",
    "visualization_feature": "📈 데이터 시각화",
    "learn_more": "🤔 더 알아보기",
    
    # 검색 페이지
    "search_title": "MLB 선수 기록 조회👁️",
    "select_player": "선수를 선택하세요:",
    "select_season": "시즌을 선택하세요:",
    "player_info": "선수 정보",
    "visualization_title": "선수 기록 시각화",
    "compare_with_league": "선수와 리그 평균 비교 (히스토그램)",
    "no_record": "해당 선수의 기록을 찾을 수 없습니다.",
    
    # 예측 페이지
    "predict_title": "MLB 선수 기록 예측",
    "player_option": "선수 및 옵션 선택",
    "prediction_tab": "기록 예측",
    "prediction_result": "예측 결과",
    "prediction_warning": "의 최근 2개년(2022, 2023) 시즌 데이터가 없어 예측이 불가능합니다.",
    
    # 트렌드 페이지
    "trend_title": "MLB 리그 트렌드 분석",
    "select_metrics": "분석할 지표 선택",
    "trend_overview": "리그 평균 지표 변화 추이",
    "moving_average": "이동평균 설명",
    "select_metric_warning": "분석할 지표를 하나 이상 선택해주세요.",
    
    # 기타
    "loading": "로딩 중...",
    "error": "오류가 발생했습니다",
    "year": "년",
    "player": "선수",
    "team": "팀",
    "stats": "기록",
}

# 영어 텍스트 사전
EN = {
    # Common
    "app_title": "MLB Player Stats Search and Prediction Service",
    "home": "Home",
    "trend_analysis": "Trend Analysis",
    "search_records": "Search Records",
    "predict_records": "Predict Records",
    
    # Home page
    "welcome_message": "Hello, baseball fans! 👋",
    "app_intro": "Welcome to the MLB Player Stats Search and Prediction Service! 🎉",
    "app_description": "This platform is a comprehensive dashboard that allows you to easily search for **Major League Baseball (MLB)** player records, analyze various metrics, and predict future performance. 📈",
    "main_features": "✨ Main Features ✨",
    "search_feature": "🔍 Player Records Search",
    "prediction_feature": "🔮 Performance Prediction",
    "visualization_feature": "📈 Data Visualization",
    "learn_more": "🤔 Learn More",
    
    # Search page
    "search_title": "MLB Player Records Search👁️",
    "select_player": "Select a player:",
    "select_season": "Select a season:",
    "player_info": "Player Information",
    "visualization_title": "Player Records Visualization",
    "compare_with_league": "Player vs League Average (Histogram)",
    "no_record": "No records found for this player.",
    
    # Predict page
    "predict_title": "MLB Player Records Prediction",
    "player_option": "Select Player and Options",
    "prediction_tab": "Records Prediction",
    "prediction_result": "Prediction Results",
    "prediction_warning": " does not have recent data (2022, 2023) required for prediction.",
    
    # Trend page
    "trend_title": "MLB League Trend Analysis",
    "select_metrics": "Select metrics to analyze",
    "trend_overview": "League Average Metrics Trend",
    "moving_average": "Moving Average Explanation",
    "select_metric_warning": "Please select at least one metric to analyze.",
    
    # Other
    "loading": "Loading...",
    "error": "An error occurred",
    "year": "Year",
    "player": "Player",
    "team": "Team",
    "stats": "Stats",
}

# 일본어 텍스트 사전
JA = {
    # 共通
    "app_title": "MLB選手記録検索・予測サービス",
    "home": "ホーム",
    "trend_analysis": "トレンド分析",
    "search_records": "記録検索",
    "predict_records": "記録予測",
    
    # ホームページ
    "welcome_message": "野球ファンの皆様、こんにちは！ 👋",
    "app_intro": "MLB選手記録検索・予測サービスへようこそ！ 🎉",
    "app_description": "このプラットフォームは、**Major League Baseball (MLB)** 選手の記録を簡単に検索し、様々な指標を分析し、将来のパフォーマンスを予測できる総合的なダッシュボードです。 📈",
    "main_features": "✨ 主な機能 ✨",
    "search_feature": "🔍 選手記録検索",
    "prediction_feature": "🔮 パフォーマンス予測",
    "visualization_feature": "📈 データ可視化",
    "learn_more": "🤔 詳細を見る",
    
    # 検索ページ
    "search_title": "MLB選手記録検索👁️",
    "select_player": "選手を選択:",
    "select_season": "シーズンを選択:",
    "player_info": "選手情報",
    "visualization_title": "選手記録の可視化",
    "compare_with_league": "選手とリーグ平均の比較 (ヒストグラム)",
    "no_record": "この選手の記録は見つかりませんでした。",
    
    # 予測ページ
    "predict_title": "MLB選手記録予測",
    "player_option": "選手とオプションの選択",
    "prediction_tab": "記録予測",
    "prediction_result": "予測結果",
    "prediction_warning": "の最近2年間(2022、2023)のデータがないため、予測できません。",
    
    # トレンドページ
    "trend_title": "MLBリーグトレンド分析",
    "select_metrics": "分析する指標を選択",
    "trend_overview": "リーグ平均指標の変化傾向",
    "moving_average": "移動平均の説明",
    "select_metric_warning": "分析する指標を少なくとも1つ選択してください。",
    
    # その他
    "loading": "読み込み中...",
    "error": "エラーが発生しました",
    "year": "年",
    "player": "選手",
    "team": "チーム",
    "stats": "記録",
}

# 언어 사전 매핑
LANGUAGE_DICTS = {
    "ko": KO,
    "en": EN,
    "ja": JA
}

def get_text(key: str, lang: str = "ko") -> str:
    """
    지정된 언어로 텍스트를 반환합니다.
    
    Args:
        key: 텍스트 키
        lang: 언어 코드
        
    Returns:
        str: 해당 언어의 텍스트
    """
    language_dict = LANGUAGE_DICTS.get(lang, KO)
    return language_dict.get(key, key)

def get_languages() -> Dict[str, str]:
    """
    지원되는 언어 목록을 반환합니다.
    
    Returns:
        Dict[str, str]: 언어 코드와 이름 매핑
    """
    return {
        "ko": "한국어",
        "en": "English",
        "ja": "日本語"
    }

def get_supported_languages() -> List[str]:
    """
    지원되는 언어 코드 목록을 반환합니다.
    
    Returns:
        List[str]: 지원되는 언어 코드 목록
    """
    return list(LANGUAGE_DICTS.keys())
