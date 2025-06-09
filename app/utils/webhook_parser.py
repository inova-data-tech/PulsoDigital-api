# filepath: app/utils/webhook_parser.py

def parse_webhook_payload(payload: dict, topic_id: int) -> dict:
    result = payload.get("resultado", {})
    status = payload.get("status", "deactive")
    avg_rate = result.get("indicador_sentimento", {}).get("media_geral", 0)
    category = result.get("indicador_sentimento", {}).get("categoria", "")
    negative_rate = result.get("distribuicao_avaliacoes", {}).get("negativas", 0)
    neutral_rate = result.get("distribuicao_avaliacoes", {}).get("neutras", 0)
    positive_rate = result.get("distribuicao_avaliacoes", {}).get("positivas", 0)

    dashboard_data = {
        "topic_id": topic_id,
        "status": status,
        "avg_rate": avg_rate,
        "category": category,
        "negative_rate": negative_rate,
        "neutral_rate": neutral_rate,
        "positive_rate": positive_rate,
        "evaluations": []
    }

    data_charts = result.get("dados_graficos", [])
    for aspecto in data_charts:
        product_aspect = aspecto["aspecto"]
        for avaliacao in aspecto["avaliacoes"]:
            dashboard_data["evaluations"].append({
                "product_aspect": product_aspect,
                "rate_date": avaliacao["data"],
                "rate": avaliacao["nota"]
            })
    return dashboard_data