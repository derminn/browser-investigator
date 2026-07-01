from extractors.chrome_extractor import ChromeExtractor
from analyzer import Analyzer

extractor = ChromeExtractor("data/History")
history = extractor.extract()
analyzer = Analyzer(history)
print(analyzer.search("github"))
print(f"\nTotal Visits : {len(history)}")
print(len(analyzer.df))
stats = analyzer.statistics()

for key, value in stats.items():
    print(f"{key}: {value}")