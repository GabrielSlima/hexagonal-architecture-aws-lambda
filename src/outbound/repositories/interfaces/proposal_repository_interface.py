from src.domain.entities.proposal import Proposal


class ProposalRepositoryInterface:
    def find_by(self, proposal_id: str) -> Proposal:
        pass
