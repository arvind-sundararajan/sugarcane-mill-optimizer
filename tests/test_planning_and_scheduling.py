```json
{
    "tests/test_planning_and_scheduling.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from scikit_plot import plot
from taskade_agents import Agent
from google.cloud import firestore

# Define a logger
logger = logging.getLogger(__name__)

class PlanningAndSchedulingModel(BaseModel):
    """Model for planning and scheduling."""
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

def plan_and_schedule(model: PlanningAndSchedulingModel) -> Dict:
    """
    Plan and schedule the sugarcane mill production.

    Args:
    model (PlanningAndSchedulingModel): The model containing the planning and scheduling parameters.

    Returns:
    Dict: A dictionary containing the planned and scheduled production.
    """
    try:
        # Initialize the agent
        agent = Agent()
        
        # Get the current state of the mill
        current_state = agent.get_current_state()
        
        # Plan the production
        planned_production = agent.plan_production(model.non_stationary_drift_index, model.stochastic_regime_switch)
        
        # Schedule the production
        scheduled_production = agent.schedule_production(planned_production)
        
        # Log the planned and scheduled production
        logger.info('Planned production: %s', planned_production)
        logger.info('Scheduled production: %s', scheduled_production)
        
        # Return the planned and scheduled production
        return {'planned_production': planned_production, 'scheduled_production': scheduled_production}
    
    except Exception as e:
        # Log the error
        logger.error('Error planning and scheduling production: %s', e)
        return None

def test_planning_and_scheduling() -> None:
    """
    Test the planning and scheduling logic.
    """
    try:
        # Create a model
        model = PlanningAndSchedulingModel(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
        
        # Plan and schedule the production
        result = plan_and_schedule(model)
        
        # Log the result
        logger.info('Result: %s', result)
        
        # Plot the result
        plot(result['planned_production'], result['scheduled_production'])
    
    except Exception as e:
        # Log the error
        logger.error('Error testing planning and scheduling: %s', e)

def simulate_rocket_science() -> None:
    """
    Simulate the 'Rocket Science' problem.
    """
    try:
        # Create a model
        model = PlanningAndSchedulingModel(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
        
        # Plan and schedule the production
        result = plan_and_schedule(model)
        
        # Log the result
        logger.info('Result: %s', result)
        
        # Save the result to Firestore
        db = firestore.Client()
        db.collection('results').document('rocket_science').set(result)
    
    except Exception as e:
        # Log the error
        logger.error('Error simulating rocket science: %s', e)

if __name__ == '__main__':
    simulate_rocket_science()
",
        "commit_message": "feat: implement specialized test_planning_and_scheduling logic"
    }
}
```