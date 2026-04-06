```json
{
    "tests/test_memory.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from sklearn.metrics import mean_squared_error
from scikit_plot import plot_confusion_matrix
from google.cloud import firestore

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MemoryTest(BaseModel):
    """Memory test configuration"""
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """Initialize memory test configuration"""
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch

    def run_test(self) -> Dict:
        """Run memory test and return results"""
        try:
            # Initialize Firestore client
            db = firestore.Client()
            # Get test data from Firestore
            test_data_ref = db.collection('test_data').document('memory_test')
            test_data = test_data_ref.get().to_dict()
            # Run test using scikit-plot
            plot_confusion_matrix(test_data['y_true'], test_data['y_pred'])
            # Calculate mean squared error
            mse = mean_squared_error(test_data['y_true'], test_data['y_pred'])
            # Log results
            logger.info(f'MSE: {mse}')
            return {'mse': mse}
        except Exception as e:
            logger.error(f'Error running test: {e}')
            return {'error': str(e)}

def simulate_rocket_science(non_stationary_drift_index: float, stochastic_regime_switch: bool) -> List[float]:
    """Simulate rocket science problem"""
    try:
        # Initialize memory test configuration
        memory_test = MemoryTest(non_stationary_drift_index, stochastic_regime_switch)
        # Run memory test
        results = memory_test.run_test()
        # Simulate rocket science problem using results
        rocket_science_results = [results['mse'] * i for i in range(10)]
        return rocket_science_results
    except Exception as e:
        logger.error(f'Error simulating rocket science: {e}')
        return []

if __name__ == '__main__':
    # Simulate rocket science problem
    non_stationary_drift_index = 0.5
    stochastic_regime_switch = True
    rocket_science_results = simulate_rocket_science(non_stationary_drift_index, stochastic_regime_switch)
    # Log results
    logger.info(f'Rocket science results: {rocket_science_results}')
",
        "commit_message": "feat: implement specialized test_memory logic"
    }
}
```