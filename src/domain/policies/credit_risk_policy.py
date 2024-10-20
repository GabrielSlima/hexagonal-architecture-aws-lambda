from src.domain.policies.credit_risk_policy_enforcement_exception import CreditRiskPolicyEnforcementException


class CreditRiskPolicy:
    def __init__(self, credit_score: int, market_exposure: float, approved: bool) -> None:
        self.credit_score=credit_score
        self.market_exposure=market_exposure
        self.approved=approved

    def assert_can_be_executed(self) -> bool:
        if self.approved:
            return True

        if self.credit_score >= 70 and self.market_exposure <= 2000000:
            return True
        
        raise CreditRiskPolicyEnforcementException("Contract execution not allowed for this client")
