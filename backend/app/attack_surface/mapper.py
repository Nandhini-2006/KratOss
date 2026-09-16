def create_attack_surface(vulnerabilities):
    nodes = []
    edges = []

    for index, vulnerability in enumerate(vulnerabilities):
        node_id = f"crypto_{index + 1}"

        nodes.append({
            "id": node_id,
            "type": "crypto",
            "algorithm": vulnerability["algorithm"],
            "file": vulnerability["file"],
            "line": vulnerability["line"],
            "risk_level": vulnerability["risk_level"],
            "risk_score": vulnerability["risk_score"]
        })

        edges.append({
            "source": "project",
            "target": node_id
        })

    return {
        "nodes": nodes,
        "edges": edges
    }