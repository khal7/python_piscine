import sys
import importlib.util
import importlib.metadata

def check_packages(packages: dict) -> None:

    for pkg, description in packages.items():
        version = importlib.metadata.version(pkg)
        print(f"[OK] {pkg} ({version}) - {description}")

required_modules = {"numpy": "Numerical computation ready",
                     "pandas": "Data manipulation ready",
                       "matplotlib": "Visualization ready",
                         "requests": "Network access ready"}
print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")

for module in required_modules:
    if importlib.util.find_spec(module) is None:
        print(f"[KO] missing package {module}")
        print("\nInstall dependencies using:")
        print("pip install -r requirements.txt or poetry install")
        sys.exit()
import numpy
import pandas
import matplotlib
import requests
import matplotlib.pyplot
check_packages(required_modules)


# randint generate 1000 number and sctore them into a numpy array 
data = numpy.random.randint(0, 100, size=1000)

# so DataFrame create columns and rows of numbers
dataframe = pandas.DataFrame(data, columns=["MatrixValue"])
print(f"Processing {len(dataframe)} data points...")
print("Generating visualization...")

# hist draw a histogram a bar chart that counts how many times numbers appear
# bins=10 split the number int 10 groups. 0-10 in one bar and so on.
# alpha=1 1 means fully visible bar, 0 means invisible
 
matplotlib.pyplot.hist(dataframe["MatrixValue"], bins=10, alpha=1)
matplotlib.pyplot.title("Matrix Data Analysis")
matplotlib.pyplot.xlabel("Value")
matplotlib.pyplot.ylabel("Frequency")
output_file = "matrix_analysis.png"
matplotlib.pyplot.savefig(output_file)
matplotlib.pyplot.close()
print("\nAnalysis complete!")
print(f"Results saved to: {output_file}")
