import pytest
from vision_agent.agent import VisionWorkforceAgent
from vision_agent.tools.data_loader import load_dataset


def test_load_dataset_success():
    res = load_dataset("candidates")
    assert res["status"] == "success"
    assert len(res["data"]) > 0


def test_agent_workflow_execution():
    agent = VisionWorkforceAgent(mode="mock")
    report = agent.run_workflow(enterprise_id="COMP-101")
    
    assert report is not None
    assert "target_enterprise" in report
    assert "analysis_results" in report
    assert "recommendations" in report
    assert report["sdg_mapping"]["primary"] == "SDG 8 (Decent Work and Economic Growth)"
