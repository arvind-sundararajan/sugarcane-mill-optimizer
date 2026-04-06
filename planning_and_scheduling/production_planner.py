```json
{
    "planning_and_scheduling/production_planner.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from scikit_plot import plot
from google.cloud import firestore
from pipedrive import Pipedrive

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductionPlan(BaseModel):
    """Production plan model"""
    non_stationary_drift_index: float
    stochastic_regime_switch: bool
    sugarcane_yield: int

class ProductionPlanner:
    """Production planner class"""
    def __init__(self, db: firestore.Client):
        """
        Initialize production planner

        Args:
        db (firestore.Client): Firestore client
        """
        self.db = db

    def plan_production(self, sugarcane_yield: int) -> ProductionPlan:
        """
        Plan production based on sugarcane yield

        Args:
        sugarcane_yield (int): Sugarcane yield

        Returns:
        ProductionPlan: Production plan
        """
        try:
            # Calculate non-stationary drift index
            non_stationary_drift_index = self.calculate_non_stationary_drift_index(sugarcane_yield)
            # Determine stochastic regime switch
            stochastic_regime_switch = self.determine_stochastic_regime_switch(non_stationary_drift_index)
            # Create production plan
            production_plan = ProductionPlan(
                non_stationary_drift_index=non_stationary_drift_index,
                stochastic_regime_switch=stochastic_regime_switch,
                sugarcane_yield=sugarcane_yield
            )
            return production_plan
        except Exception as e:
            logger.error(f\"Error planning production: {e}\")
            return None

    def calculate_non_stationary_drift_index(self, sugarcane_yield: int) -> float:
        """
        Calculate non-stationary drift index

        Args:
        sugarcane_yield (int): Sugarcane yield

        Returns:
        float: Non-stationary drift index
        """
        try:
            # Calculate non-stationary drift index using scikit-plot
            non_stationary_drift_index = plot.calculate_drift_index(sugarcane_yield)
            return non_stationary_drift_index
        except Exception as e:
            logger.error(f\"Error calculating non-stationary drift index: {e}\")
            return 0.0

    def determine_stochastic_regime_switch(self, non_stationary_drift_index: float) -> bool:
        """
        Determine stochastic regime switch

        Args:
        non_stationary_drift_index (float): Non-stationary drift index

        Returns:
        bool: Stochastic regime switch
        """
        try:
            # Determine stochastic regime switch using pipedrive
            stochastic_regime_switch = Pipedrive.determine_regime_switch(non_stationary_drift_index)
            return stochastic_regime_switch
        except Exception as e:
            logger.error(f\"Error determining stochastic regime switch: {e}\")
            return False

if __name__ == \"__main__\":
    # Create Firestore client
    db = firestore.Client()
    # Create production planner
    production_planner = ProductionPlanner(db)
    # Plan production
    sugarcane_yield = 1000
    production_plan = production_planner.plan_production(sugarcane_yield)
    # Log production plan
    logger.info(f\"Production plan: {production_plan}\")
        ",
        "commit_message": "feat: implement specialized production_planner logic"
    }
}
```