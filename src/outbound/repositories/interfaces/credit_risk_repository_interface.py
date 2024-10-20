class CreditRiskRepositoryInterface:
    def find_score_by(self, proposal_id: str) -> int:
        pass

    def find_market_exposure_by(self, proposal_id: str) -> float:
        pass

    def find_approval_by(self, proposal_id: str) -> bool:
        pass
