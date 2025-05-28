# src/skills/skill_trend.py

def detect_trend(df):
    if df['emissao_co2_toneladas'].is_monotonic_increasing:
        return "Tendência de alta nas emissões."
    elif df['emissao_co2_toneladas'].is_monotonic_decreasing:
        return "Tendência de queda nas emissões."
    else:
        return "Sem tendência clara."
