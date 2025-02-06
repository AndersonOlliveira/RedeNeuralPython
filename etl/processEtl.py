import bonobo
from bonobo.config import use_raw_input

@use_raw_input

def getLinha(row):
    return {"id":row.Id,
            "lagura":row.PetalWidthCm,
            "comprimento":row.PetalLengthCm
            }
def get_grapg():
    return bonobo.Graph(
        bonobo.CsvReader("Iris.csv"),
        getLinha,
        bonobo.JsonWriter("Iris.petalas.json")
    )

bonobo.run(get_grapg())
    
        