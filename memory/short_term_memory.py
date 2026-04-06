```json
{
    "memory/short_term_memory.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from sklearn.metrics import mean_squared_error
from scikit_plot import plot_confusion_matrix

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ShortTermMemory(BaseModel):
    """
    Model for short term memory.
    
    Attributes:
    non_stationary_drift_index (float): Index of non-stationary drift.
    stochastic_regime_switch (bool): Flag for stochastic regime switch.
    """
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize the ShortTermMemory model.
        
        Args:
        non_stationary_drift_index (float): Index of non-stationary drift.
        stochastic_regime_switch (bool): Flag for stochastic regime switch.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch

    def update_memory(self, new_data: List[float]) -> None:
        """
        Update the short term memory with new data.
        
        Args:
        new_data (List[float]): New data to update the memory.
        
        Raises:
        Exception: If the update fails.
        """
        try:
            # Update the memory using the new data
            self.non_stationary_drift_index = self._calculate_drift_index(new_data)
            logger.info('Memory updated successfully')
        except Exception as e:
            logger.error(f'Error updating memory: {e}')
            raise Exception('Error updating memory')

    def _calculate_drift_index(self, data: List[float]) -> float:
        """
        Calculate the drift index for the given data.
        
        Args:
        data (List[float]): Data to calculate the drift index for.
        
        Returns:
        float: The calculated drift index.
        """
        try:
            # Calculate the drift index using the data
            drift_index = mean_squared_error(data, [0] * len(data))
            return drift_index
        except Exception as e:
            logger.error(f'Error calculating drift index: {e}')
            raise Exception('Error calculating drift index')

    def plot_memory(self, data: List[float]) -> None:
        """
        Plot the short term memory using the given data.
        
        Args:
        data (List[float]): Data to plot the memory for.
        
        Raises:
        Exception: If the plotting fails.
        """
        try:
            # Plot the memory using the data
            plot_confusion_matrix(data, [0] * len(data))
            logger.info('Memory plotted successfully')
        except Exception as e:
            logger.error(f'Error plotting memory: {e}')
            raise Exception('Error plotting memory')

def simulate_rocket_science() -> None:
    """
    Simulate the 'Rocket Science' problem.
    """
    try:
        # Create a short term memory model
        memory = ShortTermMemory(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
        
        # Update the memory with new data
        new_data = [1, 2, 3, 4, 5]
        memory.update_memory(new_data)
        
        # Plot the memory
        memory.plot_memory(new_data)
        
        logger.info('Rocket science simulation completed successfully')
    except Exception as e:
        logger.error(f'Error simulating rocket science: {e}')

if __name__ == '__main__':
    simulate_rocket_science()
",
        "commit_message": "feat: implement specialized short_term_memory logic"
    }
}
```