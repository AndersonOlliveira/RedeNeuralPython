import bubbles 

URLBASE = "https://raw.github.com/Stiivi/cubes/master"  
URL = URLBASE + "/examples/hello_world/data.csv" 

P = bubbles.Pipeline() 
p.source(bubbles.data_object("csv_source", URL, infer_fields=True)) 
p.aggregate("Category", "Amount (US$, Millions)") 
p.pretty_print()