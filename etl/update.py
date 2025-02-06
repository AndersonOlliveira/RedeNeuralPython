import panda as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymsql://{user}:{pw}@localhot/{db}".format(user="andersonOliveira",
                                                                         pw="123456",db="suporte_visium"))
df.to_sql('tb_solucoes', con=engine, if_exists='append', chunkize=200)
          