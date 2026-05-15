class ClientScorer:
    def __init__(self):
        pass

    def calculate_trust_score(self, client_data: dict) -> float:
        """
        Calculates a trust score based on history, payment status, and reviews.
        """
        score = 50.0 # Baseline
        
        if client_data.get("payment_verified"):
            score += 20
        
        if client_data.get("total_spent", 0) > 10000:
            score += 15
        
        reviews = client_data.get("reviews", [])
        if reviews:
            avg_rating = sum([r['rating'] for r in reviews]) / len(reviews)
            score += (avg_rating - 3) * 10
            
        return min(100, max(0, score))

    def detect_toxicity(self, job_description: str) -> dict:
        """
        Detects signs of a toxic or difficult client.
        """
        toxic_keywords = ["urgent", "cheap", "fast", "asap", "lowest price", "fixed budget no negotiation"]
        matches = [word for word in toxic_keywords if word in job_description.lower()]
        
        risk_level = "Low"
        if len(matches) > 2:
            risk_level = "High"
        elif len(matches) > 0:
            risk_level = "Medium"
            
        return {
            "risk_level": risk_level,
            "indicators": matches
        }
