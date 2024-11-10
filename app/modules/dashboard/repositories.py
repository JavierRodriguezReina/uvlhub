from app.modules.dataset.models import DataSet
from core.repositories.BaseRepository import BaseRepository

class DashboardRepository(BaseRepository):
    def __init__(self):
        super().__init__(DataSet)  # Utilizamos DataSet en lugar de Notepad para contar los datasets

    def get_dataset_count(self):
        return DataSet.query.count()
