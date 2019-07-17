import Model
import dataset
import numpy as np
from scipy.spatial import distance

def from_string_to_list(string):
    string = string[1:-1]
    arr = np.fromstring(string, dtype='float32', sep=' ')
    return arr

db = dataset.connect('sqlite:///texts11-04')

table = db.load_table('analyzed')

def smallest_dst(post_text="Hi!"):
    vec = Model.predict(post_text)
    min_dst = 9999
    best_comments = []
    for t in table:
        text_metrics = from_string_to_list(t['vect'])
        #print(t["results"])
        dst = distance.euclidean(text_metrics, vec)
        print(dst)
        if(dst < min_dst and len(t["results"]) > 20):
            print("min dst")
            min_dst = dst
            best_comments = []
            for p in eval(t["results"]):
                print(p)
                best_comments.append(p)
            
    
    print(best_comments)
    print(min_dst)
            
smallest_dst("new single tommorow")

