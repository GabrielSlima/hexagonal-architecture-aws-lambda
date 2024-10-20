from src.outbound.repositories.interfaces.proposal_repository_interface import ProposalRepositoryInterface
from src.outbound.repositories.interfaces.credit_risk_repository_interface import CreditRiskRepositoryInterface
from src.domain.entities.contract import Contract
from src.domain.policies.credit_risk_policy import CreditRiskPolicy


class ContractService:
    def __init__(self, credit_risk_repository: CreditRiskRepositoryInterface, proposal_repository: ProposalRepositoryInterface) -> None:
        self.credit_risk_repository = credit_risk_repository
        self.proposal_repository = proposal_repository
    
    def execute_by(self, proposal_id: str) -> Contract:
        proposal = self.proposal_repository.find_by(proposal_id)
        counterparty_credit_score = self.credit_risk_repository.find_score_by(proposal.counterparty_id)
        market_exposure = self.credit_risk_repository.find_market_exposure_by(proposal.counterparty_id)
        approved_by_management = self.credit_risk_repository.find_approval_by(proposal.counterparty_id)

        credit_risk_policy = CreditRiskPolicy(counterparty_credit_score, market_exposure, approved_by_management)
        credit_risk_policy.assert_can_be_executed()
