import joblib

# Save the trained model
joblib.dump(model, 'crop_yield_predictor_model.joblib')

print("Model saved successfully!")
