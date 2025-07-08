import emlearn_trees
import array

# local hr, cloud, humidity, precip, temp, wind
features = ["10", "3", "77", "0.0", "87", "4"]
features = [10, 3, 77, int(0.0), 87, 4]

# WBGT: 85
features = [15, 11, 68, int(0.0), 89, 12]

# WBGT: 77
features = [14, 27, 30, int(0.01), 89, 3]

model = emlearn_trees.new(5, 10000, 10000)


# Load a CSV file with the model
with open("dt.csv", "r") as f:
    emlearn_trees.load_model(model, f)

print(model.outputs())
out = array.array("f", range(model.outputs()))
featuresArray = array.array("h", features)

model.predict(featuresArray, out)
print(list(featuresArray), '->', list(out), ':')
