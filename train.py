from Classes.Model import LungModel

if __name__ == "__main__":
    # Create Model
    model = LungModel("C:/Users/alenk/Projects/ivp/LungDiseaseClassification/Data")

    # Train model
    model.train(15)