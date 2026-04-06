```json
{
    "agents/agent.py": {
        "content": "
import logging
from typing import Dict, List
from pydantic import BaseModel
from scikit_plot import plot
from google.cloud import firestore
from pipedrive import Pipedrive

class Agent(BaseModel):
    """Base agent model"""
    id: str
    name: str
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

    def __init__(self, id: str, name: str, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize the agent

        Args:
        - id (str): Unique identifier
        - name (str): Agent name
        - non_stationary_drift_index (float): Drift index
        - stochastic_regime_switch (bool): Regime switch flag
        """
        self.id = id
        self.name = name
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch

    def update_non_stationary_drift_index(self, new_index: float) -> None:
        """
        Update the non-stationary drift index

        Args:
        - new_index (float): New drift index

        Raises:
        - ValueError: If the new index is not a valid float
        """
        try:
            if not isinstance(new_index, float):
                raise ValueError(\"New index must be a float\")
            self.non_stationary_drift_index = new_index
            logging.info(f\"Updated non-stationary drift index for agent {self.id} to {new_index}\")
        except Exception as e:
            logging.error(f\"Error updating non-stationary drift index: {e}\")

    def switch_stochastic_regime(self) -> None:
        """
        Switch the stochastic regime

        Raises:
        - Exception: If an error occurs during the switch
        """
        try:
            self.stochastic_regime_switch = not self.stochastic_regime_switch
            logging.info(f\"Switched stochastic regime for agent {self.id}\")
        except Exception as e:
            logging.error(f\"Error switching stochastic regime: {e}\")

    def plot_performance(self) -> None:
        """
        Plot the agent's performance

        Raises:
        - Exception: If an error occurs during plotting
        """
        try:
            plot(self.id, self.name)
            logging.info(f\"Plotted performance for agent {self.id}\")
        except Exception as e:
            logging.error(f\"Error plotting performance: {e}\")

    def sync_with_firestore(self) -> None:
        """
        Sync the agent's data with Firestore

        Raises:
        - Exception: If an error occurs during syncing
        """
        try:
            db = firestore.Client()
            doc_ref = db.collection(\"agents\").document(self.id)
            doc_ref.set({
                \"name\": self.name,
                \"non_stationary_drift_index\": self.non_stationary_drift_index,
                \"stochastic_regime_switch\": self.stochastic_regime_switch
            })
            logging.info(f\"Synced agent {self.id} data with Firestore\")
        except Exception as e:
            logging.error(f\"Error syncing agent data with Firestore: {e}\")

    def sync_with_pipedrive(self) -> None:
        """
        Sync the agent's data with Pipedrive

        Raises:
        - Exception: If an error occurs during syncing
        """
        try:
            pd = Pipedrive()
            pd.update_agent(self.id, self.name, self.non_stationary_drift_index, self.stochastic_regime_switch)
            logging.info(f\"Synced agent {self.id} data with Pipedrive\")
        except Exception as e:
            logging.error(f\"Error syncing agent data with Pipedrive: {e}\")

if __name__ == \"__main__\":
    # Simulation of the 'Rocket Science' problem
    agent = Agent(\"agent-1\", \"Rocket Science\", 0.5, True)
    agent.update_non_stationary_drift_index(0.7)
    agent.switch_stochastic_regime()
    agent.plot_performance()
    agent.sync_with_firestore()
    agent.sync_with_pipedrive()
",
        "commit_message": "feat: implement specialized agent logic"
    }
}
```