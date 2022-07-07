import featureform as ff

client = ff.ServingClient()
dataset = client.dataset("fraud_training","quickstart")
training_dataset = dataset.repeat(10).shuffle(1000).batch(8)
for feature_batch in training_dataset:
    print(feature_batch)


fpf = client.features([("avg_transactions", "quickstart")], {"user":"C1410926"})