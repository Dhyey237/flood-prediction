from .model import load_model

model = load_model()

def predict_risk(precip, water_level):
    risk_score = 0.5 * precip + 0.5 * water_level
    return "High" if risk_score > model["threshold"] else "Low"
