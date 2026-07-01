import pandas as pd 
from urllib.parse import urlparse

class Analyzer:
    
    def __init__(self,history):
        self.df = self.load_data(history)
    
    
    
    def load_data(self,history):
        df = pd.DataFrame(history)
        return df 
    
    
    def timeline(self):
        self.df["date"] = self.df["timestamp"].apply(lambda x: x.date())
        timeline = self.df.groupby("date").size()
        return timeline

    
    def active_hours(self):
        self.df["hour"] = self.df["timestamp"].apply(lambda x: x.hour)
        active_hours = self.df.groupby("hour").size()
        return active_hours
    
    
    
    def top_domains(self):
        self.df["domain"] = self.df["url"].apply(
            lambda x: urlparse(x).netloc
        )
        top_domains = (
            self.df
            .groupby("domain")
            .size()
            .sort_values(ascending=False)
            .head(10)
        )
        
        return top_domains          
    
   
   
    def top_pages(self):
        top_pages = (
            self.df
            .groupby("url")
            .agg(
                title=("title","first"),
                visits=("url","count")
            )
            .sort_values("visits",ascending=False)
            .head(10)
            .reset_index()
        )
        return top_pages

    
    
    def search(self, keyword):
        results = self.df[
            (
               self.df["title"].str.contains(keyword,case=False,na=False)
            )
            |
            (
                self.df["url"].str.contains(keyword,case=False,na=False)
            )
        ]
        results = results.sort_values(
            "timestamp",
            ascending=False
        )
        return results
        
        
    def statistics(self):
        stats={}
        stats["Total Visits"] = len(self.df)
        stats["unique URL"] = self.df["url"].nunique()
        if "domain" not in self.df.columns:
            self.df["domain"] = self.df["url"].apply(
                lambda x: urlparse(x).netloc
            )
        stats["First Visit"] = self.df["timestamp"].min()
        stats["Lasr Visit"] = self.df["timestamp"].max()
        stats["Most Active Day"] = self.timeline().idxmax()
        stats["Most Active Hour"] = self.active_hours().idxmax()
        stats["Most Visited Domain"] = self.top_domains().idxmax()
        stats["Top Page"] = {
            "title": self.top_pages()["title"],
            "url": self.top_pages()["url"],
            "visits":self.top_pages()["visits"]
         }
        return stats 
