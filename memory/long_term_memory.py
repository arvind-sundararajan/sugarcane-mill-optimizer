```json
{
    "memory/long_term_memory.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from scikit_plot import plot_learning_curve
from google.cloud import firestore

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LongTermMemory(BaseModel):
    """Represents a long-term memory entity."""
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initializes a LongTermMemory instance.

        Args:
        - non_stationary_drift_index (float): The non-stationary drift index.
        - stochastic_regime_switch (bool): Whether the stochastic regime switch is enabled.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch

    def update_memory(self, new_data: List[float]) -> None:
        """
        Updates the long-term memory with new data.

        Args:
        - new_data (List[float]): The new data to update the memory with.

        Raises:
        - ValueError: If the new data is empty.
        """
        try:
            if not new_data:
                raise ValueError('New data cannot be empty')
            # Update the memory using the new data
            self.non_stationary_drift_index = sum(new_data) / len(new_data)
            logger.info('Updated long-term memory with new data')
        except Exception as e:
            logger.error(f'Error updating long-term memory: {str(e)}')

    def get_memory_state(self) -> Dict[str, float]:
        """
        Gets the current state of the long-term memory.

        Returns:
        - Dict[str, float]: A dictionary containing the current state of the memory.
        """
        try:
            # Get the current state of the memory
            memory_state = {'non_stationary_drift_index': self.non_stationary_drift_index}
            logger.info('Retrieved long-term memory state')
            return memory_state
        except Exception as e:
            logger.error(f'Error retrieving long-term memory state: {str(e)}')

def simulate_rocket_science() -> None:
    """
    Simulates the 'Rocket Science' problem using the long-term memory.
    """
    try:
        # Initialize the long-term memory
        long_term_memory = LongTermMemory(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
        
        # Update the long-term memory with new data
        new_data = [0.1, 0.2, 0.3]
        long_term_memory.update_memory(new_data)
        
        # Get the current state of the long-term memory
        memory_state = long_term_memory.get_memory_state()
        logger.info(f'Long-term memory state: {memory_state}')
        
        # Plot the learning curve
        plot_learning_curve(memory_state['non_stationary_drift_index'])
        
        # Save the memory state to Firestore
        db = firestore.Client()
        doc_ref = db.collection('long_term_memory').document('memory_state')
        doc_ref.set(memory_state)
        logger.info('Saved long-term memory state to Firestore')
    except Exception as e:
        logger.error(f'Error simulating rocket science: {str(e)}')

if __name__ == '__main__':
    simulate_rocket_science()
",
        "commit_message": "feat: implement specialized long_term_memory logic"
    }
}
```