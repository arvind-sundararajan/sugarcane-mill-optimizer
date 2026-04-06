```json
{
    "tests/test_agent.py": {
        "content": "
import logging
from typing import Dict, List
from pydantic import BaseModel
from logfire import Logger
from scikit_plot import plot_drift
from taskade import Agent

# Set up logging
logger = Logger(__name__)

class SugarcaneMillOptimizer(BaseModel):
    """Sugarcane mill optimization model"""
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

class TestAgent:
    """Test agent for sugarcane mill optimization"""
    def __init__(self, agent_id: int, mill_optimizer: SugarcaneMillOptimizer):
        """
        Initialize test agent

        Args:
        - agent_id (int): Unique agent ID
        - mill_optimizer (SugarcaneMillOptimizer): Sugarcane mill optimization model
        """
        self.agent_id = agent_id
        self.mill_optimizer = mill_optimizer

    def optimize_mill(self, data: Dict[str, List[float]]) -> Dict[str, float]:
        """
        Optimize sugarcane mill using provided data

        Args:
        - data (Dict[str, List[float]]): Input data for optimization

        Returns:
        - Dict[str, float]: Optimized mill parameters
        """
        try:
            # Use taskade to run optimization task
            task = Agent.run_task(self.agent_id, 'optimize_mill', data)
            result = task.result
            logger.info(f'Optimization result: {result}')
            return result
        except Exception as e:
            logger.error(f'Error optimizing mill: {e}')
            return {}

    def detect_drift(self, data: Dict[str, List[float]]) -> float:
        """
        Detect non-stationary drift in provided data

        Args:
        - data (Dict[str, List[float]]): Input data for drift detection

        Returns:
        - float: Non-stationary drift index
        """
        try:
            # Use scikit-plot to detect drift
            drift_index = plot_drift(data)
            logger.info(f'Drift index: {drift_index}')
            return drift_index
        except Exception as e:
            logger.error(f'Error detecting drift: {e}')
            return 0.0

    def switch_regime(self, data: Dict[str, List[float]]) -> bool:
        """
        Switch stochastic regime based on provided data

        Args:
        - data (Dict[str, List[float]]): Input data for regime switching

        Returns:
        - bool: Whether regime switch was successful
        """
        try:
            # Use taskade to run regime switching task
            task = Agent.run_task(self.agent_id, 'switch_regime', data)
            result = task.result
            logger.info(f'Regime switch result: {result}')
            return result
        except Exception as e:
            logger.error(f'Error switching regime: {e}')
            return False

if __name__ == '__main__':
    # Simulate 'Rocket Science' problem
    mill_optimizer = SugarcaneMillOptimizer(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
    test_agent = TestAgent(1, mill_optimizer)
    data = {'input1': [1.0, 2.0, 3.0], 'input2': [4.0, 5.0, 6.0]}
    optimized_params = test_agent.optimize_mill(data)
    drift_index = test_agent.detect_drift(data)
    regime_switched = test_agent.switch_regime(data)
    logger.info(f'Optimized params: {optimized_params}, Drift index: {drift_index}, Regime switched: {regime_switched}')
",
        "commit_message": "feat: implement specialized test_agent logic"
    }
}
```