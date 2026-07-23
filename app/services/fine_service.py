from app.models.fine import Fine
from app.models.enums import FineStatus
from app.repositories.fine_repository import FineRepository
from app.exceptions.errors import ConflictError, NotFoundError

class FineService:
    def __init__(self, fine_repo: FineRepository) -> None:
        self._fine_repo = fine_repo

    def list_pending_fines(self)-> list[Fine]:
        return self._fine_repo.list_pending()

    def pay_fine(self ,fine_id:int)->Fine:
        fine=self._fine_repo.get_by_id(fine_id)
        if fine is None:
            raise NotFoundError(f"No fine found with id {fine_id} ")
        if fine.status==FineStatus.PAID:
            raise ConflictError(f"Fine with id {fine_id} is already paid")
        fine.status=FineStatus.PAID
        return fine