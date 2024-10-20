from datetime import date
from src.domain.value_objects.supply_vo import SupplyVO
from src.domain.value_objects.price_vo import PriceVO
from src.domain.entities.proposal import Proposal
from src.domain.policies.credit_risk_policy import CreditRiskPolicy
import pytest
from src.domain.policies.credit_risk_policy_enforcement_exception import CreditRiskPolicyEnforcementException


def test_contract_execution_on_counterparty_score_bellow_allowed_for_proposals():
    policy = CreditRiskPolicy(credit_score=70, market_exposure=10000, approved=True)
    assert policy.assert_can_be_executed()

def test_contract_execution_on_counterparty_market_exposure_higher_than_20_mm():
    policy = CreditRiskPolicy(credit_score=70, market_exposure=21000000, approved=False)
    with pytest.raises(CreditRiskPolicyEnforcementException) as ex:
        policy.assert_can_be_executed()


def test_contract_exectuion_on_counterparty_special_terms_approved():
    policy = CreditRiskPolicy(credit_score=12, market_exposure=21000000, approved=True)
    assert policy.assert_can_be_executed()