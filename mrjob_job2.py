from mrjob.job import MRJob
from mrjob.step import MRStep

class MovieLensData_Analysis(MRJob):
    
    def mapper(self, _, line):
        words = line.split(',')
        yield words[0], 1
    
    def reducer(self, country, values):
        yield (country, sum(values))
        
        
if __name__ == '__main__':
    MovieLensData_Analysis.run()
