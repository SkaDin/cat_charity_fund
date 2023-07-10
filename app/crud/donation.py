from app.crud.base import CRUDBase
from app.models.donation import Donation


class CRUDDonation(CRUDBase):
    ...


charity_project_crud = CRUDDonation(Donation)
