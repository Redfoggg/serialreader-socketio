from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType


Base = declarative_base()

class DadosParaPlotar(Base):
    
    __tablename__="DadosParaPlotar"
    id = Column(Integer, primary_key = True)
    periodo = Column(Integer, nullable = False)
    dataEHora = Column(DateTime, nullable = False)
    Id_maquina = Column(String, nullable = False)
    posicao_x = Column(String, nullable = False)
    posicao_y = Column(String, nullable = False)

    def __repr__(self):
        return "<DadosParaPlotar(periodo= '{}', dataEHora= '{}', posicao_x= '{}', posicao_y= '{}', Id_maquina= '{}')>"\
            .format(self.periodo, self.dataEHora, self.posicao_x, self.posicao_y, self.Id_maquina)

