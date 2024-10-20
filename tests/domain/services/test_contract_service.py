from unittest import mock
import pytest
from datetime import date
from src.domain.entities.proposal import Proposal
from src.domain.value_objects.supply_vo import SupplyVO
from src.domain.value_objects.price_vo import PriceVO
from src.domain.services.contract_service import ContractService
from src.domain.policies.credit_risk_policy_enforcement_exception import CreditRiskPolicyEnforcementException
from src.outbound.repositories.interfaces.credit_risk_repository_interface import CreditRiskRepositoryInterface
from src.outbound.repositories.interfaces.proposal_repository_interface import ProposalRepositoryInterface

@pytest.fixture
def proposal():
    return Proposal(
        counterparty_id="any",
        start_date=date(2025, 1, 1),
        end_date=date(2025, 2, 28),
        supplies=[
            SupplyVO(
                start_day=date(2025, 1, 1),
                end_day=date(2025, 1, 31),
                submarket="SOUTHEAST",
                source="hydro",
                volume=10,
                price=PriceVO(value=10, currency="BRL")
            ),
            SupplyVO(
                start_day=date(2025, 2, 1),
                end_day=date(2025, 2, 28),
                submarket="SOUTHEAST",
                source="hydro",
                volume=10,
                price=PriceVO(value=10, currency="BRL")
            )
        ]
    )


def test_contract_execution_non_existent_proposal_should_raise_exception():
    assert False

def test_contract_execution_from_proposal_customer_with_bad_score_should_be_denied(proposal):
    credit_risk_repository_stub = mock.create_autospec(CreditRiskRepositoryInterface)
    credit_risk_repository_stub.find_score_by.return_value = 50
    credit_risk_repository_stub.find_market_exposure_by.return_value = 1000
    credit_risk_repository_stub.find_approval_by.return_value = False

    proposal_repository_stub = mock.create_autospec(ProposalRepositoryInterface)
    proposal_repository_stub.find_by.return_value = proposal

    contract_service = ContractService(credit_risk_repository_stub, proposal_repository_stub)

    with pytest.raises(CreditRiskPolicyEnforcementException) as ex:
        contract_service.execute_by(proposal_id="666")

def test_contract_execution_from_proposal_customer_with_bad_score_but_management_approval():
    assert False

def test_contract_execution_from_proposal_customer_with_market_exposure_over_limitations_should_be_denied():
    assert False

def test_contract_execution_from_proposal_customer_with_market_exposure_over_limitations_but_management_approval():
    assert False


def test_contract_execution_from_proposal_customer_with_market_exposure_over_limitations_and_bad_score_should_be_denied():
    assert False


def test_contract_execution_customer_with_good_credit_score_low_market_exposure():
    assert False
