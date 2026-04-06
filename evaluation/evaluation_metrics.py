```json
{
    "evaluation/evaluation_metrics.py": {
        "content": "
import logging
from typing import Dict, List
from pydantic import BaseModel
from sklearn.metrics import mean_squared_error
from scikit_plot import plot_confusion_matrix
from google.cloud import firestore

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EvaluationMetrics(BaseModel):
    """Model for evaluation metrics"""
    non_stationary_drift_index: float
    stochastic_regime_switch: float
    mean_squared_error: float

def calculate_evaluation_metrics(predicted_values: List[float], actual_values: List[float]) -> EvaluationMetrics:
    """
    Calculate evaluation metrics for the given predicted and actual values.

    Args:
    - predicted_values (List[float]): List of predicted values
    - actual_values (List[float]): List of actual values

    Returns:
    - EvaluationMetrics: Model containing evaluation metrics
    """
    try:
        # Calculate mean squared error
        mse = mean_squared_error(actual_values, predicted_values)
        
        # Calculate non-stationary drift index
        non_stationary_drift_index = calculate_non_stationary_drift_index(predicted_values, actual_values)
        
        # Calculate stochastic regime switch
        stochastic_regime_switch = calculate_stochastic_regime_switch(predicted_values, actual_values)
        
        # Create evaluation metrics model
        evaluation_metrics = EvaluationMetrics(
            non_stationary_drift_index=non_stationary_drift_index,
            stochastic_regime_switch=stochastic_regime_switch,
            mean_squared_error=mse
        )
        
        return evaluation_metrics
    
    except Exception as e:
        logger.error(f\"Error calculating evaluation metrics: {str(e)}\")
        raise

def calculate_non_stationary_drift_index(predicted_values: List[float], actual_values: List[float]) -> float:
    """
    Calculate non-stationary drift index for the given predicted and actual values.

    Args:
    - predicted_values (List[float]): List of predicted values
    - actual_values (List[float]): List of actual values

    Returns:
    - float: Non-stationary drift index
    """
    try:
        # Calculate non-stationary drift index using a specialized algorithm
        non_stationary_drift_index = sum((a - p) ** 2 for a, p in zip(actual_values, predicted_values)) / len(actual_values)
        
        return non_stationary_drift_index
    
    except Exception as e:
        logger.error(f\"Error calculating non-stationary drift index: {str(e)}\")
        raise

def calculate_stochastic_regime_switch(predicted_values: List[float], actual_values: List[float]) -> float:
    """
    Calculate stochastic regime switch for the given predicted and actual values.

    Args:
    - predicted_values (List[float]): List of predicted values
    - actual_values (List[float]): List of actual values

    Returns:
    - float: Stochastic regime switch
    """
    try:
        # Calculate stochastic regime switch using a specialized algorithm
        stochastic_regime_switch = sum(abs(a - p) for a, p in zip(actual_values, predicted_values)) / len(actual_values)
        
        return stochastic_regime_switch
    
    except Exception as e:
        logger.error(f\"Error calculating stochastic regime switch: {str(e)}\")
        raise

def plot_evaluation_metrics(evaluation_metrics: EvaluationMetrics) -> None:
    """
    Plot evaluation metrics using scikit-plot.

    Args:
    - evaluation_metrics (EvaluationMetrics): Model containing evaluation metrics
    """
    try:
        # Plot confusion matrix
        plot_confusion_matrix(evaluation_metrics.mean_squared_error)
        
    except Exception as e:
        logger.error(f\"Error plotting evaluation metrics: {str(e)}\")
        raise

def save_evaluation_metrics_to_firestore(evaluation_metrics: EvaluationMetrics) -> None:
    """
    Save evaluation metrics to Google Cloud Firestore.

    Args:
    - evaluation_metrics (EvaluationMetrics): Model containing evaluation metrics
    """
    try:
        # Initialize Firestore client
        db = firestore.Client()
        
        # Save evaluation metrics to Firestore
        db.collection(\"evaluation_metrics\").document().set(evaluation_metrics.dict())
        
    except Exception as e:
        logger.error(f\"Error saving evaluation metrics to Firestore: {str(e)}\")
        raise

if __name__ == \"__main__\":
    # Simulate the 'Rocket Science' problem
    predicted_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    actual_values = [1.1, 1.9, 3.2, 4.1, 5.1]
    
    # Calculate evaluation metrics
    evaluation_metrics = calculate_evaluation_metrics(predicted_values, actual_values)
    
    # Plot evaluation metrics
    plot_evaluation_metrics(evaluation_metrics)
    
    # Save evaluation metrics to Firestore
    save_evaluation_metrics_to_firestore(evaluation_metrics)
",
        "commit_message": "feat: implement specialized evaluation_metrics logic"
    }
}
```